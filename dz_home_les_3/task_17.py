import random

size =int(input('введите размер списка: '))
list_number = list()
for i in range(size): 
    list_number.append(random.randint(-4, 4))
print (list_number)
list_number_new = set(list_number)
size_list_new = len(list_number_new)
print(size_list_new)
