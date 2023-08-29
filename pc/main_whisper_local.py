import whisper, os, pyaudio, wave, client_wlan


ENABLE_WLAN_CLIENT = False
ENABLE_CUDA = True


# Function for clearing the console
def cls():
    os.system("cls" if os.name == "nt" else "clear")


cls()
print("Initializing...")

# initialize pyaudio
CHUNK = 1024  # Record in Chunks of 1024 samples
SAMPLE_FORMAT = pyaudio.paInt16  # 16 bits per sample
CHANNELS = 2
FS = 8000  # Record at 8000 samples per second
SECONDS = 5
MINUTES = 0
FILENAME = "output.wav"
TIME = SECONDS + MINUTES * 60

if TIME < 3:
    print("ERROR: Recording time too short.")
    

p = pyaudio.PyAudio()


def main():
    # connect to server
    if ENABLE_WLAN_CLIENT:
        c = client_wlan.Client("192.168.1.194")
        c.connect()
    # load model
    cls()
    print("Loading model...")
    model = whisper.load_model("small.en")
    # move model to gpu
    if ENABLE_CUDA:
        model.cuda()
    try:
        while True:
            # record a given amount of audio (see SECONDS and MINUTES)
            print("Recording...", end="\r")
            stream = p.open(
                format=SAMPLE_FORMAT,
                channels=CHANNELS,
                rate=FS,
                frames_per_buffer=CHUNK,
                input=True,
            )
            frames = []  # Initialize array to store audio frames
            for _ in range(int(FS / CHUNK * TIME)):
                data = stream.read(CHUNK)
                frames.append(data)
            stream.stop_stream()
            stream.close()
            print("Finished recording.", end="\r")

            # save audio file
            audioFile = wave.open(FILENAME, "wb")
            audioFile.setnchannels(CHANNELS)
            audioFile.setsampwidth(p.get_sample_size(SAMPLE_FORMAT))
            audioFile.setframerate(FS)
            audioFile.writeframes(b"".join(frames))
            audioFile.close()

            # transcribe audio file
            response = str(model.transcribe(FILENAME)["text"]).lower()

            # send command to robot
            if ENABLE_WLAN_CLIENT:
                if "right" in response:
                    c.send_command("right")
                elif "left" in response:
                    c.send_command("left")
                elif "forward" in response or "go" in response:
                    c.send_command("forward")
                elif "backward" in response or "back" in response:
                    c.send_command("backward")

            print(response)

            os.remove(FILENAME)
    except Exception as e:
        if e != KeyboardInterrupt:
            print(e)
        if ENABLE_WLAN_CLIENT:
            c.close()
        os.remove(FILENAME)
        cls()
        exit()


main()
