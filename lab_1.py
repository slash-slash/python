import random as rm
import math

# ********************************** TASK 1 **************************************
# ******************************** вариант 2 *************************************
# определить имеется ли среди a b c хотя бы одна пара равных между собой чисел (2)

a = 1
b = 2
c = 2
def hast_duplicates(a, b, c):
    return len({a, b, c}) != len([a, b, c]) # {} is shortcut for set()

print(f"{ hast_duplicates(a, b, c) }")

# ******************************** вариант 5 *************************************
# определить имеется ли  среди трех чисел А Б С и Д хотя бы одно нечетное

a = 6
b = 2
c = 1
d = 4
def filterFn(x):
    return x % 2 != 0

def hast_odd(a, b, c, d):
    return True if (len(list(filter(filterFn, [a, b, c, d])))) else False

print(f"{ hast_odd(a, b, c, d) }")

# ********************************** TASK 1 **************************************
# ******************************** вариант 2 *************************************
# торговая фирма в первый день работы реализовала товаров на P тыс руб, а затем
# ежедневно увеличивала выручку на 3%. Какой будет выручка фирмы в тот день, когда
# она впервые превысит заданное значение Q? Сколько дней придется торговать фирме для достижения этого рез-та?
def getRevenue(initialValue, interest, periods):
    return initialValue * (1 + interest / 100) ** periods

def getRevenueResults(initialValue, target):
    days = 0
    interest = 3
    result = initialValue
    while (result <= target):
        result = getRevenue(result, interest, days)
        days += 1
    return { 'days': days, 'result': result }

results = getRevenueResults(100, 102)

print(f"days: {results['days']}, result: {results['result']}")

# сформировать одномерный список целых чисел А, используя генератор случайных чисел (диапазон от 0 до 99)
# Размер списка n ввести с клавиатуры.
def generateRandomList():
    length = int(input())
    return [rm.randint(0, 99) for i in range(length)]

# ********************************** TASK 3 **************************************
# ******************************** вариант 2 *************************************
# Все четные по значению элементы исходного списка А поместить в новый список В
def printRandomEven():
    mylist = generateRandomList()
    evenList = list(filter(lambda x: x % 2 == 0, mylist))
    print(f"{ evenList }")

printRandomEven()

# ******************************** вариант 16 ************************************
# найти номера минимального и максимального элементов первой половины списка
def getFirstPart(arr):
    return arr[:math.ceil(len(arr) / 2)]

def findExtremums():
    mylist = getFirstPart(generateRandomList())
    print(f"{mylist}")
    return { 'minIndex': mylist.index(min(mylist)), 'maxIndex': mylist.index(max(mylist)) } if len(mylist) else { 'minIndex': 'unknown', 'maxIndex': 'unknown' }

extremums = findExtremums()

print(f"minIndex: {extremums['minIndex']}, maxIndex: {extremums['maxIndex']}")