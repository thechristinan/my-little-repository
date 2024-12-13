
board = list(range(1,10))

def draw_board(board):
    ''' Функция рисует игровое поле '''
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|")
        print("-" * 13)

def take_input(player_token):
   '''Функция считывает ход игрока и проверяет корректность хода'''
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята! Повторите попытку.")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
    '''Функция проверяет победу одного из игроков'''
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for pos in win_coord:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            return board[pos[0]]
    return False
##########################################################################################################

print("Добро пожаловать в игру 'Крестики-нолики!'")
def main_game(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break

main_game(board)

input("Нажмите Enter для выхода!")

