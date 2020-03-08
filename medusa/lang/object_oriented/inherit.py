class Base:
    def __init__(self, name):
        self.name = name


class Foo(Base):
    def __init__(self, name, time):
        Base.__init__(self, name)
        self.time = time


class BaseA:
    def __init__(self):
        print("BaseA")


class FooA(BaseA):
    def __init__(self):
        BaseA.__init__(self)
        super().__init__()
    pass


foo = FooA()
