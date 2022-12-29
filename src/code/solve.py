import random
import pygame
import sys
from random import *

main_board = []

def check_board(cur_board):
    # print('check - ',end='')

    for i in range(3):
        if cur_board[i][0] != 'e':
            j = 1
            for j in range(1, 3):
                if cur_board[i][j] != cur_board[i][j - 1]:
                    j -= 1
                    break
            if j == 2:
                # print('winner is {0}'.format(cur_board[i][j]))
                return cur_board[i][j]

    for i in range(3):
        if cur_board[0][i] != 'e':
            j = 1
            for j in range(1, 3):
                if cur_board[j][i] != cur_board[j-1][i]:
                    j -= 1
                    break
            if j == 2:
                # print('winner is {0}'.format(cur_board[j][i]))
                return cur_board[j][i]

    if cur_board[0][0] != 'e':
        for i in range(1,3):
            if cur_board[i][i] != cur_board[i-1][i-1]:
                i -= 1
                break
            if i == 2:
                # print('winner is {0}'.format(cur_board[i][i]))
                return cur_board[i][i]

    if cur_board[0][2] != 'e':
        for i in range(1,3):
            if cur_board[i][2-i] != cur_board[i-1][2-(i-1)]:
                i -= 1
                break
            if i == 2:
                # print('winner is {0}'.format(cur_board[i][2-i]))
                return cur_board[i][2-i]

    for i in range(3):
        for j in range(3):
            if cur_board[i][j] == 'e':
                # print('playing')
                return 'playing'
    # print('draw')
    return 'draw'



def build_board():
    for i in range(3):
        main_board.append([])
        for j in range(3):
            main_board[i].append('e')


def clear_board():
    for i in range(3):
        main_board.append([])
        for j in range(3):
            main_board[i][j]='e'

def random_board():
    for i in range(3):
        for j in range(3):
            main_board[i][j] = 'e' if not randint(0,2) else 'X' if randint(0,1) else 'O'


def print_board(cur_board):
    for i in range(3):
        for j in range(3):
            print(cur_board[i][j], end=' ')
        print()

def state_id(cur_board, cur_turn):
    ans = players[cur_turn]
    for i in range(3):
        for j in range(3):
            ans+=cur_board[i][j]
    return ans

States = {}


def preload_minimax(cur_board, cur_turn, depth):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    cur_state = check_board(cur_board)
    if cur_state == 'playing':
        best_result = 0
        results = []

        if cur_turn:
            best_result = 20
        else:
            best_result = -20

        for i in range(3):
            for j in range(3):
                if cur_board[i][j] == 'e':
                    cur_board[i][j] = players[cur_turn]


                    result = preload_minimax(cur_board, cur_turn ^ 1, depth+1)
                    # if depth == 1 and flag:
                    #     print(cur_turn, best_result)
                    #     print_board(cur_board)
                    #     print('flag res=', result)
                    #     print()
                    cur_board[i][j] = 'e'

                    if cur_turn:

                        if result <= best_result:
                            if result == best_result:
                                results.append([i,j])
                            else:
                                results.clear()
                                results.append([i,j])
                                best_result = result
                    else:
                        if result >= best_result:
                            if result == best_result:
                                results.append([i,j])
                            else:
                                results.clear()
                                results.append(
                                    [i,j]
                                )
                                best_result = result

        idx = state_id(cur_board, cur_turn)
        States[idx] = results
        return best_result

    if cur_state == 'draw':
        idx = state_id(cur_board, cur_turn)
        States[idx] = []
        return 0
    if cur_state == 'X':
        idx = state_id(cur_board, cur_turn)
        States[idx] = []
        return 10
    if cur_state == 'O':
        idx = state_id(cur_board, cur_turn)
        States[idx] = []
        return -10

def get_move(cur_id):
    move = randint(0, len(States[cur_id]) - 1)
    x, y = States[cur_id][move][0], States[cur_id][move][1]
    return (x,y)


def random_move(cur_id):

    moves = []
    # print(cur_id)
    for i in range(1,10):
        if cur_id [i] =='e':
            moves.append([int((i-1)/3),(i-1)%3])
    id = randint(0,len(moves)-1)
    # print(id)
    # print(len(moves))
    x,y = moves[id][0],moves[id][1]
    return (x,y)


build_board()
'''random_board()
print_board()
check_board()
'''
turn = 0
game = 1
players = ['X', 'O']
# print('start')
counter = 0

'''crbrd = [['e','e','e'],['e','e','e'],['e','e','e']]
crbrd = main_board
x, y = minimax(crbrd,cur_turn=0,depth=0)
crbrd[x][y] = 'X'
print('ans')
print_board(crbrd)'''




# while game:
#     # print(counter+1)
#     # print(players[turn], 'turn\nbefore')
#     # print_board(main_board)
#
#     if turn:
#         '''while game:
#             x=randint(0,2)
#             y=randint(0,2)
#             # x, y = input().split()
#             x=int(x)
#             y=int(y)
#
#             if(main_board[x][y]!='e'):
#                 continue
#             main_board[x][y] = players[turn]
#             break'''
#         x, y = dinamic_minimax(main_board, turn, 0)
#         main_board[x][y] = players[turn]
#     else:
#         x, y = dinamic_minimax(main_board, turn, 0)
#         main_board[x][y] = players[turn]
#
#     if check_board(main_board) != 'playing':
#         res=check_board(main_board)
#         print(res)
#         clear_board()
#         if(res=='O'):
#             print("ERROR")
#     turn ^= 1
# print_board(main_board)
def start_load():
    # print(len(States))
    preload_minimax(main_board,0,0)
def half_load():
    # print(len(States))
    preload_minimax(main_board,1,0)
    fo=open("src/solve/solve.txt",'w')
    for i in States:
        fo.write(str(i))
        fo.write(' ')
        fo.write(str(States[i]))
        fo.write('\n')
def load():
    fi = open("src/solve/solve.txt", 'r')
    read = fi.read()
    flag = 0

    s = ''
    key = ''
    val_x = ''
    val_y = ''
    values = []
    for i in read:
        if i == ' ':
            continue
        elif i == '[':
            if not flag:
                key = s
            flag+=1
            s = ''
        elif i == ']':
            flag-=1
            if flag:
                val_y = s
                # print(val_x, val_y)
                values.append([int(val_x), int(val_y)])
                s = ''
        elif i == ',':
            val_x = s
            s = ''
        elif i =='\n':

            States[key] = values

            key = ''
            s=''
            values = []
        else:
            s+=i
    # print(len(read))
# print('start')
# k_games = 0
def play_game():
    while True:
        turn = 0
        # print(counter+1)
        print(players[turn], 'turn\nbefore')
        # print_board(main_board)

        if turn:
            while game:
                # x=randint(0,2)
                # y=randint(0,2)
                x, y = input().split()
                x=int(x)-1
                y=int(y)-1

                if(main_board[x][y]!='e'):
                    continue
                main_board[x][y] = players[turn]
                break
            '''idx = state_id(main_board, turn)
            move = randint(0, len(States[idx]) - 1)
            x, y = States[idx][move][0], States[idx][move][1]
            main_board[x][y] = players[turn]'''
        else:
            idx = state_id(main_board,turn)
            move = randint(0, len(States[idx])-1)
            x, y = States[idx][move][0], States[idx][move][1]
            main_board[x][y] = players[turn]

        if check_board(main_board) != 'playing':
            res=check_board(main_board)
            # print(res)
            clear_board()
            if(res=='O'):
                print("ERROR")
        turn ^= 1
# print_board(main_board)
'''
0 0
0 1
0 2
'''