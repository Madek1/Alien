from src.connect import *


class Main(object):
    @staticmethod
    def start():
        print("Hello World!")
        alien = Alien()
        alien.connect()


if __name__ == '__main__':
    Main().start()
