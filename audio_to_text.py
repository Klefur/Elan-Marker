import whisper_timestamped as whisper
import glob
import json

def att_folder(data_path: str = "input"):
    wav_files = glob.glob(data_path + "\*.wav", recursive=False)
    for wav_path in wav_files:
        audio = whisper.load_audio(wav_path)

        model = whisper.load_model("small", device="cpu")

        result = whisper.transcribe(model, audio, language='es', 
                                    compute_word_confidence=False, vad=True,
                                    beam_size=5, best_of=5, temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0))

        wav_file_name = wav_path[:-4]
        json_output = open(f'{wav_file_name}.json', 'w', encoding='utf-8')
        json_output.write(json.dumps(result, indent = 4, ensure_ascii = False))
        json_output.close()
