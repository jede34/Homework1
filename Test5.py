class Car:
    vehicle_type = 'Automobile'
    def __init__(self, make, model, year):
      self.make = make 
      self.model = model
      self.year = year
    def get_info(self):
       return f'{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}'
car1 = Car('Buggati', 'Shiron', 2024)
print(car1.get_info()) 
   