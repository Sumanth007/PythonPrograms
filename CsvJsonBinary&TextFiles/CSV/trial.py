import json
a = {"Name":"Sumanth","Age":21}
b = {"Name":"Sumanth","Age":21}

with open("json1.json","w+") as f:
    json.dump(a,f)
    f.seek(0)
    d = json.load(f)
    print(d)
bb = json.dumps(b)
c = json.loads(bb)
print(bb)
print(c)