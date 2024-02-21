def outer():
    a = 10
    def inner():
        nonlocal a
        a = 5
        print(a)
    inner()
    print(a)

outer()