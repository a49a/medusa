from enum import Enum, unique

@unique
class Person(Enum):
    # 易感者
    Susceptible = 0
    # 暴露者
    Exposed = 1
    # 染病者
    Infectious = 2
    # 康复者
    Recovered = 3

print(Person.Exposed)