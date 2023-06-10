import xml.etree.ElementTree as ET
from json_to_elan import make_elan
from detector import filter_json
from audio_to_text import att_folder
import os
import glob

def delete_temp_files():
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
        print("The folder '{}' already exists.".format(name_folder))

def link_mp4_to_elan(output_folder):
    """
    Swap the link from the .wav file to the .mp4 file
    """
    eaf_files = glob.glob(output_folder + "\*.eaf", recursive=False)
    for eaf in eaf_files:
        tree = ET.parse(eaf)
        root = tree.getroot()
        file_name = eaf[len(output_folder)+1:-4]
        print(file_name)
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


wav_folder = "input" # variable
output_folder = "output" # variable
flag_delete_temp_files = False # variable
flag_mp4_to_wav = True # variable

if (flag_mp4_to_wav):
    print("\nConverting wav files:")
#    mp4towav(wav_folder)
    print("Done!")

print("\nSpeech to text:")
att_folder(wav_folder)
print("Done!")

print("\nApplying filters:")
filter_json(wav_folder, filters=["d", "t"])
print("Done!")

print("\nMaking elan:")
make_folder(output_folder)
make_elan(tier_name="Marcador elan", data_dir=output_folder)
link_mp4_to_elan(output_folder)

if (flag_delete_temp_files):
    delete_temp_files()

print("Done!")