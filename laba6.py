"""Задание состоит из двух частей. 1 часть – написать программу в соответствии со своим вариантом задания. Написать 2
варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение. 2 часть –
усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики
объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 18. Дан одномерный массив. Сформировать все возможные варианты данного массива путем перестановки
отрицательных элементов."""
import timeit
from itertools import permutations

#Вывод
def printres(x):
    for c in x:
        print(*c)

#Создание массива отриц чисел подготовка основного массива
def prepare(x,quq):
    mal = []
    per = x.copy()
    for i in range(len(per)):
        if per[i] < 0:
            mal.append(per[i])
            per[i] = "m"
    if quq == 1:
        return mal
    elif quq == 2:
        return per
    elif quq == 3:
        return mal, per

# замена функцией Питона
def funtion_P(x):
    global res
    res = []
    mal, per = prepare(x, 3)
    comb = list(permutations(mal, len(mal)))
    for c in comb:
        workm = per.copy()
        cn = 0
        for i in range(len(workm)):
            if workm[i] == "m":
                workm[i] = c[cn]
                cn += 1
        res.append(workm)
    printres(res)

#Алгоритмическая замена
def function_A(mmx, mel, start, end):
    if start == end:
        cn = 0
        mmy = mmx.copy()
        for i in range(len(mmx)):
            if mmy[i] == "m":
                mmy[i] = mel[cn]
                cn += 1
        print(*mmy)
    else:
        for i in range(start, end + 1):
            mel[i], mel[start] =  mel[start], mel[i]
            function_A(mmx, mel, start + 1, end)
            mel[i], mel[start] =  mel[start], mel[i]

def mainF():
    funtion_P(mmm)

def mainA():
    mel, mmx = prepare(mmm, 3)
    function_A(mmx, mel, 0, len(prepare(mmm, 1)) - 1)

#Усложнение
def het(x):
    res = []
    mal, per = prepare(x, 3)
    for j in range(1, len(per), 2):
        if mmm[j] in mal:
            mal.remove(mmm[j])
    comb = list(permutations(mal, len(mal)))
    for c in comb:
        workm = per.copy()
        cn = 0
        for i in range(len(workm)):
            if workm[i] == "m" and i % 2 == 0:
                workm[i] = c[cn]
                cn += 1
            else:
                workm[i] = mmm[i]
        res.append(workm)
    printres(res)

def nehet(mmx, mel, start, end,):
    if start == end:
        cn = 0
        mmy = mmx.copy()
        for i in range(len(mmx)):
            if mmy[i] == "m" and i % 2 != 0:
                mmy[i] = mel[cn]
                cn += 1
            else:
                mmy[i] = mmm[i]
        print(*mmy)
    else:
        for i in range(start, end +1):
            mel[i], mel[start] =  mel[start], mel[i]
            nehet(mmx, mel, start + 1, end)
            mel[i], mel[start] =  mel[start], mel[i]

def wtk():
    b = 9999
    rem = ""
    for c in res:
        a = 0
        for i in range(len(c) - 1):
            a += abs(abs(c[i]) - abs(c[i+1]))
        b = min(a, b)
        if b == a:
            rem = c
    print("Минимальный путь:",b, "в", rem)
mmm =  [int(i) for i in input("Веддите числа через пробел:\n").split()]
print("Варианты замены алгоритмическим подходом:")
print("Время выполнения алгоритмического подхода:\n", timeit.timeit(lambda: mainF(), number=1))
print("Варианты замены с использованием функции питона:")
print("Время выполнения функции питона:\n", timeit.timeit(lambda: mainA(), number=1))
print("Усложнение(меняются только четные позиции):")
het(mmm)
print("Усложнение(меняются только нечетные позиции):")
mmx = prepare(mmm, 2)
mel = prepare(mmm, 1)
for i in range(0, len(mmx), 2):
    if mmm[i] in mel:
        mel.remove(mmm[i])
nehet(mmx, mel, 0, len(mel) - 1,)
wtk()
