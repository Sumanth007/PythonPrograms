with open("sam.txt","a+") as f:

    f.seek(0)
    a = f.readlines()
    for i in a:
        print(i)

    a = f.closed
    print(a)
    a= f.readable()
    print(a)
    print(f.mode)
    print(f.name)




l = [1,2,34,5]

def add(*l):
    print(l)

add([1,2,34,5],[2])


def itt():
    n = 1
    while True:
        yield n
        n += 1

g = itt()

print(g.__next__())
print(next(g))

l = [1,2,3,4,5]
li = iter(l)
print(next(li))
print(next(li))


def smartAdd(add):
    print("smartAdd is initiated")
    def sA(a,b):
        add(a+a,b+b)
    return sA

@smartAdd
def add(a,b):
    print(a+b)

add(20,20)

