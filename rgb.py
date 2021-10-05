# Classes, Modules, & Objects, Lucy Gray 29.09.21
import simpleio

class RGB:
    def __init__(self, rPin, gPin, bPin):
        self.rPin = rPin
        self.gPin = gPin
        self.bPin = bPin

    def red(self):
        self.color((255, 0, 0))
        print("red!")

    def green(self):
        self.color((0, 255, 0))
        print("green!")

    def blue(self):
        self.color((0, 0, 255))
        print("blue!")

    def cyan(self):
        self.color((0, 255, 255))
        print("cyan!")

    def magenta(self):
        self.color((255, 0, 255))
        print("magenta!")

    def yellow(self):
        self.color((255, 255, 0))
        print("yellow!")

    def rainbow(self):