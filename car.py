class Car:
    def __init__(self):
        self.name = " "
        self.model = " "
        self.caka = 4
    
    def inpu(self):
        self.name = input("your car name = ")
        self.model = input("your car model = ")
        # self.caka = int(input("caka koita = "))
    
    def output(self):
        print("car name = ",self.name, "car model = " ,self.model,"car caka = ",self.caka)
        
    
# ====================================#
car1 = Car()
car2 = Car()
car3 = Car()

car1.inpu()
car2.inpu()
# car3.inpu()

car1.output()
car2.output()
car3.output()