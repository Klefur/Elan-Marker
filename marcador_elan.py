import xml.etree.ElementTree as ET
from json_to_elan import make_elan
from detector import filter_json
from audio_to_text import att_folder
from moviepy.editor import *
import os
import glob
import argparse

def delete_temp_files(wav_folder, output_folder):
    temp_wav_files = glob.glob(wav_folder + "\*.json", recursive=False)
    for temp in temp_wav_files:
        os.remove(temp)
    temp_json_files = glob.glob(output_folder + "\*.json", recursive=False)
    for temp in temp_json_files:
        os.remove(temp)

def make_folder(name_folder):
    if not os.path.exists(name_folder):
        try:
            os.mkdir(name_folder)
            print("The folder '{}' has been created successfully.".format(name_folder))
        except Exception as e:
            print("An error occurred while creating the folder. '{}': {}".format(name_folder, str(e)))
    else:
        print("The folder '{}' already exists. Skipping.".format(name_folder))

def link_mp4_to_elan(output_folder):
    """
    Swap the link from the .wav file to the .mp4 file
    """
    eaf_files = glob.glob(output_folder + "\*.eaf", recursive=False)
    for eaf in eaf_files:
        tree = ET.parse(eaf)
        root = tree.getroot()
        file_name = eaf[len(output_folder)+1:-4]
        new_parameters = {
            'MEDIA_URL': file_name + ".mp4",
            'MIME_TYPE': "video/mp4"
        }
        # Search for the header 'MEDIA_DESCRIPTOR'
        for media_descriptor in root.iter('MEDIA_DESCRIPTOR'):
            # Modificar los parámetros
            for key, value in new_parameters.items():
                media_descriptor.set(key, value)

        # Save the changes to the XML file
        tree.write(eaf)

def mp4_to_wav(input_folder):
    mp4_files = glob.glob(input_folder + "\*.mp4", recursive=False)
    for mp4 in mp4_files:
        video = VideoFileClip(mp4)
        audio = video.audio
        audio.write_audiofile(f'{mp4[:-4]}.wav')

def main():
    parser = argparse.ArgumentParser(description='Add timestamps with filters to ELAN files')
    parser.add_argument('-f', '--filters', nargs='+', help='List of strings to filter (use lowercase)', default=["s", "d"])
    parser.add_argument('-i', '--input_folder', help='Folder with the input files', default='input')
    parser.add_argument('-o', '--output_folder', help='Folder for output files', default='output')
    parser.add_argument('-t', '--save_temp', action='store_true', help='Save temporal files', default=False)
    parser.add_argument('-w', '--use_wav', action='store_true', help='Skip .wav to .mp4 conversion', default=False)
    parser.add_argument('-m', '--name_model', help='Select whisper model', default='small')
    parser.add_argument('-l', '--language', help='Select language of the audio: {af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba}', default='es')
    args = parser.parse_args()

    if args.input_folder == args.output_folder:
        print("Input and Output folders can't be the same.")
        exit(1)

    if not args.use_wav:
        print("\nConverting wav files:")
        mp4_to_wav(args.input_folder)
        print("Done!")

    print("\nSpeech to text:")
    att_folder(args.input_folder, args.name_model, args.language)
    print("Done!")

    print("\nApplying filters.")
    filter_json(args.input_folder, args.filters)
    print("Done!")

    print("\nMaking output folder:")
    make_folder(args.output_folder)
    print("Done!")
    
    print("\nMaking elan.")
    make_elan(tier_name="Marcador elan", data_dir=args.output_folder)
    link_mp4_to_elan(args.output_folder)

    if not args.save_temp:
        print("Deleting temp files")
        delete_temp_files(args.input_folder, args.output_folder)

    print("Done!")


if __name__ == '__main__':
    main()
