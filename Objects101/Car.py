# # A class is a recipe
# # An object is the food you made with the recipe
# # The recipe can be used lots and lots of times

# # Our blueprint for making cars is called Car
# class Car(object):
#     # Whenever we start making a new car, __init__ will run
#     # we ALWAYS pass self first
#     def __init__(self):
#         # self is special
#         # self refers to THIS object
#         self.make = "Honda"
#         self.model = "Accord"
#         self.year = 2007
# myCar = Car()
# print myCar.make
# yourCar = Car()
# print yourCar.make
# yourCar.make = "Toyota"
# print yourCar.make

class Car(object):
    def __init__(self,make, model):
        self.make = make
        self.model = model
    def changeModel(self, newModel):
        self.model = newModel

zachsCar = Car('Ford','F150')
chrisCar = Car('Chevy','Silverado')
print zachsCar.make
print zachsCar.model
print chrisCar.make
print chrisCar.model

zachsCar.model = "Focus"
# ZACHS CAR: DON'T MESS WITH ME
print zachsCar.model
zachsCar.changeModel("Fiesta")
print zachsCar.model