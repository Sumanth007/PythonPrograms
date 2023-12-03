def gen(a,b):
    while a <= b:
        yield a
        a += 1

it = gen(5,10)
print(it.__next__())
print(it.__next__())
print(next(it))
print(next(it))
print(next(it))
print(next(it))