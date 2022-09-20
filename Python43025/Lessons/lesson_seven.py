
## board 3x3

## two players X and O

## turn 

"""
    1. create a board & show board 
    2. create two players

    while game is not over:
        3. get coordinates from the user
        4. check if the coordinates are valid -> in board bounds and empty
        5. check if the game is over
"""



def create_board(size):
    matrix = []
    for row in range(size):
        matrix.append([])
        for col in range(size):
            matrix[row].append(0)
    return matrix  ##  -> [[0,0,0],[0,0,0],[0,0,0]]





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


board = create_board(3) # board -> [[0,0,0],[0,0,0],[0,0,0]]
for row in range(len(board)): # row -> 0,1,2 run 3 times
    print("row is:",row)
    for col in range(len(board[row])): # col -> 0,1,2 run 3 x 3 times
        print("col is:",col)
        for z in range(3): # z -> 0,1,2 run 3 x 3 x 3 times
            print("z is:", z)
            for w in range(3): # w -> 0,1,2 run 3 x 3 x 3 x 3 times
                print("w is:", w) 
    print()
"""

"""    


# for i in range(5):
#     for j in range(5):
#         print(j)


# for i in range(1, 5): # 1,2,3,4 run 4 times
#     print(i)
#     for j in range(2,7): # 2,3,4,5,6 run 4 x 5 times
#         print(j)


# for row in range(1,4): # 0 -> n-1
#     #print("row is:", row)
#     for col in range(1,4):
#         #print("col is:", col + row)
#         for jelly in range(1,3):
#             print("jelly is:", jelly + row + col)
