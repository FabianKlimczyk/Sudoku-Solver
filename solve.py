'''
    solve.py - checks an unfinished sudoku and solves it in case there is a solution
'''

from tkinter.tix import CheckList
from typing import List

def solve(board: list) -> None:
    # 1 - create a list of list to mark the mutable cells 
    checkBoard = createCheckBoard(board)

    # 2 -
    currRow, currCol = 0, 0
    currValue = 1 
    while not (currRow == 9 and currCol == 9 and solved(board)): 
        if not checkBoard[currRow][currCol]:
            if currValue <= 9:
                board[currRow][currCol] = currValue 
                valueFits = rowAndLineOk(currRow,currCol, board)
        else:
            if currRow < 8:
                currRow += 1
            elif currCol < 8:
                currCol += 1    
    
    
    # Final stel
    printSolution(board)
    
def solved(board: list) -> bool:
    '''
        Returns True if the last field has a valid value
    '''
    return (board[8][8] > 0) and (rowAndLineOk(8,8,board))
        

def rowAndLineOk(xPos: int,yPos: int,board: list) -> bool:
    rowAndLineOk = True
    #print(f'x: {xPos} - y: {yPos}')
    for cell in range(9):
        if (cell != yPos and board[xPos][cell] == board[xPos][yPos]) or (cell != xPos and board[cell][yPos] == board[xPos][yPos]):
            #print(f'value: {board[xPos][yPos]} - row: {board[xPos][cell]} - column: {board[cell][yPos]}')
            rowAndLineOk = False
    return rowAndLineOk
    
def createCheckBoard(board: list) -> List:
    '''
        According to the argument board all mutable cells will be marked as False 
    '''
    checkBoard=[[True if i > 0 else False for i in innerList ] for innerList in board]
    return checkBoard
    
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
        [0,7,0,0,0,2,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,3,0,4,2],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,5,0,0,0,0,0],
        [0,7,0,0,0,0,0,0,1]
        ]

solve(board)