l = list(range(1,15))
l[::2] = [111] * len(l[::2])
print(l)

