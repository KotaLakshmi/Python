import abc
class Main(abc.ABC):
    @abc.abstractmethod
    def A(self):
        pass
class B(Main):
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def A(self):
        print(self.a*self.b)
r=B(10,20)
r.A()