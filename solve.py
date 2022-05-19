'''
    solve.py - checks an unfinished sudoku and solves it in case there is a solution
'''

import time

isMutable = None 

def solve(board: list, row: int, col: int) -> bool:
    """ run until condition is fulfilled by recursion 
    
    arguments
    ---------
    board list
        current state of the board
    row: int
        current row
    col: int
        current column
    
    """
    
    if row == 8 and col == 8:
        # condition is fullfiled
        printSolution(board)
        return True 
    
    if col == 9:
        # jump to start of next line
        row +=1
        col = 0

    if not isMutable[row][col]:
        # filled on the origional board
        return solve(board,row,col+1)
    
    for i in range (1,10):
        # try out all possible numbers
        if solved(board,row,col,i):
            board[row][col] = i
            if solve(board,row,col+1):
                return True
        board[row][col] = 0
    return False
    
def solved(board: list, row: int, col: int, num: int) -> bool:
    ''' Returns True if the numer does not exist in the same row, column or the block
    
    arguments
    ---------
    board: list
        current state of the board
    row: int
        current rowNo
    col: int
        current colNo
    num: int
        number to check a solution
    
    '''
    
    for i in range(9):
        if board[i][col] == num and row != i:
            return False
        if board[row][i] == num and col != i:
            return False
    
    startRow = row - row % 3
    startCol = col - col % 3
    for rowNo in range (3):
        for colNo in range(3):
            if board[rowNo+startRow][colNo+startCol] ==  num and rowNo != row and colNo != col:
                return False
    
    return True
    
def createMutableCellIndicatorBoard(board: list) -> list:
    ''' According to the original board all mutable cells will be marked as True 
    
    arguments
    ---------
    board: list
        the original sudoku board
        
    '''
    
    return [[False if i > 0 else True for i in innerList ] for innerList in board]
    
def printSolution(board: list) -> None:
    ''' Prints a solution of the sudoku board 
    
    arguments
    ---------
    board: list
        list to print
    
    '''
    
    print("Please, see one solution for the sudoku below!")
    print()
    # print each value and divider
    for row in range(len(board)):
        for column in range(len(board)):
            if column == 2 or column == 5: 
                print(f' {board[row][column]} |',end =" ")
            else:
                print(f' {board[row][column]}',end =" ")
        print()
        if row == 2 or row == 5:
            print("- - - - - - - - - - - - - - - -")
    print()
    
        
board = [
        [0,2,0,3,5,0,0,8,4],
        [0,0,0,4,6,0,0,5,7],
        [0,0,0,2,0,7,0,1,0],
        [0,0,5,0,4,0,8,0,2],
        [0,6,9,0,2,8,0,0,0],
        [0,0,8,0,0,0,1,0,6],
        [7,3,0,8,0,5,4,2,0],
        [9,0,0,7,3,0,0,6,1],
        [0,5,0,0,9,2,0,0,8]
        ]

print('###Start###')
print()

startTime = time.time()
isMutable = createMutableCellIndicatorBoard(board)

if not solve(board,0,0):
    print("There is no solution!")

endTime = time.time()
duration = endTime - startTime
print(f'The calculation run {duration} seconds')

print()
print('###END###')