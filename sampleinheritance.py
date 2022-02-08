

# single inheritance
# class Parent:
#     def func1(self):
#         print("this is function in parent class")
# class Child(Parent):
#     def func2(self):
#         print("this function is child class")
# obj=Child()
# obj.func1()
# obj.func2()

# multiple inheritance
# class Parent:
#     def func1(self,name):
#         self.name=name
#         print(self.name)
#         print("this is function in parent class")
# class Child:
#     def func2(self,id):
#         self.id=id
#         print(self.id)
#         print("this function is child class")
# class Subchild(Parent,Child):
#     def func3(self,name,id):
#         self.name=name
#         self.id=id
#         print(self.name)
#         print(self.id)
#         print("this function is subchild class")
# obj=Subchild()
# obj.func1("prasanna")
# obj.func2(439)
# obj.func3("prasanna",439)

# multilevel inheritance
# class College(object):
#     def __inti__(self,cname):
#         self.cname=cname
# class Student(College):
#     def __inti__(self,name,cname):
#         self.name=name
#         College.__init__(self,cname)
# class Department(Student):
#     def __inti__(self,depname,name,cname):
#         self.depname=depname
#         Student.__init__(self,name,cname)
#     def print_names(self):
#         print("Collegename:",self.cname)
#         print("studentename:", self.name)
#         print("departmentname:", self.depname)
# obj=Department('vec','ram','ECE')
# obj.print_names

# Hierarchical inheritance
# class Parent:
#     def func1(self):
#         print("this function is parent class ")
# class Child1(Parent):
#     def func2(self):
#         print("this function is child1 class ")
# class Child2(Parent):
#     def func3(self):
#         print("this function is child2 class ")
# obj1=Child1()
# obj2=Child2()
# obj1.func1()
# obj1.func2()
# obj2.func1()
# obj2.func3()

# hybrid inheritance
class Parent:
    def func1(self):
        print("this function is parent class ")
class Child1(Parent):
    def func2(self):
        print("this function is child1 class ")
class Child2(Parent):
    def func3(self):
        print("this function is child2 class ")
class Child3(Child1,Parent):
    def func4(self):
        print("this function is in child3")
obj=Child3()
obj.func1()
obj.func2()