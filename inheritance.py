class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print("I am " + self.name + " and I am " + str(self.age) + " years old")

    def speak(self):
        print("I do not know what to say")

class Dog(Pet): 
    def __init__(self, name, age, colour): 
        #calling the parent class Pet and passing name, age 
        super().__init__(name, age) #U need to do this because there might be some operations on arguments in the parent class
        self.colour = colour

    def show(self):
        print("I am " + self.name + " and I am " + str(self.age) + " years old of colour " + self.colour)


    def speak(self):              
        print("Bark")

class Cat(Pet):
    def speak(self):
        print("Meow")
class Fish(Pet):
    pass

p = Pet("Tim", 10)
p.speak()
d = Dog("Tom", 9, "Brown")            
d.show()
c = Cat("Jill",11)
c.speak()
f = Fish("Bubbles",1)
f.speak()
