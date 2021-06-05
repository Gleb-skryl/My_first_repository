# Создаем игровое поле
field = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
print(len(field))

# Выводим игровое поле на печать
def print_field(field):
    # вывод номера столбцов
    print(' ', *range(1, len(field)+1), sep='  ')
    # вывод номеров строк и их содержимого
    for i in range(len(field)):
        print(i+1, end=" ")
        for item in field[i]:
            print_cell(item)
        print()
    print()


# Выводим значение каждой клеточки в игровое поле
def print_cell(cell):
    value = "[E]"
    if cell == None:
        value = "[ ]"
    elif cell == 1:
        value = '[X]'
    elif cell == 0:
        value = '[O]'
    print(value, end="")


# Выполняем ход игроков
def make_move(player_type):
    print("Ход ноликов") if player_type == "нолик" else print("Ход крестиков")
    print()
    row = int(input("Введите номер строки: "))
    # Выполняем проверку введенного числа
    while row > 3 or row < 1:
        row = int(input("Введите номер строки от 1 до 3: "))
    column = int(input("Введите номер столбца: "))
    while column > 3 or column <1:
        column = int(input("Введите номер строки от 1 до 3: "))
    # Выполняем проверку, свободна ли клетка
    if field[row-1][column-1] == None:
        field[row-1][column-1] = 0 if player_type == "нолик" else 1
    else:
        print("Эта клетка уже занята, введите другие координаты")
        print()
        make_move(player_type)
    print()


# Проверка строк
def check_rows(field):
    for row in field:
        x_count = row.count(1)
        o_count = row.count(0)
        if x_count == len(row):
            return 1
        if o_count == len(row):
            return 0
        else:
            return -1


# Проверка столбцов
def check_columns(field):
    x_count = 0
    o_count = 0
    for i in range(len(field)):
        for column in field:
            if column[i] == 1:
                x_count += 1
            elif column[i] == 0:
                o_count += 1
    if o_count == len(field):
        return 0
    if x_count == len(field):
        return 1
    return -1


# Выполняю проверку диагонали справа налево
def check_diag1(field):
    x_count = 0
    o_count = 0
    i = 0
    for j in range(len(field) - 1, -1, -1):
        if field[i][j] == 1:
            x_count += 1
        elif field[i][j] == 0:
            o_count += 1
        i += 1
    if o_count == len(field):
        return 0
    if x_count == len(field):
        return 1
    return -1


# Выполняю проверку диагонали справо налево
def check_diag2(field):
   # print("Проверяю диагональ слева направо")
    x_count = 0
    o_count = 0
    for i in range(len(field)):
        if field[i][i] == 1:
            x_count += 1
        elif field[i][i] == 0:
            o_count += 1
    if o_count == len(field):
        return 0
    if x_count == len(field):
        return 1
    return -1


# Выполняю комплексную проверку
def check_win(field):
    checks = [check_rows, check_columns, check_diag1, check_diag2]
    for func in checks:
        result = func(field)
        if result != -1:
            return result
    return -1


# Игра
def game():
    print("Добро пожаловать в игру крестики-нолики!")
    print()
    while True:
        print_field(field)
        make_move("крестик")
        check_win(field)
        if check_win(field) == 1:
            print_field(field)
            print("Крестики победили")
            break
        print_field(field)
        make_move("нолик")
        check_win(field)
        if check_win(field) == 0:
            print_field(field)
            print("Нолики победили")
            break

game()
