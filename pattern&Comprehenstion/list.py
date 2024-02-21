from random import sample,shuffle
l = [1,32,34,12515,12]
a = sample(l,2)
print(a)

b = "Hello world"
l1 = b.split()
print(l1)

x = [0,1,2,3,4,5,6,7,8,9]

x[1::2] = [0] *len(x[1::2])
print(x)
x = "Hello \"nice\""
print(x)

l1 = [1,2,3,4,5,1,2,3,4,5,1]
print(l1.index(1))

a = len("sajdlajf")
print(a)

import random
l = [1,23,41,5,15,15]

a = "Hello how are you,what are you doint"
b = a.split()
print(b)
c = ' and '.join(b)
print(c)
random.shuffle(l)
print(l)

print("hi",end="")
print("Nice")