dict = {n:(n*2 if n%2==0 else "Invalid") for n in range(6)}
print(dict)

list = [(1,'a'),(2,'b')]

dict = {k:v for k,v in list}
print(dict)

d1 = {"Sam":21,"Ronny":22,"Ajay":23,"Rox":20}

a = d1.pop('Sam')
print(a)

d1.popitem()
print(d1.keys(),d1.values())
# print(help(d1))
# d2 = {k.lower(): "Eligible" if v >=21 else "Next time" for k,v in d1.items()}
# print(d2)
#
# a = [1,2,3,4,5,6,7,8]
#
# b = [x**2 for x in a]
#
# b = {1,2,3,4,5}
# a = dict(**b)


d1 = {"Sam":21,"Ronny":22,"Ajay":23,"Rox":20}
def addd(**a):
    print(a.items())

addd(**d1)
def add(*a):
    print(a)

l = tuple(range(0,11))
add(*l)

a = (1,2,3,4,5)
b = ('a','b','c','d')

c = zip(a,b)
c = tuple(c)
print(c)

c = "hello"
print(c.zfill(20))

