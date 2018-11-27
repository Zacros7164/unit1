class Car(object):
    def __init__(self, make, model, mpg):
        self.make = make
        self.model = model
        self.mpg = mpg
    def startCar(self):
        print "%s goes vroom" % self.model

# myCar = Car('Ford', 'Focus', 40)

# myCar.startCar()

class ElectricCar(Car):
    # init this object
    def __init__(self, make, model, batteryLife):
        # call super class constructor
        super(ElectricCar,self).__init__(make,model, None)
        self.batteryLife = batteryLife
    # def startCar(self):
    #     print "%s goes vroom" % self.model

car1 = Car('Toyota','Camry', 35)
car2 = ElectricCar('Tesla', "S", '100kh')

print car1.model
print car2.model
print car2.mpg