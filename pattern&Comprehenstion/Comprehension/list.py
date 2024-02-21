list1 = list(range(1,15))
# print(list1)
list2 = [i*i for i in list1 if i%2 == 0 if 4%2 == 0]
list3 = {i for i in list1 for j in list1 if i % (2*j) == 0}
# print(list2)
# print(list3)
list4 = [i if i%2 ==0 else "invalid" for i in range(20)]
print(list4)
a = {}
print(type(a))