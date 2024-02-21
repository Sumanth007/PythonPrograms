class a():
    def __init__(self,Id):
        self.Id = Id
        print("calling init in a")
    def add(self):
        print("Adding")

class b(a):
    def __init__(self,name,age,Id):
        a.__init__(self,Id)
        # super().__init__(Id)
        self.name = name
        self.age = age

    def func(self):
        print("Calling func")
        super().add()

bb = b("Sumanth",21,1)
bb.func()