class Employee():
    dept="ECE"
    def __init__(self,name,id):
        self.name=name
        self.id=id
emp1=Employee('prasanna','439')
emp2=Employee('lakshmi','435')
print(emp1.dept)
print(emp2.dept)
print(emp1.name)
print(emp1.id)
print(emp2.name)
print(emp2.id)
print(Employee.dept)
Employee.dept="CSE"
print(Employee.dept)

#
class Example:
    staticvar="true"

e=Example()
print(Example.staticvar)
instance=Example()
print(instance.staticvar)
instance.staticvar="false"
print(instance.staticvar)
print(Example.staticvar)