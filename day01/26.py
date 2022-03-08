emp = (["zhangsan", 18000], ["lisi", 16000], ["wangwu", 2000], ["maliu", 15000])
# print(id(emp))
# emp[0][1] = 19000
# print(id(emp))

# 找出工资最高的人叫啥
emp2 = []
for i in emp:
    emp2.append(i[1])
emp2.index(max(emp2))



# for num in range(2, 1001):
#     for i in range(2, num):  # num=2直接跳过这个循环
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")


# list1 = []
# for i in range(2, 1001):
#     list1.append(i)
#
#
# for num in list1[::1]:
# # for num in range(2, 1001):
#     for j in range(2, num):
#         if num % j == 0:
#             list1.remove(num)
#             break
# print(list1)
