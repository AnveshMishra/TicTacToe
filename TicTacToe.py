#<-----Global Varibale----->

board=[
"_","_","_",
"_","_","_",
"_","_","_"
]


game_is_still_going=True



winner=None


current_player="X"






#<---------Functions-------->
#<-----To Display tic tac toe board--->
def dislpay_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
    print()





def play_game():
    while game_is_still_going:

        dislpay_board()
        handle_player()
        check_if_game_over()
        flip_player()
        



def handle_player():
    global board,current_player
    print(current_player+"s turn")
    postion=input("enter the postion from 1-9: ")

    valid=False

    while not valid:
        while postion not in ["1","2","3","4","5","6","7","8","9"]:

            postion=input("enter the postion from 1-9: ")
            
        postion=int(postion)-1

        if board[postion]=="_":
            valid=True
        else:
            print("you Can't go there")
        
        
    board[postion]=current_player
    dislpay_board()



def check_if_game_over():
    check_win()
    check_tie()



def check_win():
    global winner
    win_row = row_win()
    win_column = column_win()
    win_digonal = digonal_win()


    if win_row:
        winner=win_row
    elif win_column:
        winner=win_column
    elif win_digonal:
        winner=win_digonal
    


def row_win():
    global board,game_is_still_going
    row_1=board[0]==board[1]==board[2]!="_"
    row_2=board[3]==board[4]==board[5]!="_"
    row_3=board[6]==board[7]==board[8]!="_"

    if row_1 or row_2 or row_3 :
        game_is_still_going=False
    
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    



def column_win():
    global board,game_is_still_going
    column_1=board[0]==board[3]==board[6]!="_"
    column_2=board[1]==board[4]==board[7]!="_"
    column_3=board[2]==board[5]==board[8]!="_"

    if column_1 or column_2 or column_3 :
        game_is_still_going=False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_tie():
    global game_is_still_going
    if "_" not in board:
        game_is_still_going=False
        return True
    else:
        return False


def digonal_win():
    global board,game_is_still_going
    digonal_1=board[0]==board[4]==board[8]!="_"
    digonal_2=board[2]==board[4]==board[6]!="_"

    if digonal_1 or digonal_2:
        game_is_still_going=False


    if digonal_1:
        return board[0]
    elif digonal_2:
        return board[2]
    else:
        return None



    


def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"

            
        
#<-----------Main-------->

play_game()

if winner=="X" or winner=="O":
    print(winner+"s Wins")
else:
    print("Game is Tie")