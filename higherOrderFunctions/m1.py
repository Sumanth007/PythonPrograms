def add(a,b):
    return a+b

l1 = [1,1,1,1]
l2 = [1,1,1,1]

# a = map(lambda x:(x+x)**(x+x),l1)
# print(list(a))

l = [1,2,3,4,5,6,7,8]
a = filter(lambda x:x%2 == 0,l)
print(list(a))

def fil(a):
    if a%2 == 0 and a%4==0:
        return a
a = filter(fil,l)
print(list(a))


def smartAdd(add):

    def sA(a,b):
        print(a+a+b*b)
    return sA

@smartAdd
def add(a,b):
    pass

add(2,2)


