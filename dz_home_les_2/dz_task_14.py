number = int(input("введите число: "))
a = 2
counter = 1
list_degree = list()

while(a <= number):
    a *= 2
    counter += 1

for i in range(counter):
   list_degree.append(i)

print(list_degree)