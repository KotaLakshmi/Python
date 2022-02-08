def breakTest(a):
    for i in a:
        if i==5:
            break
        print(i,end=" ")
        # print("")
def continueTest(b):
    for i in b:
        if i==5:
            continue
        print(i,end=" ")
        # print("")

a=[2,3,4,6,5]
b=[1,3,42,5,6,7,8,9]
print("breaktest output")
breakTest(a)
print("\ncontinueTest output")
continueTest(b)