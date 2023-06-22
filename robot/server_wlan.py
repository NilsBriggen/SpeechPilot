import socket, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Server:
    def __init__(self):
        cls()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('', 12345)
        self.server_socket.bind(self.server_address)
        self.server_socket.listen(1)
        print(f"Server started, waiting for client connection (ip: {self.server_address})...")

    def wait_for_connection(self):
        self.client_socket, self.client_address = self.server_socket.accept()
        print("Client connected:", self.client_address)

    def receive_command(self):
        try:
            data = self.client_socket.recv(1024)
            command = data.decode().strip()
            return command
        except:
            cls()
            print(f"Client disconnected.\nWaiting for new connection...")
            self.wait_for_connection()

    def send_response(self, response):
        try:
            self.client_socket.sendall(response.encode())
        except:
            cls()
            print(f"Client disconnected.\nWaiting for new connection...")
            self.wait_for_connection()

    def close(self):
        self.client_socket.close()
        self.server_socket.close()
