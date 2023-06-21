import server_wlan, controller

DISTANCE = 30
ANGLE = 90

s = server_wlan.Server()
c = controller.Controller()

s.wait_for_connection()

while True:
    command = s.receive_command()
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
    s.send_response("OK")
