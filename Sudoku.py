import pygame
import subprocess

class Sudoku:
    def __init__(self):
        '''self.board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                       [6, 0, 0, 1, 9, 5, 0, 0, 0],
                       [0, 9, 8, 0, 0, 0, 0, 6, 0],
                       [8, 0, 0, 0, 6, 0, 0, 0, 3],
                       [4, 0, 0, 8, 0, 3, 0, 0, 1],
                       [7, 0, 0, 0, 2, 0, 0, 0, 6],
                       [0, 6, 0, 0, 0, 0, 2, 8, 0],
                       [0, 0, 0, 4, 1, 9, 0, 0, 5],
                       [0, 0, 0, 0, 8, 0, 0, 7, 9]]'''
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

'''file scope lol'''
s = Sudoku()

''' Checks if the array contains duplicates '''
def checkArray(arr):
    if(sum(arr) > 45):
        return False
    arr2 = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(arr)):
        if(arr2[arr[i]] == 1):
            return False
        arr2[arr[i]] += 1
    return True


''' Creates an array for the vertical column that is specified '''
def createArrFromVertical(x):
    arr = []
    for i in range(9):
        arr.append(s.board[i][x])
    return arr

''' Creates an array for the block that contains the coordinates '''
def createArrFromBlock(x, y):
    newX = int(x/3)*3
    newY = int(y/3)*3
    arr = []
    for i in range(3):
        for j in range(3):
            arr.append(s.board[newY+i][newX+j])
    return arr

''' Solves the sudoku puzzle '''
def solve(x, y, screen, depth):
    ''' First check if the current place satisfies the sudoku rules.
        Then if both x and y are 8 this sudoku is solved so return True.
        then increment x and y to get to the next space in the board.
        Then iterate through the possible values of the current spot
        and recursivly call the solve function. '''
    ''' This might not work if the first entry is empty in the double array-----------------------------------------------------'''
    if(checkArray(s.board[y]) and checkArray(createArrFromVertical(x)) and checkArray(createArrFromBlock(x, y))):
        if(x == 8 and y == 8):
            return True
        else:
            ''' These are the new values in the board that are going to be chosen '''
            newX = x + 1
            newY = y
            if(newX > 8):
                newY += 1
                newX = 0
            if(newY > 8 or newX > 8):
                return True
            while(s.board[newY][newX] != 0):
                if(newX == 8):
                    newX = -1
                    newY += 1
                newX += 1
                if(newY > 8 or newX > 8):
                    return True
            for i in range(9):
                s.board[newY][newX] = i+1
                createWindow(screen)
                if(solve(newX, newY, screen, depth + 1)):
                    return True
            ''' need to set it to 0 because it went through all of the possibilities and needs to go back '''
            s.board[newY][newX] = 0
            return False
    else:
        ''' need to set it to 0 because this configuration doesn't work '''
        s.board[y][x] = 0
        return False

def createWindow(screen):
    screen.fill((127, 127, 127))
    font = pygame.font.SysFont('arial', 100)
    '''Displays a number on that tile'''
    for i in range(10):
        if(i % 3 == 0):
            weight = 5
        else:
            weight = 1
        pygame.draw.line(screen, (255, 255, 255), (0+92*i, 0), (0+92*i, 828), weight)
        pygame.draw.line(screen, (255, 255, 255), (0, 0+92*i), (828, 0+92*i), weight)
        if(i < 9):
            for j in range(9):
                if(s.board[i][j] != 0):
                    screen.blit(font.render(
                        str(s.board[i][j]), True, (0, 0, 0)), (23+j*92, i*92-10))
    
    pygame.display.update()

def main():
    pygame.init()
    '''Original size was 828 x 828'''
    size = 832, 832
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if(count == 0):
                    solve(0, 0, screen, 0)
                    count += 1
                elif(count == 1):
                    subprocess.call("python3 SudokuV2.py", shell=True)
                    quit()
                else:
                    createWindow(screen)


if __name__ == "__main__":
    main()
