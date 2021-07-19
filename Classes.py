
# _____________Incapsulation___________

# creating class with private attributes and annotations

class Human:
    def __init__(self, name, age):
        self.__name = name      # Using constructors and __private__ attributes
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):     # Writing setter and getters functions
        if age in range(1,100):
            self.__age = age
        else:
            print('Недопустимый возраст')
    @property                   #Using annotations for a better quality of code
    def name(self):
        return self.__name

    def display_info (self):
        print('Имя:', self.__name, '\nВозраст:', self.__age)

# Slava = Human('Slava', 45)
# Slava.display_info()
# # Slava.set_age(500)            Can't call it with annotations
# Slava.age                   # Won't print nothing, because it return methods. After involving annotation there is no need in parenthesis
# Slava.name
# Slava.age = 57              # Won't work, because it __private. But it'll with annotations
# # Slava.set_age(46)             # Won't work with annotation
# Slava.display_info()            # Getting a new value

# ____________________Inheritance_________

# Creating subclass. Human is parent class, employee is derived|child class.

class Employee(Human):

    def originating(self, company):
        print(self.name, 'is working in', company) # self,__name is private. Whereby it won't allow us changing smth

# Andrey = Employee('Andrey',21)
# Andrey.display_info()
# Andrey.originating('Factory')
# Andrey.age = 22
# Andrey.display_info()

# _____________Polymorphism ____________

class Pupil(Human):
    def __init__(self, name, age, univercity):
        Human.__init__(self, name, age)       # Importing attributes from parent
        self.univercity = univercity

    def display_info (self):            # On the scale with number of strokes is a tag
        print('Имя:', self.name, '\nВозраст:', self.age, '\nМесто учебы:', self.univercity)

pupil = Pupil('Vasya', 40, 'MGTU')
pupil.display_info()

print(isinstance(pupil, Human)) # Cheking the affilation and link beetwen child and parent object




