import socket, os, time

# Function for clearing the console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Client:
    # Constructor
    def __init__(self, ip):
        cls()
        self.server_address = (ip , 12345)
        # Connect to server on Raspberry Pi
        while True:
            try:
                print("Trying to connect to server...")
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect(self.server_address)
                break
            except Exception as e:
                cls()
                print(f"Could not connect to server. Retrying...\n{e}")
                time.sleep(3)

    # Send command to server
    def send_command(self, command):
        response = b""
        while response != b"OK":
            self.socket.sendall(command.encode())
            response = self.socket.recv(1024)

    # Close connection
    def close(self):
        self.socket.close()
