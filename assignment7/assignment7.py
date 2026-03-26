import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


car = Car("ABC-123", 142)

print(car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance)


car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(car.current_speed)

car.accelerate(-200)
print(car.current_speed)


car.current_speed = 60
car.travelled_distance = 2000

car.drive(1.5)
print(car.travelled_distance)


cars = []

for i in range(10):
    max_speed = random.randint(150, 200)
    cars.append(Car(f"ABC-{i+1}", max_speed))

race_finished = False

while not race_finished:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True

print("\nRace results:")
print("Reg\tMax\tSpeed\tDistance")

for car in cars:
    print(f"{car.registration_number}\t{car.maximum_speed}\t{car.current_speed}\t{car.travelled_distance}")