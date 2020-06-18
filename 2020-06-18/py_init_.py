
# Learning __init__ (initializer)


class People:


    def __init__(self, firstName, age, ):
        self.firstName = firstName
        self.age = age

    def displayPerson(self):
        print("Hello, my name is " + self.firstName + ", I am " +
              str(self.age) + " years old.")



person1 = People("John", 25)
person2 = People("Tim", 24)


print("Person 1 name:", person1.firstName)
print("Person 2 name:", person2.firstName + "\n")


person1.displayPerson()
person2.displayPerson()

#END