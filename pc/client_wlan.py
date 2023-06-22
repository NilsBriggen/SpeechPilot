import socket, os, time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Client:
    def __init__(self, ip):
        cls()
        self.server_address = (ip , 12345)
    
    def connect(self):
        cls()
        while True:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect(self.server_address)
                break
            except Exception as e:
                print(f"Could not connect to server. Retrying...\n{e}")
                time.sleep(3)

    def send_command(self, command):
        try:
            response = b""
            while response != b"OK":
                self.socket.sendall(command.encode())
                response = self.socket.recv(1024)
        except:
            cls()
            print("Connection lost.")
            self.connect()
            self.send_command(command)

    def close(self):
        self.socket.close()

