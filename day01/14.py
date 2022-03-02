import random
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1

# i = 1
# while i < 101:
#     print(i, end=" ")
#     i += 2

num = random.randint(1, 100)
while True:
    guess_num = int(input("请猜1-100内的一个整数："))
    if guess_num > num:
        print("大了")
    elif guess_num < num:
        print("小了")
    else:
        print("对了")
        break
print("恭喜")
