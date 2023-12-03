def outer(start):
    print("hello")
    def inner(sept = 1):
        nonlocal start
        start += sept
        print(start)
    return inner


my_in = outer(5)
my_in(-2)
my_in(2)
my_in(2)
my_in(2)