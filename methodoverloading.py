class Super():
    def add(self,a,b,c=20):
        if c>20:
            print("a+b+c={}".format(a+b+c))
        else:
            print("a+b={}".format(a + b))
obj=Super()
obj.add(10,20,40)
obj.add(10,20)