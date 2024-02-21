dict  = {"name":"Sumanth","age":21,"course":"MCA"}

for k,v in dict.items():
    print(k , "  ->  ",v)


dict1 = {1:"Number",2:"Number",3:"Number",4:"Number"}

a = {K:"Even" if K%2 == 0 else "ODD" for K,V in dict1.items() }
print(a)

a = [1,2,3,4,5,6,7,8,9,10,11,12]

b = [x for x in a if x%2==0 if x%3 == 0 if x%4 == 0]
print(b)