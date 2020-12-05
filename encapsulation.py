

class Car:
    def __init__(self, speed, colour):
        self._speed = speed
        self._colour = colour

    def displayInfo(self):
        print(f'Colour: {self._colour}\nSpeed: {self._speed} km/h')


c = Car(100, 'gray')
c.displayInfo()

print(c._speed, c._colour)
