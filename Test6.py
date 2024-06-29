class Car:
    vehicle_type = "Automobile"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"
car_ford = Car('Ford', 'Mustang', 2022)
car_toyota = Car('Toyota','Corolla', 2021)
print(car_ford.get_info())
print(car_toyota.get_info())



