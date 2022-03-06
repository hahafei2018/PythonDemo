emp2 = (["zhangsan", 18000], ["lisi", 16000], ["wangwu", 2000], ["maliu", 15000])
print(id(emp2))
emp2[0][1] = 19000
print(id(emp2))

