import csv
with open("n1.csv","r+") as f:
    cr = csv.reader(f,delimiter=",")
    for i in cr:
        print(i[0],"|",i[1],"|",i[2])
        break
    for j in cr:
        print(j[0],"->",j[1],"->",j[2])

    list = ["A","B","C"]
    list1 = [[1,2,3],[1,2,3],[1,2,3]]
    cw = csv.writer(f,delimiter=",")
    cw.writerow(list)
    cw.writerows(list1)