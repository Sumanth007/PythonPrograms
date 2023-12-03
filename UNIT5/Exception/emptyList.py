from functools import reduce

l = []

try:
    a =  reduce(lambda x,y:x+y,l)
except Exception as e:
    print("Error :",e)

else:
    print(a)

str = "aladsjfoiaisjkl"

a = sorted(str)
print(a)

print("hello how are you {a}{b}".format(a = 10,b =20))

for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(4,1,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()