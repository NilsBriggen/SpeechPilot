# SpeechPilot
A library to control a robot with speech recognition

## Requirements
- [Python 3.10.13](https://www.python.org/downloads/release/python-31013/)
- [Whisper](https://pypi.org/project/openai-whisper/)
- [pyAudio](https://pypi.org/project/PyAudio/)
### Optional
[CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive). This is technically not required, but it will speed up the speech recognition by a lot. **Needs a Nvidia GPU!** 
For this to work you also need [Visual Studio 2019](https://visualstudio.microsoft.com/de/downloads/) or above.
You also need to install [pyTorch](https://pytorch.org/get-started/locally/) with CUDA support
<br>
<br>
## My Progress in SpeechPilot
### 19.06.2023

Done:
- control libary finished and checked robot functions
- Implemented the first version of the speech recognition with whisper and turtle

Problems:
- The speech recognition is slow (probably because I'm using the API)
- Tensorflow doesn't work on the Raspberry Pi Zero
- The Picon Board is instable and can disconnect from the Raspberry Pi Zero

### 20.06.2023
Done:
- Implemented my own speech recognition with Tensorflow

Problems:
- The Tensorflow model isn't giving a usable output (probably because of the model or the microphone input)


### 21.06.2023
Done:
- Implemented a new speech recognition with a local model of whisper
- Implemented Wlan/Bluetooth communication with the Raspberry Pi Zero (Work in Progress)
- The Whisper model is now fast enough to be used in real time

Problems:
- The Wlan communication gets refused by the server (probably because of a firewall)
- The Bluetooth communication doesn't work in Linux

### 22.06.2023
Done:
- The Wlan communication works now
- The Robot fully works with the "remote" speech recognition

Problems:
- My own model still doesn't work

### 23.06.2023
Done:
- The tiny.en model is too large for the Raspberry Pi Zero. The conversion will have to be done outside of the Raspberry Pi
- Cleaned up code

Problems:
- My own model still doesn't work

## Todo:
- Try to fix my model
- Write the paper
