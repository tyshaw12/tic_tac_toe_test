

def main():
    user=""
    
    board = board_creation()
    board_viewed(board)
    picks = pick_first()
    user = user_fun(picks)
    while not (winner(board)):
        board_viewed(board)
        moving(user, board)
        user = next_user(user)
    board_viewed(board)
    print(f"Congratulations! {user}'s lost!")
    
    
def board_creation():
    board = []
    for box in range(9):
        board.append(box + 1)
    return board


def board_viewed(board):
    print()
    print(f"{board[0]}{board[1]}{board[2]}")
    print(f"{board[3]}{board[4]}{board[5]}")
    print(f"{board[6]}{board[7]}{board[8]}")
    print()

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

#def moving(user, board):
        #square = int(input("{user}'s turn to choose a square (1-9): "))
        #test1 = board[square - 1] = user
        #if test1 == "X" or "O":
            #square = int(input("Try again, {user} (1-9): "))
        #elif test1 != "X" or "O":
            #board[square - 1] = user
            
def moving(user, board):
    square = int(input(f"{user}'s turn to choose a square (1-9): "))
    board[square - 1] = user

def pick_first():
    first = ""
    while first != 1 or 2:
        first = (input("Would you like to be X's or O's? Respond with an 'X' or 'O'. "))
        if first == 'O':
            return(f"You will be X's, other user will be O's")
        elif first == 'X':
            return(f"You will be O's, other user will be X's. ")

def user_fun(picks):
    if picks == "You will be O's, other user will be X's. ":
        return("X")
    elif picks == "You will be X's, other user will be O's. ":
        return("O")
    
def next_user(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

def check_board(board):
    for i in range(9):
        while board == 'X' or 'O':
            print(f"Try a new spot. This one is taken by {board}")

main()
