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


wav_folder = "input" # variable
output_folder = "output" # variable
flag_delete_temp_files = False # variable

print("\nSpeech to text:")
att_folder(wav_folder)
print("Done!")

print("\nApplying filters:")
filter_json(wav_folder, filters=["d", "t"])
print("Done!")

print("\nMaking elan:")
make_folder(output_folder)
make_elan(tier_name="marcador elan", data_dir=output_folder)

if (flag_delete_temp_files):
    delete_temp_files()

print("Done!")