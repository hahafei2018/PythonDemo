name = input("输入你的名字: ")
age = int(input("输入你的年龄: "))


print(type(name))
print(type(age))
# print(name, "你"+str(int(age)+5)+"岁了")

# print(name+"，你"+age+"岁了")

# print("%s，你5年后%d岁了" % (name, age+5))

print("{}，你5年后{}岁了".format(name, age+5))
