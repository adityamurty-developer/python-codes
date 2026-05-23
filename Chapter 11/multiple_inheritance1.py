class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def Eat(self):
        print("Dog Eat")

class Cow:
    def Walk(self):
        print("Cow walks")

class Cat(Dog, Cow):
    def rush(self):
        print("Cat runs")


c = Cat()
c.sound()
c.Eat()
c.Walk()