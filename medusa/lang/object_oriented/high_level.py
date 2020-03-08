
class Person():
    #对象固定属性
    # __slots__ = ("name", "_birth")
    bar = 12

    def __init__(self):
        self.name = "aa"
        self._birth = 1964

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, v):
        if self.birth > 2020:
            raise ValueError("hehe")
        self._birth = v

    @property
    def age(self):
        return 2020 - self._birth




person = Person()

print(person.age)
