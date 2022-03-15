f = open("D:/黑马课程/Python运维开发/PythonDemo/1.txt", mode="r")
# for index, i in enumerate(f):
#     if 3 >= index >= 1:
#         print(i.strip())

for i in f:
    if i.startswith("daemon"):
        print(i.strip())
f.close()
