import whisper, os, turtle, pyaudio, wave, client_wlan

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 8000  # Record at 8000 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()
t = turtle.Turtle()
c = client_wlan.Client("localhost")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    model = whisper.load_model("medium.en")
    model.cuda()

    while True:
        cls()
        #record 5 seconds of audio
        print("Recording...")
        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)
        frames = []  # Initialize array to store frames
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        print("Finished recording.")

        #save audio file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        #transcribe audio file
        response = str(model.transcribe(filename)["text"]).lower()

        if "right" in response:
            t.right(90)
            c.send_command("right")
        elif "left" in response:
            t.left(90)
            c.send_command("left")
        elif "forward" in response or "go" in response:
            t.forward(30)
            c.send_command("forward")
        elif "backward" in response or "back" in response:
            t.backward(30)
            c.send_command("backward")

        os.remove(filename)

main()
