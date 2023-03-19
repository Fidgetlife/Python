import math

sum_numbers = int(input('введите сумму задуманных чисел: '))
multiplication_numbers = int(input('введите произведение этих задуманных чисел: '))

first_term = 1
second_term = sum_numbers - first_term

while(first_term * second_term != multiplication_numbers):
    first_term += 1
    second_term -= 1
    if(first_term == sum_numbers):
        break

if(second_term == 0):
    discriminant = sum_numbers*sum_numbers - 4 * multiplication_numbers

    fist_number = (sum_numbers - math.sqrt(discriminant)) / 2 
    print(fist_number)

    second_number = (sum_numbers + math.sqrt(discriminant)) / 2 
    print(second_number)

else:
    print(first_term)
    print(second_term)



