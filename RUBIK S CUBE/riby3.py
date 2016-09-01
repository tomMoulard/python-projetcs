#made by moular_b
#Sudoku Solver
#made  2016-01-25

#In this grid :
#   - 0 is for Green
#   - 1is for Red
#   - 2 is for Yellow
#   - 3 is for White
#   - 4 is for Blue
#   - 5 is for Orange
#   - 9 is for null


solvedGrid = [[9,9,9,0,0,0,9,9,9],
                            [9,9,9,0,0,0,9,9,9],
                            [9,9,9,0,0,0,9,9,9],
                            [1,1,1,2,2,2,3,3,3],
                            [1,1,1,2,2,2,3,3,3],
                            [1,1,1,2,2,2,3,3,3],
                            [9,9,9,4,4,4,9,9,9],
                            [9,9,9,4,4,4,9,9,9],
                            [9,9,9,4,4,4,9,9,9],
                            [9,9,9,5,5,5,9,9,9],
                            [9,9,9,5,5,5,9,9,9],
                            [9,9,9,5,5,5,9,9,9]]

def prinGrid(grid):
    for x in grid:
        for y in x:
            if y == 9:
                print(" ", end=' ')
            else:
                print(y, end=' ')
        print('')

print(solvedGrid):

def getGrid ();
    