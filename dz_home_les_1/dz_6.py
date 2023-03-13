flag = True
while flag:
    num = input('Введите шестизначный номер билета: ')
    size = len(num)    
    if num.isdigit() == True and size == 6:
        sum_left = int(num[0]) + int(num[1]) + int(num[2])
        sum_right = int(num[-1]) + int(num[-2]) + int(num[-3])
        
        if sum_left == sum_right:
            print('Поздравляю, у вас счасливый билетик!')
        else:
            print('Вам не повезло, билетик ваш не счасливый')
        flag = False 
    else:
        print('Введите корректное шестизначное число!')