
## board 3x3

## two players X and O

## turn 

"""
    1. create a board
    2. create two players
    3. get coordinates from the user
    4. check if the coordinates are valid -> in board bounds and empty
    5. check if the game is over
"""



def create_board(size): ## [[0,0,0],[0,0,0],[0,0,0]]
    matrix = []
    for row in range(size):
        matrix.append([])
        for col in range(size):
            matrix[row].append(0)
    return matrix


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
        print()

    
def create_players():
    pass

def get_coordinates(size, board):
    x = input("please enter row number: ")
    y = input("please enter col number: ")
    move = [x,y]
    if check_coordinates(size, move, board):
        move = [int(x), int(y)]
        return move
    else:
        print("invalid move")
        get_coordinates(size, board)    

def check_coordinates(size, move, board):
    if move[0].isdigit() and move[1].isdigit():
        if 0 < int(move[0]) <= size and 0 < int(move[1]) <= size:
            if board[int(move[0]) - 1][int(move[1]) -1] == 0:
                return True 
    return False

def insert_move(board, move, player):
    board[move[0] -1][move[1] -1] = player

def check_game_over():
    pass


def main():
    size = 3
    player1 = 'X'
    player2 = 'O'
    board = create_board(size)
    win = False
    counter = 0
    while not win:
        current_player = player1 if counter % 2 == 0 else player2
        print("current player is: ", current_player)
        print_board(board)
        move = get_coordinates(size, board)
        insert_move(board, move, current_player)
        counter += 1
main()     


"""
0 0 0
0 0 0
0 0 0

1. create the algorithm to check for the winner of the game to

1:
X X X
0 0 0
0 0 0

2:
X 0 0
X 0 0
X 0 0

3:
X 0 0
0 X 0
0 0 X 

plan how to check if one of the conditions are true

"""