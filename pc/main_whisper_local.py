import whisper, os, pyaudio, wave, client_wlan

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 8000  # Record at 8000 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()
c = client_wlan.Client("192.168.1.194")

# Function for clearing the console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    #connect to server
    c.connect()
    #load model
    model = whisper.load_model("medium.en")
    #move model to gpu
    model.cuda()
    try:
        while True:
            cls()
            #record 5 seconds of audio
            print("Recording...")
            stream = p.open(format=sample_format,
                            channels=channels,
                            rate=fs,
                            frames_per_buffer=chunk,
                            input=True)
            frames = []  # Initialize array to store audio frames
            for i in range(0, int(fs / chunk * seconds)):
                data = stream.read(chunk)
                frames.append(data)
            stream.stop_stream()
            stream.close()
            print("Finished recording.")

            #save audio file
            audioFile = wave.open(filename, 'wb')
            audioFile.setnchannels(channels)
            audioFile.setsampwidth(p.get_sample_size(sample_format))
            audioFile.setframerate(fs)
            audioFile.writeframes(b''.join(frames))
            audioFile.close()

            #transcribe audio file
            response = str(model.transcribe(filename)["text"]).lower()

            #send command to robot
            if "right" in response:
                c.send_command("right")
            elif "left" in response:
                c.send_command("left")
            elif "forward" in response or "go" in response:
                c.send_command("forward")
            elif "backward" in response or "back" in response:
                c.send_command("backward")

            os.remove(filename)
    except KeyboardInterrupt:
        os.remove(filename)
        c.close()
        exit()

main()
