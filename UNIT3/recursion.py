#sum of numbers using recursion
"""l = []
def summ(n):
    if n == 0:
        return
    else:
        dig = n % 10
        l.append(dig)
        summ(n//10)

n = int(input("Enter the number"))
summ(n)
print(sum(l))
"""

"""#gcd of two numbers using euclids algorithm
def gcd(a,b):
    if b != 0:
        return (gcd(b, a % b))
    else:
        return a

print(gcd(150,100))
"""

#gcd of two numbers using Dijistras algorithm
def gcd(a,b):
    if b > a:
        return gcd(b-a,a)
    elif b < a:
        return gcd(a-b,a)
    if a == b:
        return a

a = gcd(150,200)
print(a)