tabel = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_doard(board):

    for row in board:
        for cell in row:
            print(cell, end='')
        print()
def check_win(board, player):

    if row in board:
        if row.count(player) == 3:
            return True

    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][2] == player: # i бегает по range(3) (проверка по вертикали)
            return True

    if board[0][0] == player and board[1][1] == player and board[2][0] == player: # проверка по диагонали
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

current_player = 'X' #Данная переменная будет хранить игрока, который играет сейчас
#Прописываем основной цикл, в котором будет проходить вся игра
while True:
    print_doard(tabel)
    print('Ход игрока', current_player)
    row = int(input('Введите номер строки: ')) - 1
    col = int(input('Введите номер столбца: ')) - 1

    if tabel[row][col] != '-':
        print('Ячейка занята')
        continue

    tabel[row][col] = current_player

    if check_win(tabel, current_player):
        print_doard(tabel)
        print(f'Игрок {current_player} выйграл!!')

    if all([cell != '-' for row in tabel for cell in row]):
        print('Ничья')
        print_doard()
        break

current_player = '0' if current_player == 'X' else "X"




