class Student:
    def greet(self):
        print("hi i am a student")
        
class ClassRep(Student):
    def greet(self):
        print("hi am the classRep")

class GuildPresident(Student):
    def greet(self):
        print("hi am the guild president of our university") 
        
people = [Student(), ClassRep(), GuildPresident()]


   