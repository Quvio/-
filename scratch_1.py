'''Лабораторная работа №3
С клавиатуры вводится два числа K и N.
Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение,
а целенаправленное.

Для ИСТд-12 вид матрицы А
Е В
D С

Области
    1
  4   2
    3
18.Формируется матрица F следующим образом: если в С количество чисел, больших К в нечетных столбцах в области 3
больше, чем произведение чисел в нечетных строках в области 2, то поменять в В симметрично области 1 и 3 местами,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*F+ K* F T .
Выводятся по мере формирования А, F и все матричные операции последовательно'''

import random

def printM(x):
    for i in range(len(x)):
        for j in range(len(x)):
            print("{:4d}".format(x[i][j]), end=" ")
        print()

#Создание матриц
K, N = int(input()), int(input())
half = N // 2
B, E, D, C = [], [], [], []
R = [B, E, D, C]
A = []
for r in range(4):
    for _ in range(N // 2):
        a = [random.randint(-10, 10) for i in range(N // 2)]
        R[r].append(a)
for i in range(N // 2):
    A.append(E[i] + B[i])
for i in range(N // 2):
    A.append(D[i] + C[i])
print("Матрица А")
printM(A)

count = 0
s = 1
# зона 3
for i in range(half - 1, half // 2 - 1, -1):
    if i > half - i:
        for j in range(i, half - i - 2, -1):
            if i % 2 == 0 and C[i][j] > K: count += 1
    else:
        for j in range(half - i - 1, i - 1, - 1):
            if i % 2 == 0 and C[i][j] > K: count += 1
print("Колличество чисел в 3 зоне больших К:", count)

f = half // 2  # зона 2
for i in range(half // 2):
    for j in range(half - 1, f - i, -1):
        if j % 2 != 0: s *= C[i][j]
    f -= 1
for i in range(half // 2, half):
    for j in range(half - 1, i - 1, -1):
        if j % 2 != 0: s *= C[i][j]
print("Произведение чисел в зоне 2:", s)

#Трансформации
F = []
if count > s:
    for i in range(half - 1, half // 2 - 1, -1):
        for j in range(i, half - i - 2, -1):
            C[i][j], C[half - i - 1][j] = C[half - i - 1][j], C[i][j]
    for i in range(N // 2):
        F.append(E[i] + B[i])
    for i in range(N // 2):
        F.append(D[i] + C[i])
else:
    for i in range(N // 2):
        F.append(C[i] + B[i])
    for i in range(N // 2):
        F.append(D[i] + E[i])
print("Матрица F")
printM(F)
#Вычисления
# К*А
for i in range(N):
    for j in range(N):
        A[i][j] *= K
print("матриица K*A:" )
printM(A)
#(K*A)*F
AKF = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            AKF[i][j] += A[i][j] * F[k][j]
print("матриица (K*A)*F:" )
printM(AKF)
#K*FT
KF = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        KF[i][j] = K * F[j][i]
print("матриица K*FT:" )
printM(KF)
print()
#(K*A) * F + K * FT
for i in range(N):
    for j in range(N):
        AKF[i][j] += KF[i][j]
print("Результат:")
printM(AKF)