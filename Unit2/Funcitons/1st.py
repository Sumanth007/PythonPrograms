def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
# For loop to reverse the string
for char in rev_str("hello"):
    print(char)


a = 10
print()
for i in range(a -1,-1,-1):
    print(a)
    a -= 1
