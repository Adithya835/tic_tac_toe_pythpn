# tic tac toe game


import random

def tic_tac_toe():
    board = ['']*9
    player = 'X '

    for _ in range(9):
        print(f"\n{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}")
        
        if player == 'X':
            move = int(input(f"player{player} position(1-9):"))-1
        else:
            move = random.randint(0,8)

        if board[int(move)] != '':
            print("invalid,try again.")
            continue

        board[(move)-1] = player

        if (board[0] == board[1] == board[2]!= '' or board[3] == board[4] == board[5] != '' or 
            board[6] == board[7] ==board[8] != '' or board[0] == board[3] == board[6] != '' or
            board[1] == board[4] == board[7] != '' or board[2] == board[5] == board[8] != '' or
            board[0] == board[4] == board[8] != '' or board[2] == board[4] == board[6] != ''):
            print(f"player{player} wins")
            return
        else:
            print("its a tie")
tic_tac_toe()
        
