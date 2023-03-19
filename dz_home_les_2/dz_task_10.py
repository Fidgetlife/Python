import random

col_money = int(input('введите кол-во монеток: '))
random_money = list()
eagle = 0
tails = 0

for i in range(col_money):
    random_money.append(random.randint(0, 1))

print(random_money)

for i in range(col_money):
    if(random_money[i] == 0):
        tails += 1
    elif(random_money[i] == 1):
        eagle += 1

if(tails < eagle):
    if(tails % 10 == 1):
        print(f'Нужно перевернуть {tails} монетку')
    elif(tails % 10 == 2 or tails % 10 == 3 or tails % 10 == 4):
        print(f'Нужно перевернуть {tails} монетки')
    else:
        print(f'Нужно перевернуть {tails} монеток')
elif(tails > eagle):
    if(eagle % 10 == 1):
        print(f'Нужно перевернуть {eagle} монетку')
    elif(eagle % 10 == 2 or eagle % 10 == 3 or eagle % 10 == 4):
        print(f'Нужно перевернуть {eagle} монетки')
    else:
        print(f'Нужно перевернуть {eagle} монеток')
elif(tails == eagle):
    print('Ничего переворачивать не нужно')