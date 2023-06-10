1. python 3.9+
2. torchaudio Light installation for CPU
   pip3 install torch==1.13.1+cpu torchaudio==0.13.1+cpu -f https://download.pytorch.org/whl torch_stable.html
3. pip3 install git+https://github.com/linto-ai/whisper-timestamped
4. ffmpeg
    1. on Ubuntu or Debian
    sudo apt update && sudo apt install ffmpeg

    2. on Arch Linux
    sudo pacman -S ffmpeg

    3. on MacOS using Homebrew (https://brew.sh/)
    brew install ffmpeg

    4. on Windows using Chocolatey (https://chocolatey.org/)
    choco install ffmpeg

    5. on Windows using Scoop (https://scoop.sh/)
    scoop install ffmpeg
5. pip3 install onnxruntime torchaudio
6. Audio backend torchaudio
   1. SoundFile for Windows pip install soundfile
   2. Sox for Linux pip install sox
7. pip install json_to_elan
8. pip install moviepy