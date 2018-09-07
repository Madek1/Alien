import telnetlib
import time


class Alien(object):
    def connect(self):
        # Connect with Alien
        telnet = telnetlib.Telnet("192.168.0.24", "23")

        # Name
        print(telnet.read_until(b"Username>"))
        telnet.write(b"alien\n")

        # Password
        print(telnet.read_until(b"Password>"))
        telnet.write(b"password\n")

        print(telnet.read_until(b"Alien>"))

        # Send command
        while True:
            telnet.write(b"get TagList\n")
            time.sleep(1)
            print(telnet.read_until(b'Alien>'))
            print("\n")
