# A class can function as a blueprint to create objects.

class Car:
    
# Constructor
    def __init__(self, make, model, year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

# Methods
    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")