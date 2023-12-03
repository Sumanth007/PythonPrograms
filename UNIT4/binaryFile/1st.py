import pickle

with open("binary.dat","wb+") as f:
    a = "Hello How Are you"
    c = "Nice day"
    d = "See ya"
    pickle.dump(a,f)
    pickle.dump(c,f)
    pickle.dump(d,f)
    f.seek(0)
    b = pickle.load(f)
    bb = pickle.load(f)
    bbb = pickle.load(f)

    print(b)
    print(bb)
    print(bbb)

    q = f.read()
    print(q)

    t = '{"Name":1}'
    f.write(t)