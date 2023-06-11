# Marcador-Elan
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Klefur/Marcador-Elan/blob/main/README.md)
### Herramienta de análisis de video

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
    * Sox for Linux
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