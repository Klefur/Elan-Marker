# Marcador-Elan
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/Klefur/Marcador-Elan/blob/main/README.es.md)
### Herramienta de análisis de video

## Autores: 
[Lucas Mesías](https://www.github.com/Skyrdow) | [Joaquín Salidivia](https://www.github.com/Skyrdow) | [Nicolás Aguilera](https://www.github.com/Skyrdow)

## Instrucciones de uso
### Instalación de librerías
```python
pip install json-to-elan
```
### Azure

### Preparar archivos
Mover todos los archivos a procesar a la carpeta input
Los archivos .mp4 serán transformados a .wav automáticamente, para evitar la conversión se usa la flag ``--use_wav True``

## Ejecutar el programa desde la terminal
La siguiente línea de comando ejecutará el programa y marcará en la línea de tiempo las palabras que contengan las letras 's' y 'd'
```
python ./marcador_elan.py --filters s d
```
### Parámetros:
* ``--filters``: List of strings to filter (use lowercase)
* ``--input_folder``: Folder with the input files
* ``--output_folder``: Folder for output files
* ``--delete_temp``: Delete temporal files
* ``--use_wav``: Skip .wav to .mp4 conversion
* ``--name_model``: Select whisper model
* ``--language``: Select language of the audio

Los archivos generados se encontrarán en la carpeta output