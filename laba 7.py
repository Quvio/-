"""Задание состоит из двух частей. 1 часть – написать программу в соответствии со своим вариантом задания. Написать 2
варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение. 2 часть –
усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики
объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 18. Дан одномерный массив. Сформировать все возможные варианты данного массива путем перестановки
отрицательных элементов."""
from tkinter import *
from itertools import permutations

def prepare(x, quq):
    mal = []
    per = x.copy()
    for i in range(len(per)):
        if int(per[i]) < 0:
            mal.append(per[i])
            per[i] = "m"
    if quq == 1:
        return mal
    elif quq == 2:
        return per
    elif quq == 3:
        return mal, per


def het(x):
    global res
    res = []
    mal, per = prepare(x, 3)
    for j in range(1, len(per), 2):
        if input[j] in mal:
            mal.remove(input[j])
    comb = list(permutations(mal, len(mal)))
    for c in comb:
        workm = per.copy()
        cn = 0
        for i in range(len(workm)):
            if workm[i] == "m" and i % 2 == 0:
                workm[i] = c[cn]
                cn += 1
            else:
                workm[i] = input[i]
        res.append(workm)
    for i in res:
        a = str(i) + "\n"
        output.insert(END, a, "tabs")

def wtk():
    b = 9999
    rem = ""
    for c in res:
        a = 0
        for i in range(len(c) - 1):
            a += abs(abs(int(c[i])) - abs(int(c[i+1])))
        b = min(a, b)
        if b == a:
            rem = c
    output.insert(END, ("Минимальный путь:",b, "в", rem))



root = Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Code Output")

text = Entry(root, width=35)
text.grid(row=0, column=1, padx=10, pady=5)

def display():
    output.delete("1.0", END)
    global input
    input = list(text.get().split())
    het(input)
    wtk()


button = Button(root, text="Ввод", width=10, command=display)
button.grid(row=1, column=0, columnspan=2, pady=10)
output = Text(root, height=10, width=50)
output.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
scrollbar = Scrollbar(root, command=output.yview)
scrollbar.grid(row=2, column=2, sticky='nsew')
output.config(yscrollcommand=scrollbar.set)




label = Label(root, text= "Введите числа через пробел", font = 35)
label.grid(row=0, column=0, padx=10, pady=5)
root.eval(f'tk::PlaceWindow . center')
root.mainloop()
