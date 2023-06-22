import server_wlan, controller

DISTANCE = 30
ANGLE = 90

s = server_wlan.Server()
c = controller.Controller()

s.wait_for_connection()

while True:
    command = s.receive_command()
    print(command)
    if command == "forward":
        c.forward(DISTANCE)
        pass
    elif command == "backward":
        c.reverse(DISTANCE)
        pass
    elif command == "left":
        c.left(ANGLE)
        pass
    elif command == "right":
        c.right(ANGLE)
        pass
    elif command == "exit":
        break

    s.send_response("OK")
