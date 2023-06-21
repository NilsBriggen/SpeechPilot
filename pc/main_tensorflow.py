from keras.models import load_model
import pyaudio
import numpy as np
from scipy.signal import resample

model = load_model('model.h5')
classes = ['_background_noise_', 'eight', 'five', 'four', 'go', 'left', 'nine', 'one', 'right', 'seven', 'six', 'stop', 'three', 'two', 'zero']

def record_audio(record_seconds=4):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 8000

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []
    for _ in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    raw_data = b"".join(frames)
    array_data = np.frombuffer(raw_data, dtype=np.int16)

    return array_data

while True:
    sample = record_audio()
    sample = resample(sample, 8000)
    sample = sample.reshape(-1,8000,1)
    prob = model.predict(sample, verbose = 1)
    index=np.argmax(prob)
    print(classes[index])