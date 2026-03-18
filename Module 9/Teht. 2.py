class Car:
    def __init__(self, license_plate, maximum_speed, accelerate ):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.accelerate = accelerate
    current_speed = 0
    travelled_distance = 0
    accelerate = 0

car = Car("ABC-123", 142, 10 )




print(f"Current speed: {car.accelerate} km/h")

print(f"Current speed: {car.current_speed} km/h")


