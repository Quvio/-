"""
Лабораторная работа №4
С клавиатуры вводится два числа K и N.
Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение,
а целенаправленное.

Для ИСТд-12 вид матрицы А
Е В
D С
Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib
Формируется матрица F следующим образом: скопировать в нее А и  если в С количество чисел, больших К в нечетных
столбцах, чем произведение чисел в нечетных строках, то поменять местами С и В симметрично, иначе С и Е поменять местами
 несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
  то вычисляется выражение: A*AT – K * F-1, иначе вычисляется выражение (A-1 +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по
  мере формирования А, F и все матричные операции последовательно.
"""
import numpy as np
import matplotlib.pyplot as plt

k = int(input("Введите число k: "))
n = int(input("Введите число n: "))

if n % 2 != 0:
    print("Введите четное n")
    exit()
a = np.random.randint(-10, 11, (n, n))
print("матрица А\n", a)

e = a[:n//2, :n//2]
b = a[:n//2, n//2:]
d = a[n//2:, :n//2]
c = a[n//2:, n//2:]

count = 0
s = 1
for i in range(1, n//2, 2):
    for j in range(n//2):
        if c[i][j] > k:
            count += 1
        s *= c[i][j]

print("Количество чисел больших К:", count)
print("Произведение чисел:", s)

f1 = a.copy()
f2 = a.copy()
if count>s:
    print('Меняем местами подматрицы В и С симметрично. Получаем матрицу F: \n')
    f2[n//2:, n//2:], f2[:n//2, n//2:]=np.flipud(b), np.flipud(c)
else:
    print('Меняем местами подматрицы С и Е несимметрично. Получаем матрицу F: \n')
    f2[:n//2, :n//2], f2[n//2:, n//2:] = c, e
print(f2)

detA= np.linalg.det(a)
print("Определитель матрицы А:", detA)

diagf = np.trace(f2)
print("Сумма диагоналей матрицы F:", diagf)

treg = np.tril(a)
print("Нижняя треугольная матрица G:\n",treg)
if detA > diagf:
    f3 = a * np.transpose(a) - k * np.linalg.inv(f2)
else:
    f3  = (np.linalg.inv(a)) + (treg - np.transpose(f2)) * k
print("Результат:\n", f3)

#2t = np.arange(-20,20)
a1=  np.max(f1, axis = 1)
b1 = np.min(f1, axis = 1)
c1 = np.mean(f1, axis = 1)
a2 = np.max(f2, axis = 1)
b2 = np.min(f2, axis = 1)
c2 = np.mean(f2, axis = 1)
a3 = np.max(f3, axis = 1)
b3 = np.min(f3, axis = 1)
c3 = np.mean(f3, axis = 1)
ax1 = plt.subplot(311)
plt.plot(a1, color = "red",marker = (5,1), label = "макс значение")
plt.plot(b1, color = "blue",marker = (5,1), label = "мин значение")
plt.plot(c1, color = "green",marker = (5,1), label = "среднее значение")
plt.legend()
plt.ylabel('Значение')
plt.xlabel('Строка')
plt.title('Максимальное, минимальное и среднее значение матрицы A')

ax2 = plt.subplot(312)
plt.plot(a2, color = "red", marker='o', label = "макс значение")
plt.plot(b2, color = "blue", marker='o', label = "мин значение")
plt.plot(c2, color = "green", marker='o', label = "среднее значение")
plt.xlabel('Строка')
plt.ylabel('Значение')
plt.title('Максимальное, минимальное и среднее значение матрицы F ')
plt.legend()

ax3 = plt.subplot(313)
plt.plot(c3, color = "green", marker = ">", label = "макс значение")
plt.plot(a3, color = "red", marker = ">", label = "мин значение")
plt.plot(b3, color = "blue", marker = ">", label = "среднее значение")
plt.xlabel('Строка')
plt.ylabel('Значение')
plt.title('Максимальное, минимальное и среднее значение вычисленного выражения')
plt.legend()

plt.show()



