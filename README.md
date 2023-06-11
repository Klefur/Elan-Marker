# Marker-Elan
### Video Analysis tool
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/Klefur/Marcador-Elan/blob/main/README.es.md)

## Authors: 
[Lucas Mesías](https://github.com/Skyrdow) | [Joaquín Salidivia](https://github.com/Klefur) | [Nicolás Aguilera](https://github.com/Don-Uldaricio)

## Use instructions
### Prerequisites
* Python 3.9 or newer

### Library installation
* Install ``whisper-timestamped`` library:
```bash
pip3 install git+https://github.com/linto-ai/whisper-timestamped
```
* Install ``ffmpeg``:
    * On Ubuntu or Debian:
    ```bash
    sudo apt update && sudo apt install ffmpeg
    ```
    * On Arch Linux:
    ```bash
    sudo pacman -S ffmpeg
    ```
    * On MacOS using Homebrew (https://brew.sh/):
    ```bash
    brew install ffmpeg
    ```
    * on Windows using Chocolatey (https://chocolatey.org/):
    ```bash
    choco install ffmpeg
    ```
    * on Windows using Scoop (https://scoop.sh/):
    ```bash
    scoop install ffmpeg
    ```
* Install ONNX Runtime:
```bash
pip3 install onnxruntime torchaudio
```
* Audio backend torchaudio:
    * SoundFile for Windows 
    ```bash
    pip install soundfile
    ```
    * Sox for Linux 
    ```bash
    pip install sox
    ```
* moviepy 
```bash
pip install moviepy
```

### Setup files
Move all files to process to the input folder. 
The .mp4 files will be automatically transformed into .wav files. To avoid the conversion, use the flag ``--use_wav True``


## Run the program from the terminal
The following command line will execute the program and mark on the timeline the words that contain the letters 's' and 'd'.
```
python ./marcador_elan.py --filters s d
```
### Parameters:
* ``--filters``: List of strings to filter (use lowercase)
* ``--input_folder``: Folder with the input files
* ``--output_folder``: Folder for output files
* ``--delete_temp``: Delete temporal files
* ``--use_wav``: Skip .wav to .mp4 conversion
* ``--name_model``: Select [whisper model](https://github.com/openai/whisper/tree/main#available-models-and-languages)
* ``--language``: Select language of the audio

The generate files will be in output folder