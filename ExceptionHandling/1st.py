class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class empoyee():
    def __init__(self,id,salary):
        self.id = id
        self.salary = salary

class manager(empoyee,person):
    def __init__(self,name,age,id,salary):
        person.__init__(self,name,age)
        empoyee.__init__(self,id,salary)

    def __str__(self):
        return f"{self.name} {self.age} {self.id} {self.salary}"

    def display(self):
        print(vars(self))


m1 = manager("Sam",21,1,10000000)
m1.display()
print(m1.__str__())
print(m1)

a = {1,23,4213410,2}
a[1] = 0
print(a)