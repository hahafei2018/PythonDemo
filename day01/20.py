# abc = "root:x:0:0:root:/root:/bin/bash"
# print(abc.split(":")[-1])
# print("root:x\n:0:0".splitlines())
# print(" ".join(['df', '-h']))

name_list = ["张三", "李四", "王五", "马六"]
# print(name_list)
# print(type(name_list))
# print(len(name_list))

# print(name_list[2])

# for i in name_list:
#     print(i)

# for index, i in enumerate(name_list):
#     print(index+1, i)

# print(name_list[0:3:2])
print(name_list[::-1])

# print(name_list[0:-1:-1])  # []
# print(name_list[-1:-4:-2])


name_list.reverse()
print(name_list)

