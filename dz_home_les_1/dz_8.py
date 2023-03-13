flag = True
size_n = None
size_m = None
size_k = None
while flag:
    size_n = input('Введите кол-во долек по вертикали: ')
    if size_n.isdigit() == True:
        flag = False
flag = True        
while flag:
    size_m = input('Введите кол-во долек по горизонтали: ')
    if size_m.isdigit() == True:
        flag = False
flag = True
while flag:
    size_k = input('Введите кол-во долек, которые хотите отломить: ')
    if size_k.isdigit() == True:
        flag = False

if (size >= int(size_k)):
    if (int(size_k) % int(size_n) == 0 and size_k <= size_n) or (int(size_k) % int(size_m) == 0 and size_k <= size_m):
        print('Да, можно отломить')    
    else:
        print('Нет')
else:
    print('В шоколадке нет такого кол-ва долек')        

