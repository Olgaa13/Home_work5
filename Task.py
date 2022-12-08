# 2. Создайте программу для игры в ""Крестики-нолики"".
# (в консоли происходит выбор позиции)

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def show_field(field):
    for i in range(3):
         print ("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")


def input_data(player_mot):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_mot+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer-1]) not in "XO"):
                field[player_answer-1] = player_mot
                valid = True
            else:
                print('Эта клеточка уже занята')
        else:
            print('Некорректный ввод. Введите число от 1 до 9 чтобы походить.')
              

def check_win(field):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False    


def main(field):
    counter = 0
    win = False
    while not win:
        show_field(field)
        if counter % 2 == 0:
            input_data("X")
        else:
            input_data("O")
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print(tmp, 'выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    show_field(field)  

main(field)      