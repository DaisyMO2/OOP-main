class Animal:
    def speak(self):
        print("animal is talking")
        
class Dog(Animal):
    def wroof(self):
        print("dog is barking")
        
class cat(Animal):
    def meow(self):
        print("move bitch")
        
animal = Animal()
animal.speak()
animal2 = Dog()
animal3 = cat()
Animals = [Dog(), cat()]       
for a in Animals:
    a.speak()

