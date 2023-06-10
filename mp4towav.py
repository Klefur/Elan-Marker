from moviepy.editor import *

# Ruta del archivo MP4
ruta_mp4 = 'input\Piloto informante F.mp4'

# Ruta de salida del archivo WAV
ruta_wav = 'Piloto informante F.wav'

# Cargar el archivo MP4
video = VideoFileClip(ruta_mp4)

# Extraer el audio del archivo MP4
audio = video.audio

# Guardar el audio en formato WAV
audio.write_audiofile(ruta_wav)

ruta_wav = 'Piloto informante M.wav'
ruta_mp4 = 'input\Piloto informante M.mp4'

# Cargar el archivo MP4
video = VideoFileClip(ruta_mp4)

# Extraer el audio del archivo MP4
audio = video.audio

# Guardar el audio en formato WAV
audio.write_audiofile(ruta_wav)