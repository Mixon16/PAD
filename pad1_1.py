class Animal():
    def __init__(self, genus, gender = "Female"):
        self.isAlive = True
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        if self.gender == "Female" and partner.gender == "Male" and self.genus == partner.genus:
            new = Animal(genus = self.genus)
        try:
            new.gender
            return new
        except UnboundLocalError:
            print('attribute not found')

class Dog(Animal):
    def woof(self):
        return "woof woof"
    
class Cat(Animal):
    def purr(self):
        return "purr"


d = Dog(genus = 'a', gender= 'Female')
c = Cat(genus = 'b')
c2 = Cat(genus = 'b', gender='Male')

new = c.breed(c2)
new.genus
from datetime import datetime