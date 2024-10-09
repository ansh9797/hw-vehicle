class Vehicle:
    def intro(self):
        print("Max speed:", self.max_speed())
        print("Fuel type:", self.fuel_type())
    
    def fuel_type(self):
        pass
    
    def max_speed(self):
        pass
    
class BMW(Vehicle):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari(Vehicle):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "350 km/h"

b1 = BMW()
b1.intro()

f1 = Ferrari()
f1.intro()

