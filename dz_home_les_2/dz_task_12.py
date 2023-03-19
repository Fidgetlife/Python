import math

sum_numbers = int(input('введите сумму задуманных чисел: '))
multiplication_numbers = int(input('введите произведение этих задуманных чисел: '))

discriminant = sum_numbers*sum_numbers - 4 * multiplication_numbers

fist_number = (sum_numbers - math.sqrt(discriminant)) / 2 
print(fist_number)

second_number = (sum_numbers + math.sqrt(discriminant)) / 2 
print(second_number)