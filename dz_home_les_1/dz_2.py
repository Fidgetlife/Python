flag = True
while flag:
    num = input('введите трехзначное число: ')
    size = len(str(num))    

    if num.isdigit() != True or size != 3:
        
        print('Делайте ввод корректно!')
    else:
        flag = False

sum = int(num[0]) + int(num[1]) + int(num[2])
print('сумма цифр этого числа = ', sum)


