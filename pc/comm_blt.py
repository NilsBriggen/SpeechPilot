import bluetooth
import sys

def main():
    target_address = None
    target_name = "RaspiZero"  # Make sure to use the same name on the server-side

    nearby_devices = bluetooth.discover_devices()

    for address in nearby_devices:
        name = bluetooth.lookup_name(address)
        if name == target_name:
            target_address = address
            break

    if target_address is None:
        print("Server not found")
        sys.exit(1)

    port = 0  # Set the same port number as the server-side
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"  # Set the same UUID as the server-side

    service_matches = bluetooth.find_service(uuid=uuid, address=target_address)

    if len(service_matches) == 0:
        print("Service not found")
        exit()

    first_match = service_matches[0]
    port = first_match["port"]
    name = first_match["name"]
    host = first_match["host"]

    print(f"Connecting to {name} on {host}")

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))

    try:
        while True:
            command = input("Enter command (or 'exit' to quit): ")
            sock.send(command.encode('utf-8'))
            if command.lower() == "exit":
                break
            response = sock.recv(1024).decode('utf-8')
            print(f"Response: {response}")
    except KeyboardInterrupt:
        sock.send("exit".encode('utf-8'))
    finally:
        sock.close()


if __name__ == '__main__':
    main()