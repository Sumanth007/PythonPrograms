set1 = set(range(1,15))

set2 = {x for x in set1 if x<11 if x%2 == 0 }

set2.add(12)
set2.pop()
print(set2)
list1 = list(set2)
list1.sort(reverse=True)
print(list1)
set2 = set(list1)
print(set2)
set2.add(9)
print(set2)