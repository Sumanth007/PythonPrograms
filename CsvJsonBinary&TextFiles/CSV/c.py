import csv
f = open("name.csv","a+")
row = csv.reader(f,delimiter="|")
for i in row:
    print(i[0])
wr = csv.writer(f,delimiter="|")
wr.writerows([['Sam',"XII","A"],['a','b','c']])
for i in row:
    print(i)

f.close()
