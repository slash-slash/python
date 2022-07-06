import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

#Задача на рекурсию
#Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.
def find_squares(x, y, counter = 0):
    max_value = max(x, y)
    min_value = min(x, y)

    if x <= 0 or y <= 0:
        print(f"number of squares is {counter}")
        return
    else:
        print(f"side size {min_value}")
        return find_squares(max_value - min_value, min_value, counter + 1)

find_squares(int(input('Input 1st side size')), int(input('Input 2nd side size')))

def InsertSort(A):
    for i in range(len(A)):
        t = A[i]
        j = i
        for j in range(j, 0, -1):
            if A[j - 1] > t:
                A[j] = A[j-1]
                j -= 1
            else:
                break
        A[j] = t

# compare InsertSort to BubbleSort
def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время insert"])
x=[]
y1=[]
y2=[]


for N in range(1000,5001,1000):
    x.append(N)
    minV=1
    maxV=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(maxV-minV)+minV)))

    print(A)

    B = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)


    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    InsertSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Insert   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()
