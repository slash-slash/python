from random import randrange
from functools import reduce

#Задание 1
#Вариант 1

#Удалить в списке все числа, которые повторяются более двух раз.
def filter_fn(numbers):
    def check_entries(number):
        return numbers.count(number) <= 2
    return filter(check_entries, numbers)

print(list(filter_fn([1, 2, 3, 2, 3, 2])))


#Найти подмножество данного множества чисел такое,
#что сумма его элементов равна заданному числу.
def get_subset_by_sum(num_list, num_sum):
    def get_all_subsets():
        current_subsets = [[]]
        for current_number in num_list:
            current_subsets += [current_subset + [current_number] for current_subset in current_subsets]
        return current_subsets

    all_subsets = get_all_subsets()
    for subset in all_subsets:
        if sum(subset) == num_sum:
            return subset
        else:
            return []

print(list(get_subset_by_sum([1, 2, 3, 4], 100)))

#Вариант 2
#Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
num_list = []
n = int(input('Please enter number of elements in the list'))

for i in range(n):
    num_list.append(int(input('Please enter the number')))

print(max(list(filter(lambda num: num % 2 != 0, num_list)), default="Max odd el isn't found"))

#Найдите минимальный по модулю элемент списка.
print(min(list(map(lambda num: abs(num), num_list)), default="Min abs el isn't found"))

#Задание 2
#Вариант 1
#В матрице найти номер строки, сумма чисел в которой максимальна.

def find_max_sum_column(matrix):
    if len(matrix) == 0:
        return "Matrix is not set"

    return reduce(lambda prev, curr: {'sum': sum(curr[1]), 'row': curr[0]} if (sum(curr[1]) > prev['sum']) else prev, enumerate(matrix), {'sum': sum(matrix[0]), 'row': 0})['row']


m = int(input('Please enter number of columns and rows in the matrix'))

matrix2D = [[randrange(0, 10) for i in range(m)] for i in range(m)]
print(matrix2D)
print(find_max_sum_column(matrix2D))

