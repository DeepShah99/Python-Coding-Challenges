#classmethods are specific to class and not any particular instance
class Person():
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.addperson()
    
    @classmethod
    def numberofpeople(cls):
        return cls.number_of_people

    @classmethod
    def addperson(cls):
        cls.number_of_people += 1
    

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.numberofpeople())

