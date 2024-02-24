"""Лабораторная работа №1
Написать программу, которая читая символы из бесконечной последовательности
(эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит
на экран лексемы по определенному правилу. Лексемы разделены пробелами. Преобразование делать
по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод
всех цифр числа. Регулярные выражения использовать нельзя.
Вариант 18.
Четные двоичные числа, не превышающие 102410, в которых встречается больше чем одна серия из трех подряд идущих нуля.
Выводит на экран цифры числа, исключая нули. Отдельно выводится прописью номер позиции, с которой начинается эта серия."""
import os
if not os.path.isfile("text.txt"):
    print("Файл не существует")
    exit()
slv = {"0":"ноль", "1":"один", "2":"два", "3":"три", "4":"четыре", "5":"пять", "6":"шесть", "7":"семь", "8":"восемь", "9":"девять"}
flag = 1
with open ("text.txt", 'r') as f:
    line = f.read()
    nmbrs = line.split()

    print("Результат кода:")
    if nmbrs == []:
        flag = 2
    for i in range(len(nmbrs)):
        a = nmbrs[i]
        if not a.isdigit():
            continue
        if int(a) % 2 != 0 or int(a) >= 1024:
            continue
        bn = bin(int(a))[2::]
        count = 0

        while "000" in bn:
            count += 1
            bn = bn.replace("000", "", 1)
        if count >= 2:
            print("Число номер", i,":", bn.replace("0", ""), end=". ")
            flag = 0
if flag == 1:
    print("В файле нет подходящий чисел")
if flag == 2:
    print("Файл пустой")
