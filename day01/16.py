# he = 0
# for i in range(1, 101):
#     if i % 5 == 0 and i % 2 == 1:
#         he += i
# print(he)

# for line in range(1, 4):
#     for field in range(1, 4):
#         print("学习", end=" ")
#     print()


for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(j, i, j*i), end="\t")
        # print("%d*%d=%d" % (j, i, j*i), end=" ")
    print()

