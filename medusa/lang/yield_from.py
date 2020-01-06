
def foo():
    martix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    for x in martix:
        yield from x


i = foo()

for x in i:
    print(x)