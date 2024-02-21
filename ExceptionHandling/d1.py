import pathlib
import timeit

a = 10
b = 20



from random import choice,sample,randint
list = [1,2,3,4,5]

a = choice(list)
print(a)
b = sample(list,4)
print(b)
c = randint(10,20)
print(c)

d = "Hello , what , are , you , doing"
e = d.partition(',')
f = d.rpartition(',')
print(e)
print(f)