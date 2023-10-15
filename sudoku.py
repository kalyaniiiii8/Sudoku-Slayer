# Sudoku Solver
#                By- Kalyani Pande

def solve(board):
    # Solves a sudoku board inputted as a 9x9 matrix
    find = empty(board)
    if find:
        r, c = find
    else:
        return True

    for i in range(1,10):
        if check(board, (r, c), i):
            board[r][c] = i

            if solve(board):
                return True

            board[r][c] = 0

    return False


def check(board, pos, n):
    # Checks if attempted move is valid

    # For checking row
    for i in range(0, len(board)):
        if board[pos[0]][i] == n and pos[1] != i:
            return False

    # For checking column
    for i in range(0, len(board)):
        if board[i][pos[1]] == n and pos[0] != i:
            return False

    # For checking box
    xbox = pos[1]//3
    ybox = pos[0]//3

    for i in range(ybox*3, ybox*3 + 3):
        for j in range(xbox*3, xbox*3 + 3):
            if board[i][j] == n and (i,j) != pos:
                return False

    return True


def empty(board):
    # Find empty place in board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def show_board(board):
    # Displays the board
    for i in range(len(board)):
        if i % 3 == 0:
            print(" ---------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(str(board[i][j]) + " | ", end="\n")
            else:
                print(str(board[i][j]) + " ", end="")
     
    print(" ---------------------------")    
