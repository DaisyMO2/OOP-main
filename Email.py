# Base class
class Person:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def reply(self):
        print(f"{self.name} from {self.school} replies: Thanks for your message.")

# Subclasses (inheritance + polymorphism)
class Boy(Person):
    def reply(self):
        print(f"{self.name} from {self.school} replies: Hi Quiin, nice to hear from you")

class OtherStudent1(Person):
    def reply(self):
        print(f"{self.name} from {self.school} replies: Hey Quiin, Am really glad to talk to you")

class OtherStudent2(Person):
    def reply(self):
        print(f"{self.name} from {self.school} replies: Hi love hope to hear from you soon")

# Objects
Quinn = Person("Quinn", "Spena high School")
mark = Boy("Mark", "Namilyango College")
tom = OtherStudent1("Tom", "Namilyango Secondary School")
leo = OtherStudent2("Leo", "Namilyango Secondary School")

# object interactions
print("Email Interactions:")
print(f"{quinn.name} from {quinn.school} sends an email to {mark.school}.")
mark.reply()

print(f"{quinn.name} mistakenly sends another email to {tom.school}.")
tom.reply()

print(f"{Quinn.name} sends the last email again to {leo.school}.")
leo.reply()