# ____________3 types of methods in Python:____________
# 1) Methods of class's atributtes. str.upper() for example. Editing concrete value in the "stroke" class
# 2) Class methods. Dict.from keys(). This type of methods cant achieve concrete attribure, but can greatly change the condition of class. All parts are changed.
# 3) Static methods. Cannot anything like 'others'

class Person:
    def __init__(self, name, age):            # 1 type
        self.name = name
        self.age = age

    @classmethod                              # 2 type
    def square (cls, name, number):
        return cls(name, number * number)

    @staticmethod                             # 3 type
    def is_adult(age):
        return age > 18

person1 = Person('Slava', 5)
person2 = Person.square ('Stepa', 6)

print(person1.name, person1.age)
print(person2.name, person2.age)
print(Person.is_adult(15))




