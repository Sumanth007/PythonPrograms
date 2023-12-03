def outer(n):
    print(n)
    def inner():
        print(n-1)
    return inner

closure = outer(10)
closure()