import array as arr
# interger type array
a=arr.array('i',[1, 2, 3,4,5,6])
print("the new array is created:")
for i in range(0,6):
    print(a[i],end="")
# float type array
b=arr.array('d',[2.2,3.4,5.6,1.5])
print("the array is:")
for i in range(0,4):
print(b[i],end=" ")

#insert an element in array
s1=arr.array('i',[1,2,3,4])
print("before insertion")
for i in range(0,4):
    print(s1[i],end=" ")
print("after insertion")
s1.insert(5,5)
for i in range(0,5):
    print(s1[i],end="")

#remove an element in array
p=arr.array('d',[1.2,3.4,3.6,4.4,8.4])
print("the array is created:")
p.pop(2)
for i in range(0,4):
    print(p[i],end="")
p.remove(3.6)

# append the element
a=arr.array('i',[1,2,3,4,5])
print("the append array is created:")
for i in range(0,5):
    print(a[i],end=" ")
a.append(7)
print(a)
for i in range(0,6):
    print(a[i],end=" ")
# character array
b=arr.array('u',['l','a','k','s','h','m','i'])
print("the character array is")
for i in range(0,7):
    print(b[i],end=" ")