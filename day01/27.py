dict1 = {
    "stu01": "张三",
    "stu02": "李四",
    "stu03": "王五",
    "stu04": "马六"
}
# print(type(dict1))
# print(len(dict1))
# print(dict1)

# 查
# print(dict1["stu01"])
# # 增
# dict1["stu05"] = "田七"
# # 删
# dict1.pop("stu02")
# # 改
# dict1["stu01"] = "张三丰"
#
# print(dict1)

# 查找学号为stu03的人名
for i in dict1.items():
    if i[0] == "stu03":
        print(i[1])






