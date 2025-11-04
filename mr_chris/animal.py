class Animal:
    def speak(self):
        print("animal is talking")

class Dog(Animal):
    def wroof(self):
        print("dog is barking")

class Cat(Animal):
    def meow(self):
        print("cat is meowing")

animal = Animal()
animal.speak()

Animals = [Dog(), Cat()]       
for a in Animals:
    a.speak()


