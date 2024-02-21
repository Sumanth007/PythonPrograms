import json

with open("1st.txt","r+") as f:
    strr = '{"NICE":1,"GOOD":2}'
    a = json.load(f)
    b = json.loads(strr)
    print(a)
    print(b)
    # str1 = json.dumps(b)
    # print(str1)
    # json.dump(strr,f)
    f.seek(0)
    b = json.load(f)
    print(b)

