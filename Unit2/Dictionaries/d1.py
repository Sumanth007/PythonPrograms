dict = {'name':'Sam','age':21,"courses":['CS']}
print(dict)
dict.update({'native':'sirsi'})
print(dict)
print(dict.pop('native'))
print(dict.keys())
print(dict.values())
print(dict.items())

dict['native'] = 'sirsi'
print(dict)

for k,v in dict.items():
    print(k ,'->', v)
