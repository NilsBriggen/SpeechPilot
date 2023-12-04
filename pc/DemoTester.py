import client_wlan
IP_ADDRESS = "raspberrypi.local"

c = client_wlan.Client(IP_ADDRESS)
c.connect()

c.send_command("forward")

c.close()