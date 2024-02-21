class vehicle:
 def __init__(self,make,model,year):
    self.make = make
    self.model= model
    self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

class car(vehicle):
 def __init__(self,make,model,year,num_doors):
     super().__init__(make,model,year)
     self.num_doors = num_doors

 def __str__(self):
    return f"{self.make} {self.model} {self.num_doors}"

 def hello(self):
     print("hin")
class sedan(car):
 def __init__(self,make,model,year,num_seats,num_doors):
     super().__init__(make,model,year,num_doors)
     self.num_seats = num_seats

 def __str__(self):
    return f"{self.make} {self.model} {self.year} {self.num_seats}"


a = sedan("Toyota","6thGen",2024,20,80)
b = car("Toyota","6thGen",2024,8)
print(a)
print(b)

a.hello()

