def inner(n):
    while n < 10:
        yield n
        n += 1

n = 1
a = inner(n)
print(a.__next__())
print(a.__next__())
print(next(a))
print(next(a))

list1 = list(range(1,5))

a = iter(list1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
