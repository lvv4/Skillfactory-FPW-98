def field_output(field):
    for i in range(4):
        for j in range(4):
            print(field[i][j], end=" ")
        print("          ")


def step():
    while True:
        xx = input("Введи номер строки: ")
        yy = input("Введи номер столбца: ")
        if not (xx.isdigit()) or not (yy.isdigit()):
            print("  Введи числа:  0, 1, 2  ")
            continue

        xx, yy = int(xx), int(yy)

        if xx not in [0, 1, 2] or yy not in [0, 1, 2]:
            print("  Введи числа:  0, 1, 2  ")
            continue

        xx += 1
        yy += 1

        if field[xx][yy] != "-":
            print("     Ячейка занята !     ")
            continue
        else:
            break
    return xx, yy


def check_win():
    win = (([1, 1], [2, 2], [3, 3]), ([1, 3], [2, 2], [3, 1]),
           ([1, 1], [2, 1], [3, 1]), ([1, 2], [2, 2], [3, 2]), ([1, 3], [2, 3], [3, 3]),
           ([1, 1], [1, 2], [1, 3]), ([2, 1], [2, 2], [2, 3]), ([3, 1], [3, 2], [3, 3]))
    for tup in win:
        list_win = []
        for couple in tup:
            list_win.append(field[couple[0]][couple[1]])
        if list_win == ['o', 'o', 'o']:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("   Выиграли нолики !!!   ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            return True
        if list_win == ['x', 'x', 'x']:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("  Выиграли крестики !!!  ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            return True
    return False


print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Добро пожаловать в игру:")
print("                         ")
print("    Крестики - нолики    ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("чтобы сделать ход, нужно ")
print("будет ввести адрес ячейки")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
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

n_steps = 0

while True:
    result = check_win()
    if result:
        break
    n_steps += 1
    x, y = step()
    if n_steps == 9:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("        Ничья !!!        ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        break
    if n_steps % 2 == 1:
        print("  Теперь ходят нолики !  ")
        field[x][y] = "x"
        field_output(field)
    if n_steps % 2 == 0:
        print("  Теперь ходят крестики !  ")
        field[x][y] = "o"
        field_output(field)
