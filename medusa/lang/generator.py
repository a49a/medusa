def reserve(data):
    for x in range(len(data)-1, -1, -1):
        yield data[x]


vec = list(reserve("golf"))
print(vec)


# 生成器表达式