# 报错引发IO异常就不走 finally了
handle = open("xxx.txt")
try:
    data = handle.read()
finally:
    handle.close()

# else 减少try代码行数
