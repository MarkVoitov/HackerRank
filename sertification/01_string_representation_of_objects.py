class Car:
    def __init__(self, speed, unit):
        self.speed = speed
        self.unit = unit

    def __str__(self):
        return 'Car with the maximum speed of ' + str(self.speed) + ' ' + (self.unit)


class Boat:
    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        return 'Boat with the maximum speed of ' + str(self.speed) + ' knots'
