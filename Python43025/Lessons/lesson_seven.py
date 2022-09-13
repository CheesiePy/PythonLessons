
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

    
# def create_players():
#     pass

def get_coordinates():
    pass

def check_coordinates(size, move): 
    pass     

# def check_game_over():
#     pass

def main(): # this is were the magic happens
    print_board(create_board(3))

    
main()    