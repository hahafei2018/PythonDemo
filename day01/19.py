abc = "hello,nice to meet you"
# print(abc.upper().lower())
# print(len(abc))
# print(abc.ljust(50, "*"))


# print(" haha\n".strip())  # 删除字符串左边和右边的空格或换行（常用，处理文件的换行符很有用）
# print(" haha\n".lstrip())  # 删除字符串左边的空格或换行
# print(" haha\n".rstrip())  # 删除字符串右边的空格或换行

# print(abc.startswith("hello"))
# print(abc.endswith("yousdfsdf"))
#
# print(abc.count("o"))

# count = 0
# for i in abc:
#     if i == "o":
#         count += 1
# print(count)

# char = input("请输入字符：")
# if char.isdigit():
#     print("纯数字")
# elif char.isalpha():  # 全为字母
#     if char.isupper():
#         print("纯大写")
#     elif char.islower():
#         print("纯小写")
#     else:
#         print("大小写混合")
# else:
#     print("其它")

print(abc.replace("o", "=", 2))

