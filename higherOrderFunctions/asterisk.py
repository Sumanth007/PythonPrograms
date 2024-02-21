l = [1,23,4,1,515]
l = tuple(l)
print(l)
t = 1,2,3,4
print(t)
def a(*l):
    for i in l:
        print(i)

a(t)