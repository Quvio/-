'''Лабораторная работа №5
Задана рекуррентная функция.
Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно
и итерационно(значение, время).
Определить (смоделировать) границы применимости рекурсивного
и итерационного подхода.
Результаты сравнительного исследования времени вычисления
представить в табличной и графической форме в виде отчета по лабораторной работе.
Вариант 18
F(1) = 1, F(n) = (-1)n*(F(n–1) /(2n)!-(2*n + 1)!), при n > 1
'''
import timeit
import matplotlib.pyplot as plt

def fact1(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact1(n - 1)

def fact2(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

k = -1
lastF = 1

def recF(n):
    global lastF, k
    if n == 1:
        return 1
    elif n > 1:
        k *= -1
        lastF = k * ((recF(n - 1) / fact1(2 * n)) - fact1(2*n + 1))
        return lastF

k = -1

def iterF(n):
    global k
    F = [0] * (n + 1)
    F[1] = 1
    if n== 1:
        return 1
    for i in range(1, n + 1, 2):
        k *= -1
        F[i] = k * ((F[n - 1] / fact2(2 * n)) - fact2(2 * n + 1))
        return F[i]

q = int(input("Ввeдите n"))

time1 = []
time2 = []
for n in range(1, q+1):
    timerec = timeit.timeit(lambda: recF(n), number=1)
    time1.append(timerec)
    timeiter = timeit.timeit(lambda: iterF(n), number=1)
    time2.append(timeiter)

recf = [recF(n) for n in range(1, q+1)]
intf = [iterF(n) for n in range(1, q+1)]
print('Таблица сравнения времени:')
print("| {:^7} | {:^15} | {:^15} |".format("n", "Рекурсия", "Интеракция"))
for i in range(1,q+1):
    print("| {:^7} | {:^14.6f} | {:^14.6f} |".format(i, time1[i-1], time2[i-1]))
plt.plot(range(q), time1,label='Рекурсия', color='green', marker='o', markersize=7)
plt.plot(range(q), time2, label='Итерация', color='blue', marker='o', markersize=7)
plt.legend()
plt.xlabel('n')
plt.ylabel('Время')
plt.title('График')
plt.show()
