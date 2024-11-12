class Student:
    def __init__(self):
        self.name =  " "
        self.id = 0
        # print("Hello")
    
    def inpu(self):
        self.name = input("Your name = ")
        self.id = int(input("your id = "))
            
        
    def output(self):
        print("name=",self.name,"id=",self.id)
        # print(self.id)

        

#========================================================#
#variavle = class_name()
s1 = Student()
s2 = Student()
s3 = Student()


s1.inpu()
s2.inpu()
s3.inpu()
# s2.id = 2
# s2.name = "saifur rahman saif"
# print(s1.name,s1.id)
# print(s2.name,s2.id)
s1.output()
s2.output()
s3.output()