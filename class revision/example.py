class student:
    def __init__(self,name):
        self.name = name             #public
        self._gpa = 3.5               #protected(has one underscore)
        self.__password = "1234"       #private(has 2 underscores)
        
student_one =  student("daisy")

print(student_one.name)
print(student_one._gpa)
        