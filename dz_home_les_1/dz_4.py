flag = True
col_all = 0
while flag:
    col_all = input('Введите кол-во журавликов, которые сделали Петя, Катя и Сережа: ')
    if col_all.isdigit() == True:
        if int(col_all) % 6 == 0:
            pet = int(col_all) / 6
            ser = pet
            kat = 4 * pet
            print('Петя сделал: {} журавлика, Катя сделала: {} журавликов, Сережа сделал: {} журавликов'.format(pet, kat, ser))
        else:
            print('Кол-во изделий должно быть кратно 6 :), тогда получаются целочисленные занчения, иначе =>')
            pet = float(col_all) / 6
            ser = pet
            kat = 4 * pet
            print('Петя сделал: {} журавлика, Катя сделала: {} журавликов, Сережа сделал: {} журавликов'.format(pet, kat, ser))
        flag = False
    else:
        print('ВВедите корректное целочисленное значение, желательно кратное 6 ;)')
