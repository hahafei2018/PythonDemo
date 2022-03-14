emp = (["zhangsan", 18000], ["lisi", 16000], ["wangwu", 20000], ["maliu", 15000])
# print(id(emp))
# emp[0][1] = 19000
# print(id(emp))

# 查找lisi的工资
# for i in emp:
#     if i[0] == "lisi":
#         print(i[1])


# 找出工资最高的人叫啥
# emp2 = []
# for i in emp:
#     emp2.append(i[1])
# print(emp[emp2.index(max(emp2))][0])

# num 2 3 4 5 6 7 8 9 ......
# for num in range(2, 1001):
#     for i in range(2, num):  # num=2直接跳过这个循环
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")
