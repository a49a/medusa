


def foo(a, b, *, bar=True):
    print(bar)


# 直接调用报错
foo(1, 2, 3)

