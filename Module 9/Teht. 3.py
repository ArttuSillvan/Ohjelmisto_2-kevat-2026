class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
    current_speed = 0
    travelled_distance = 0

    def accelerate(self, amount):
        self.current_speed += amount
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0


    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours