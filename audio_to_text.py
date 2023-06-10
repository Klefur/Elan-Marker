import whisper_timestamped as whisper
import glob
import json

def att_folder(data_path: str = "input", name_model:str = "small", language:str = "es"):
    wav_files = glob.glob(data_path + "\*.wav", recursive=False)
    for wav_path in wav_files:
        audio = whisper.load_audio(wav_path)

        model = whisper.load_model(name_model, device="cpu")
        print(wav_path)
        result = whisper.transcribe(model, audio, language, 
                                    compute_word_confidence=False, vad=True)

        wav_file_name = wav_path[:-4]
        json_output = open(f'{wav_file_name}.json', 'w', encoding='utf-8')
        json_output.write(json.dumps(result, indent = 4, ensure_ascii = False))
        json_output.close()
