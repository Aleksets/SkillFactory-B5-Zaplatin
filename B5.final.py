# Процедура отрисовки текущего поля игры
def print_field(tek_field):
    for x in tek_field:
        for y in x:
            print(f"{y} ", end="")
        print("\r")


# Функция оценки желания игроков начать новую игру (с проверкой)
def want_play():
    while True:
        answer = input("Желаете начать новую игру (y/n)? ").lower()
        if answer == "y" or answer == "n":
            break
        else:
            print("Необходимо ввести 'y' или 'n'. Попробуйте снова")
    if answer == "y":
        return True
    else:
        print("Будем рады видеть вас снова!")
        return False


# Начальный вид игрового поля
field_start = (
    (" ", "0", "1", "2"),
    ("0", "-", "-", "-"),
    ("1", "-", "-", "-"),
    ("2", "-", "-", "-")
)
# Все возможные варианты выигрыша
win_possibilities = tuple(map(list, [[()] * 3] * 8))
for i in range(3):
    for j in range(3):
        win_possibilities[i][j] = (i, j)
        win_possibilities[i + 3][j] = (j, i)
        if not i:
            win_possibilities[6][j] = (j, j)
            win_possibilities[7][j] = (j, 3 - j - 1)
win_poss = {}
print("Добро пожаловать в игру 'Крестики-нолики' 3x3!\nАвтор: Заплатин Алексей")
# Проверка на желание начать новую игру
play = want_play()
while play:
    # Стартовые значения переменных
    field = tuple(map(list, field_start))
    win_poss["x"] = tuple(map(tuple, win_possibilities))
    win_poss["o"] = tuple(map(tuple, win_possibilities))
    win = False
    draw = False
    move = "x"
    while not win and not draw:
        # Отрисовка текущего игрового поля
        print_field(field)
        # Выполнение хода игрока (с проверкой)
        while True:
            step = input(f"Ваш ход, {move}. Введите координаты установки {move} "
                         f"в формате '№строки №столбца': ")
            step = " ".join(step.split())
            if step.replace(" ", "").isdigit() and " " in step:
                step = tuple(map(int, step.split(" ")))
                if step[0] < 3 and step[1] < 3:
                    if field[step[0] + 1][step[1] + 1] == "-":
                        break
                    else:
                        print(f"В указанных координатах уже есть символ "
                              f"{field[step[0] + 1][step[1] + 1]}. Попробуйте снова")
                else:
                    print("№строки и №столбца задаются только цифрами 0, 1 или 2")
            else:
                print("Вы нарушили формат ввода. Попробуйте снова")
        # Изменение игрового поля после успешного хода игрока
        field[step[0] + 1][step[1] + 1] = move
        # Проверка достижения победы
        for i in win_poss[move]:
            if step in i:
                for j in i:
                    if field[j[0] + 1][j[1] + 1] != move:
                        break
                else:
                    win = True
        # Если победа ещё не состоялась
        if not win:
            move = "o" if move == "x" else "x"
            win_poss[move] = tuple(filter(lambda x: step not in x, win_poss[move]))
            # Если ничья
            if not win_poss["x"] and not win_poss["o"]:
                draw = True
                print_field(field)
                print("Боевая ничья!")
                play = want_play()
        # Если победа состоялась
        else:
            print_field(field)
            print(f"{move} победил! Поздравляем!")
            play = want_play()
