set1 = {1, 2, 3, 2, 4, 4, 5}
set2 = {3, 4, 6, 7, 8}
# 交集
print(set1.intersection(set2))
# 并集
print(set1.union(set2))
# 补集
print(set1.difference(set2))
print(set2.difference(set1))

# 对称补集
print(set1.symmetric_difference(set2))
