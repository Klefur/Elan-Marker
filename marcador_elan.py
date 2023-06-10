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

wav_folder = "input" # variable
output_folder = "output" # variable
flag_delete_temp_files = False # variable

print("\nSpeech to text:")
att_folder(wav_folder)
print("Done!")

print("\nApplying filters:")
filter_json(wav_folder, filters=["d", "t"])
print("Done!")

print("\Making elan:")
make_elan(data_dir=output_folder)

if (flag_delete_temp_files):
    delete_temp_files()

print("Done!")