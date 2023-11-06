class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

vehicle_type = input("Enter vehicle type: ")
year = input("Enter year: ")
make = input("Enter make: ")
model = input("Enter model: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter roof type (solid or sun roof): ")

car = Automobile(vehicle_type, year, make, model, doors, roof)

print(f"Vehicle type: {car.vehicle_type}")
print(f"Year: {car.year}")
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Doors: {car.doors}")
print(f"Roof: {car.roof}")
