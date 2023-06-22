import server_wlan, controller

DISTANCE = 30
ANGLE = 90

s = server_wlan.Server()
c = controller.Controller()

# Wait for connection
s.wait_for_connection()

while True:
    # Receive command from client
    command = s.receive_command()
    print(command)
    # Execute command
    if command == "forward":
        c.forward(DISTANCE)
    elif command == "backward":
        c.reverse(DISTANCE)
    elif command == "left":
        c.left(ANGLE)
    elif command == "right":
        c.right(ANGLE)
    elif command == "exit":
        break

    # Send response to client
    s.send_response("OK")
