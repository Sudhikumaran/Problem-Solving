"""instance & class variables
instance are specific to each object
class variables are shared across all instances of the class"""

class Car: 
    wheels = 4 # class variable

    def __init__(self, color, mileage):
        self.color = color  # instance variable
        self.mileage = mileage  # instance variable

car1 = Car("red", 10000)
car2 = Car("blue", 5000)

print(f"Car 1: Color={car1.color}, Mileage={car1.mileage}, Wheels={car1.wheels}")
print(f"Car 2: Color={car2.color}, Mileage={car2.mileage}, Wheels={car2.wheels}")
# Modifying instance variable
car1.color = "green"
print(f"After modification, Car 1: Color={car1.color}, Mileage={car1.mileage}, Wheels={car1.wheels}")
# Modifying class variable 
Car.wheels = 6
print(f"After modification, Car 1: Color={car1.color}, Mileage={car1.mileage}, Wheels={car1.wheels}")
print(f"After modification, Car 2: Color={car2.color}, Mileage={car2.mileage}, Wheels={car2.wheels}")
