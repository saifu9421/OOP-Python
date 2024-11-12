class Dog:
     def __init__(self):
         self.name =""
         self.color = ""
    
     def inpu(self):
          self.name = input("Dog name = ")
          self.color = input("Dog Color = ")
          
     def updateColor(self):
      self.color = input("dog color = ")
        
     def output(self):
        print(self.name,self.color)
        print(self.__dict__)
        print(dir(self))
    
# ============================================#
dog1 = Dog()
dog1.inpu()
dog1.output()
dog1.updateColor()
dog1.output()
