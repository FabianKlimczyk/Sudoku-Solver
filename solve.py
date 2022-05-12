'''
    solve.py - checks an unfinished sudoku and solves it in case there is a solution
'''

def solve(board: list) -> None:
    printSolution(board)
    
def printSolution(sudokuBoard: list) -> None:
    '''
        Prints a solution of the sudoku board
    '''
    print("Please, see one solution for the sudoku below!")
    print()
    # print each value and divider
    for row in range(len(sudokuBoard)):
        for column in range(len(sudokuBoard)):
            if column == 2 or column == 5: 
                print(f' {sudokuBoard[row][column]} |',end =" ")
            else:
                print(f' {sudokuBoard[row][column]}',end =" ")
        print()
        if row == 2 or row == 5:
            print("- - - - - - - - - - - - - - - -")
    print()
        
board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,3,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]

solve(board)