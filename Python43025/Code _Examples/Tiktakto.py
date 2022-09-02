# print(a) == print(a, end='\n')

def printMatrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
    print()


matrix = [[0,0,0],[0,0,0],[0,0,0]]

# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         matrix[row][col] 

## game of tiktaktoe
flag = True
while flag:
    print("welcome to tiktaktoe!")
    #player_name = input("enter your name: ")

    user_move = input("enter your move 0,0: ")

    user_move = user_move.split(",")
    row = user_move[0]
    col = user_move[1]

    row = int(row)
    col = int(col)

    if matrix[row][col] == 0:
        matrix[row][col] = 'X'








# print the matrix

# for row in range(3):

#     for col in range(3):
#         print(0, end=' ')
    
#     print()


def main():
    pass

main()    