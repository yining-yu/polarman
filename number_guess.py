#developed by yu
num = input('猜一下我心里想的数字是：')
guess = int(num)
time = 1

if guess == 8:
    print('哇，一次就答对了！')

while guess != 8:
    while time == 1:
        print('由于您没有猜对，因此我们将给出相应提示')
        num = input('请重新输入：')
        guess = int(num)
        time += 1
    while time > 1 and time <= 3:
        if guess == 8:
            print('恭喜你，答对了！')
        else:
            if guess < 8:
                print('哎呀猜错了，小了小了')
                print(f'这是第{time}次回答，您还有{4-time}次机会')
                num = input('请再次输入：')
                guess = int(num)
            else:
                print('哎呀猜错了,大了大了！')
                print(f'这是第{time}次回答，您还有{4-time}次机会')
                num = input('请再次输入：')
                guess = int(num)
        time += 1
    else:
        print('次数用完了，谢谢您的参与')
        break
