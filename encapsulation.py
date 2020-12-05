

class Car:
    def __init__(self, speed, colour):
        self.__speed = speed
        self.__colour = colour

    def displayInfo(self):
        print(f'Colour: {self.__colour}\nSpeed: {self.__speed} km/h')


c = Car(100, 'gray')
c.displayInfo()

# print(c.__speed, c.__colour) - will raise an AttirbuteError `'Car' object has no attribute '__speed'`
