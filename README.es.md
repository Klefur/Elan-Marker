# Marcador-Elan
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/Klefur/Marcador-Elan/blob/main/README.es.md)
### Herramienta de análisis de video

## Autores: 
[Lucas Mesías](https://www.github.com/Skyrdow) | [Joaquín Salidivia](https://www.github.com/Skyrdow) | [Nicolás Aguilera](https://www.github.com/Skyrdow)

## Instrucciones de uso
### Prerrequisitos
* Python 3.9 o superior

### Instalación de librerías
* Instalación liviana de ``torchaudio`` para CPU:
```python
pip3 install torch==1.13.1+cpu torchaudio==0.13.1+cpu
```
* Instalación de la librería ``whisper-timestamped``:
```python
pip3 install git+https://github.com/linto-ai/whisper-timestamped
```
* Instalar ``ffmpeg``:
    * En Ubuntu o Debian:
    ```python
    sudo apt update && sudo apt install ffmpeg
    ```
    * en Arch Linux:
    ```python
    sudo pacman -S ffmpeg
    ```
    * en MacOS usando Homebrew (https://brew.sh/):
    ```python
    brew install ffmpeg
    ```
    * on Windows usando Chocolatey (https://chocolatey.org/):
    ```python
    choco install ffmpeg
    ```
    * on Windows using Scoop (https://scoop.sh/):
    ```
    scoop install ffmpeg
    ```
* Instalar ONNX Runtime:
```
pip3 install onnxruntime torchaudio
```
* Audio backend torchaudio:
    * SoundFile for Windows ```pip install soundfile```
    * Sox for Linux ```pip install sox```

* Json to Elan, la cual puede ser instalada con la siguiente línea de comando:
```python
pip install json-to-elan
```
* moviepy ```pip install moviepy```

### Preparar archivos
Mover todos los archivos a procesar a la carpeta input
Los archivos .mp4 serán transformados a .wav automáticamente, para evitar la conversión se usa la flag ``--use_wav True``

## Ejecutar el programa desde la terminal
La siguiente línea de comando ejecutará el programa y marcará en la línea de tiempo las palabras que contengan las letras 's' y 'd'
```
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