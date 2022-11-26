def hello():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                         ")
    print(" Добро пожаловать в игру:")
    print("                         ")
    print("    Крестики - нолики    ")
    print("                         ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("чтобы сделать ход, нужно ")
    print("будет ввести адрес ячейки")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")


def field_output(field):
    for i in range(4):
        for j in range(4):
            print(field[i][j], end=" ")
        print("          ")


hello()
print(" Вот наше поле для игры: ")

field = [
    [" ", 0, 1, 2],
    [0, "-", "-", "-"],
    [1, "-", "-", "-"],
    [2, "-", "-", "-"]
]

field_output(field)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Первыми ходят крестики.  ")
print("Ты будешь за крестики ?  ")

while True:
    y_n = input("да/нет?")
    if y_n == "да":
        XO = "Х"
        break
    elif y_n == "нет":
        XO = "О"
        break
    else:
        print("Неправильно введен ответ.")
        print("Ты будешь за крестики ?  ")


def enter(x, y):
    field[x + 1][y + 1] = XO









