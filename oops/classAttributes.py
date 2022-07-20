#classmethods are specific to class and not any particular instance
class Person():
    number_of_people = 8

    def __init__(self, name):
        self.name = name


p1 = Person("Tim")
p2 = Person("Jill")

print(Person.number_of_people)
print(p1.number_of_people)
Person.number_of_people = 4
print(p2.number_of_people)
print(Person.number_of_people)
