name = input("输入你的名字: ")
sex = input("输入你的性别: ")
age = input("输入你的年龄: ")
# if sex == "男" and age >= 18:
#     print("{}，sir".format(name))
# elif sex == "男" and age < 18:
#     print("{}，boy".format(name))
# elif sex == "女" and age >= 18:
#     print("{}，lady".format(name))
# elif sex == "女" and age < 18:
#     print("{}，girl".format(name))
# else:
#     print("输入有误")


if not age.isdigit():  # 判断是否为纯数字
    print("输入的年龄不是数字")
    exit()  # 退出整个程序
else:
    age = int(age)

if sex == "男":
    if age >= 18:
        print("{}，sir".format(name))
    else:
        print("{}，boy".format(name))
elif sex == "女":
    if age >= 18:
        print("{}，lady".format(name))
    else:
        print("{}，girl".format(name))
else:
    print("输入有误")
