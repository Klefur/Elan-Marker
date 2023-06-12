# Marcador-Elan
### Herramienta de análisis de video
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Klefur/Marcador-Elan/blob/main/README.md)

## Autores: 
[Lucas Mesías](https://github.com/Skyrdow) | [Joaquín Salidivia](https://github.com/Klefur) | [Nicolás Aguilera](https://github.com/Don-Uldaricio)

## Instrucciones de uso
### Prerrequisitos
* Python 3.9 o superior

### Instalación de librerías
* Instalación de la librería ``whisper-timestamped``:
```bash
pip3 install git+https://github.com/linto-ai/whisper-timestamped
```
* Instalar ``ffmpeg``:
    * En Ubuntu o Debian:
    ```bash
    sudo apt update && sudo apt install ffmpeg
    ```
    * en Arch Linux:
    ```bash
    sudo pacman -S ffmpeg
    ```
    * en MacOS usando Homebrew (https://brew.sh/):
    ```bash
    brew install ffmpeg
    ```
    * on Windows usando Chocolatey (https://chocolatey.org/):
    ```bash
    choco install ffmpeg
    ```
    * on Windows using Scoop (https://scoop.sh/):
    ```bash
    scoop install ffmpeg
    ```
* Instalar ONNX Runtime:
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

### Preparar archivos
Mover todos los archivos a procesar a la carpeta input
Los archivos .mp4 serán transformados a .wav automáticamente, para evitar la conversión se usa la flag ``--use_wav True``

## Ejecutar el programa desde la terminal
La siguiente línea de comando ejecutará el programa y marcará en la línea de tiempo las palabras que contengan las letras 's' y 'd'
```bash
python ./marcador_elan.py --filters s d
```
### Parámetros:
* ``--filters``: Lista de strings a filtrar (usar minúsculas)
* ``--input_folder``: Carpeta con los archivos de entrada
* ``--output_folder``: Carpeta con los archivos de salida
* ``--delete_temp``: Borrar archivos temporales
* ``--use_wav``: Saltar la conversión de .wav a .mp4
* ``--name_model``: Seleccionar modelo de conversión
* ``--language``: Seleccionar el idioma del audio

Los archivos generados se encontrarán en la carpeta output


## Reconocimientos
* [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped): Multilingual Automatic Speech Recognition with word-level timestamps and confidence (License AGPL-3.0).
* [whisper](https://github.com/openai/whisper): Whisper speech recognition (License MIT).
* [dtw-python](https://pypi.org/project/dtw-python): Dynamic Time Warping (License GPL v3).
* [json-to-elan](https://github.com/CoEDL/elan-helpers): Tools and scripts for working with ELAN (License Apache-2.0).

## Citas de artículos
Si incorporas esto en tu investigación, haz referencia al repositorio como fuente.

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