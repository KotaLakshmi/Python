class Student:
    def __init__(self,name,id,marks):
        self.name=name
        self.id=id
        self.marks=marks
    def myfun(self):
       print("my name is:{}".format(s2.name))
       print("my id is:{}".format(s2.id))
       print("my marks is:{}".format(s2.marks))
s1=Student("jhon","73","886")
s2=Student("ram","4N","910")
print("Student details1:")
print("name:",s1.name)
print("id:",s1.id)
print("marks:",s1.marks)
print("Student details2:")
print("name:",s2.name)
print("id:",s2.id)
print("marks:",s2.marks)
s2.myfun()