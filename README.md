# SpeechPilot
A library to control a robot with speech recognition
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

## Todo:
- Try if the tiny.en model runs on the Raspberry Pi Zero
- Figure out a way to talk to the raspberry pi zero over wifi/bluetooth
