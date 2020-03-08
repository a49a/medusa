def foo():
    pass


def decorator(func):
    return func


# 手动装饰
foo = decorator(foo)


# 自动装饰
@decorator
def bar():
    pass
