left_list = [1, 2]
right_list = [3, 4]

# 改变原列表
left_list.extend(right_list)
print(left_list)

# 不改变
merged_list = left_list + right_list

# 列表推导、列表表达式，别用map、filter
# 列表表达式内避免超过两个