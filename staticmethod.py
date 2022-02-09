# from datetime import date
#
# class Person:
#     #instance method
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # a class method to create a Person object by birth year. cls is used for a class method
#     #We generally use class method to create factory methods.
#     # Factory methods return class objects ( similar to a constructor ) for different use cases.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     # a static method to check if a Person is adult or not.
#     #We generally use static methods to create utility functions.
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
#
# person1 = Person('JOHN', 21)
# person2 = Person.fromBirthYear('TOM', 1996)
#
# print(person1.age)
# print(person2.age)
#
# # print the result
# print(Person.isAdult(22))
#
from datetime import date
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromBirthDate(cls,name,year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('JOHN', 21)
person2 = Person.fromBirthDate('TOM', 1996)
print(person1.age)
print(person2.age)
print(Person.isAdult(22))