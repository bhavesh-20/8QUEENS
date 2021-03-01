def set(grid,row,i):
    x,y = row,i
    while x<8 and y<8:
        grid[x][y] = False
        x+=1
        y+=1
    x,y = row,i
    while x<8 and y>=0:
        grid[x][y]= False
        x+=1
        y-=1
    x = 0
    while x<8:
        grid[row][x] = False
        grid[x][i] = False
        x+=1

def reset(grid,solution):

    for j in range(8):
        for k in range(8):
            grid[j][k] = True

    for i in range(len(solution)):
        row = i
        column = int(solution[i])
        x = 0
        while x<8:
            grid[x][column] = False
            grid[row][x] = False
            x+=1

        x, y = row, column
        while x<8 and y<8:
            grid[x][y] = False
            x+=1
            y+=1
        
        x, y = row, column
        while x<8 and y>=0:
            grid[x][y]= False
            x+=1
            y-=1


def solvepuzzle(solution,grid,row):
    if row==8:
        f.write(solution+"\n")
    else:
        for i in range(8):
            if grid[row][i]:
                solution+=str(i)
                set(grid,row,i)
                solvepuzzle(solution,grid,row+1)
                solution=solution[:-1]
                reset(grid,solution)

f = open("solution.txt","w")
solution = ''
grid = [[True]*8 for _ in range(8)]
row = 0
solvepuzzle(solution,grid,row)
f.close()