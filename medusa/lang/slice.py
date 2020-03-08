a = [1, 2, 3, 4, 5, 6]
# 从队尾开始
print(a[::-2])

# 尽量避免同时使用start、end、stride, a[2:2:-2]
# 如果使用可以分步
x = a[::2]
print(x[1:-1])

# 使用 itertoolsde islice
# TODO 例子