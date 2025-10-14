class Person:
    def __init__ (self, name):
        self.name = name
            
    def introduce(self):
        print("hello my name is", self.name)
        
        
        
        
class Student (Person):
    def __init__ (self, name, program, year):
        super().__init__(name)
        self.program = program
        self.year = year
        
    def introduce(self):
        return super().introduce() + f",my name is {self.name}", "i am studying {self.program} program"

class Lecturer (Person):
    def __init__ (self,name, department):
        super(). __init__ (name)
        self.department = department
        
     def mintroduce(self):
        return super().introduce() + f",my name is {self.name}", "i am working in the {self.department} department"
    
    

p = Person("Daisy")
s = Student("Leopold", "BSIT", 2)
l = Lecturer("Chris", "BSIT")

print(p.introduce())
print(s.introduce())
print(l.introduce())