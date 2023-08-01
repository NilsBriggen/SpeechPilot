import bluetooth

def handle_client(client_sock):
    try:
        while True:
            data = client_sock.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received: {data}")
            if data.lower() == 'exit':
                break
            else:
                response = "Command received: " + data
                client_sock.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    client_sock.close()
    print("Client disconnected")


def main():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = bluetooth.PORT_ANY
    server_sock.bind(("", port))
    server_sock.listen(1)

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"  # Make sure to use the same UUID on the client-side
    bluetooth.advertise_service(server_sock, "RaspiZero",
                                 service_id=uuid,
                                 service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                 profiles=[bluetooth.SERIAL_PORT_PROFILE])

    print("Waiting for connection on RFCOMM channel %d" % server_sock.getsockname()[1])

    try:
        while True:
            client_sock, client_info = server_sock.accept()
            print(f"Accepted connection from {client_info}")
            handle_client(client_sock)
    except KeyboardInterrupt:
        server_sock.close()
        print("Server stopped")


if __name__ == '__main__':
    main()