name_list = ["zhangsan", "lisi", "wangwu", "maliu"]
salary = [18000, 16000, 20000, 15000]

# 请查找lisi的工资
# print(salary[name_list.index("lisi")])

# 请查找工资最高的人叫啥
# 先找最高工资是多少
# 再找最高工资的下标
# 找下标对应在name_list里的元素
print(name_list[salary.index(max(salary))])



