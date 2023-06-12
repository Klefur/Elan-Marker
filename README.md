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
    * Sox for Linux/MacOs
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

The generated files will be in output folder

## Acknowlegment
* [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped): Multilingual Automatic Speech Recognition with word-level timestamps and confidence (License AGPL-3.0)
* [whisper](https://github.com/openai/whisper): Whisper speech recognition (License MIT).
* [dtw-python](https://pypi.org/project/dtw-python): Dynamic Time Warping (License GPL v3).

## Paper Citations
If you incorporate this in your research, reference the repository as the source.

```bibtex
@misc{lintoai2023whispertimestamped,
  title={Marcador-elan},
  author={Louradour, J{\'e}r{\^o}me},
  journal={GitHub repository},
  year={2023},
  publisher={GitHub},
  howpublished = {\url{https://github.com/Klefur/Marcador-Elan}}
}
```

Whisper-timestamped:

```bibtex
@misc{lintoai2023whispertimestamped,
  title={whisper-timestamped},
  author={Louradour, J{\'e}r{\^o}me},
  journal={GitHub repository},
  year={2023},
  publisher={GitHub},
  howpublished = {\url{https://github.com/linto-ai/whisper-timestamped}}
}
```

OpenAI Whisper paper:

```bibtex
@article{radford2022robust,
  title={Robust speech recognition via large-scale weak supervision},
  author={Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and McLeavey, Christine and Sutskever, Ilya},
  journal={arXiv preprint arXiv:2212.04356},
  year={2022}
}
```

Dynamic-Time-Warping:

```bibtex
@article{JSSv031i07,
  title={Computing and Visualizing Dynamic Time Warping Alignments in R: The dtw Package},
  author={Giorgino, Toni},
  journal={Journal of Statistical Software},
  year={2009},
  volume={31},
  number={7},
  doi={10.18637/jss.v031.i07}
}
```