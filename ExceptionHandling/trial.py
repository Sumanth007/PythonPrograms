def gen():
    x,y = 0,1
    while True:
        yield y
        x,y = y,x+y

it = gen()

print(it.__next__(),end=", ")
print(it.__next__(),end=", ")
print(it.__next__(),end=", ")
print(it.__next__(),end=", ")
print(it.__next__(),end=", ")
print(it.__next__(),end=", ")
print(it.__next__(),end=", ")
print(it.__next__(),end=", ")
print(it.__next__(),end=", ")
print(it.__next__())

list1 = ["Hello"," World!"]

mlist1 = ''.join(list1)
print(mlist1)

def gen(n):
    while n > 0:
        n -= 1
        yield n

strr = "hello"
n = len(strr)
a = n
it = gen(n)
for i in range(a):
    print(strr[it.__next__()],end="")