# Marker-Elan
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/Klefur/Marcador-Elan/blob/main/README.es.md)
### Video Analysis tool

## Authors: 
[Lucas Mesías](https://www.github.com/Skyrdow) | [Joaquín Salidivia](https://www.github.com/Skyrdow) | [Nicolás Aguilera](https://www.github.com/Don-Uldaricio)

## Use instructions
### Prerrequisitos
* Python 3.9 or newer

### Library installation
* ``torchaudio`` light installation for CPU:
```python
pip3 install torch==1.13.1+cpu torchaudio==0.13.1+cpu
```
* Install ``whisper-timestamped`` library:
```python
pip3 install git+https://github.com/linto-ai/whisper-timestamped
```
* Install ``ffmpeg``:
    * On Ubuntu or Debian:
    ```python
    sudo apt update && sudo apt install ffmpeg
    ```
    * On Arch Linux:
    ```python
    sudo pacman -S ffmpeg
    ```
    * On MacOS using Homebrew (https://brew.sh/):
    ```python
    brew install ffmpeg
    ```
    * on Windows using Chocolatey (https://chocolatey.org/):
    ```python
    choco install ffmpeg
    ```
    * on Windows using Scoop (https://scoop.sh/):
    ```
    scoop install ffmpeg
    ```
* Install ONNX Runtime:
```
pip3 install onnxruntime torchaudio
```
* Audio backend torchaudio:
    * SoundFile for Windows ```pip install soundfile```
    * Sox for Linux ```pip install sox```

* Json to Elan, with follow command line:
```python
pip install json-to-elan
```
* moviepy ```pip install moviepy```

### Setup files
Move all files to process to the input folder. 
The .mp4 files will be automatically transformed into .wav files. To avoid the conversion, use the flag "--use_wav True."


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