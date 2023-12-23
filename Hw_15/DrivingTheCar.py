import random


class Car:
    def __init__(self, model, color, economy, initial_mileage=0, initial_fuel=100):
        self.mileage = initial_mileage
        self.fuel = initial_fuel
        self.model = model
        self.color = color
        self.economy = economy

    def drive(self, distance):
        required_fuel = (distance / 100) * self.economy
        if required_fuel > self.fuel:
            print(f"Error: Not enough fuel to cover the distance {distance} km.")
        else:
            self.fuel -= required_fuel
            self.mileage += distance
            print(f"Mileage {distance} km. Fuel reserve: {self.fuel}.")

    def distance_left(self):
        return (self.fuel / self.economy) * 100

    def fuel_up(self, amount):
        self.fuel += amount
        print(f"Fuelled car. Fuel reserve: {self.fuel} litres.")

cars = []

models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]

for _ in range(10):
    model = random.choice(models)
    color = random.choice(["Yellow", "Ruby", "White", "Orange", "Black"])
    economy = random.randint(8, 12,)
    car = Car(model, color, economy)
    cars.append(car)

for car in cars:
    car.drive(200)
    car.fuel_up(20)
    car.drive(100)

max_fuel_car = max(cars, key=lambda x: x.fuel)

print(f"\nThe car with the most fuel remaining: {max_fuel_car.color} {max_fuel_car.model}")
print(f"Fuel reserve: {max_fuel_car.fuel} litres.")
print(f"Mileage: {max_fuel_car.mileage} km.")
print(f"Remaining fuel allows you to travel further {max_fuel_car.distance_left()} km.")