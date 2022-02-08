class Addition:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def calculate(self):
        self.answer=self.first+self.second
    def display(self):
        print("first number:"+str(self.first))
        print("second number:" + str(self.second))
        print("addition of two numbers:"+str(self.answer))
obj=Addition(20,30)
obj.calculate()
obj.display()