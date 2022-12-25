import random
from random import *

'''from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
import ctypes as ct
class main:
    def __init__(self, master):
        self.master=master
        self.master = master
        self.master.minsize(width=850, height=250)
        self.master.title('Крестики-нолики')
        self.master.geometry('1000x1024')
        self.master.configure(bg='white',)
        self.labelHeader=Label(self.master, text="Крестики-нолики")
        self.labelHeader.config(bg="#afafaf", fg='white', font=('Arial', 100))
        self.labelHeader.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.buttonStart=Button(self.master,text="Начать игру", command=self.gameStart,font=('Arial', 24))
        self.buttonStart.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.buttonStart.config(bg='#afafaf', fg='white',font=('Arial', 24))
        self.labelChoose=Label(self.master,text="Выберите сторону:")
        self.labelChoose.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.labelChoose.config(bg='#afafaf', fg='white',font=('Arial', 24))
        self.side = BooleanVar()
        self.side.set(True)
        self.radioX = Radiobutton(self.master, text="X", variable=self.side, value=1, bg='#afafaf',font=('Arial', 24))
        self.radioX.place(relx=0.47, rely=0.57, anchor=CENTER)
        self.radioY = Radiobutton(self.master, text="O", variable=self.side, value=0, bg='#afafaf',font=('Arial', 24))
        self.radioY.place(relx=0.53, rely=0.57, anchor=CENTER)

        self.buttonExit=Button(self.master, text="Выйти из игры")
        self.buttonExit.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.buttonExit.config(bg='#afafaf', fg='white',font=('Arial', 24))

        self.master.mainloop()

    def gameStart(self):
        pass
root=Tk()
''''''root.update()
set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
get_parent = ct.windll.user32.GetParent
hwnd = get_parent(root.winfo_id())
value = 2
value = ct.c_int(value)
set_window_attribute(hwnd, 20, ct.byref(value),
                     4)''''''
root.configure(highlightcolor='#afafaf', highlightthickness=20)
main(root)'''

'''class minimax:
    def __init__(self):'''


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

def dinamic_minimax(cur_board, cur_turn, depth):
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


                    result = minimax(cur_board, cur_turn ^ 1, depth+1)
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
        if depth == 0:
            idx = randint(0,len(results)-1)
            return results[idx][0], results[idx][1]
        else:
            return best_result

    if cur_state == 'draw':
        return 0
    if cur_state == 'X':
        return 10
    if cur_state == 'O':
        return -10





# build_board()
'''random_board()
print_board()
check_board()
'''
# turn = 0
# game = 1
# players = ['X', 'O']
# print('start')
# counter = 0

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
    print(len(States))
    preload_minimax(main_board,0,0)
def half_load():
    print(len(States))
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
    print(len(read))
# print('start')
# k_games = 0
def play_game():
    turn = 0
    while True:
        # print(counter+1)
        print(players[turn], 'turn\nbefore')
        print_board(main_board)

        if turn:
            while game:
                # x=randint(0,2)
                # y=randint(0,2)
                x, y = input().split()
                x=int(x)
                y=int(y)

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
            print(res)
            clear_board()
            if(res=='O'):
                print("ERROR")
        turn ^= 1
print_board(main_board)
'''
0 0
0 1
0 2
'''