name_list = ["张三", "李四", "王五", "马六"]

# print(name_list[::-1])
# print(name_list)

# print(id(name_list))
# name_list.reverse()
# print(id(name_list))

# 增加元素
name_list.append("田七")
print(name_list)
name_list.insert(2, "陈八")
print(name_list)

# 删除元素
name_list.remove("李四")
print(name_list)
name_list.pop(2)
print(name_list)

# del name_list[2]
# print(name_list)
# name_list.clear()
# print(name_list)

# 改（替换元素）
name_list[0] = "张三丰"
print(name_list)

# 查
print(name_list[0])

