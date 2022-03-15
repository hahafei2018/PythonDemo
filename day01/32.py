f = open("D:/黑马课程/Python运维开发/PythonDemo/1.txt")
# data1 = f.read()
# f.seek(10)
# print(f.tell())
# f.seek(3)
# print(f.tell())
# for i in range(3):
#     f.readline()
# print(f.tell())
# data2 = f.read()

data = f.readlines()
print(data[1].strip())
f.close()
# print(data1)
# print("*"*20)
# print(data2)







