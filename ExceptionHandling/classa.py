class a():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def add(self):
        print("HEY")

class b(a):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        print(name,age)
        self.salary = salary
        self.id = id

    def add(self):
        print("Hell0")
class c(b):
    def __init__(self,name,age,id,salary):
        a.__init__(self,name,age)
        b.__init__(self,name,age,id,salary)

    def add(self):
        a.add(self)

bb = c("Sumanth",21,1,10483310)
bb.add()
print("Ended Here")
