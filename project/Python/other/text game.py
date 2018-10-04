import random
secret = random.randint(0,10)
print('-------------------大家好我是老长-------------------')
temp = input("猜一个心里想一个数字：")
guess = int(temp)
i = 1
while guess != secret and i < 3:
    i += 1
    if guess > secret:
        print("大了")
    else:
        print("小了")
    temp = input("重新输入：")
    guess = int(temp)
if guess == secret:
    print("猜对了也没有奖励")
else:
    print("超过" + str(i) + "次,game over")
