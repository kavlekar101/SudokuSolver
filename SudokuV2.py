import pygame
import ctypes
import time


DP = ctypes.POINTER(ctypes.c_int16 * 9 * 9)


class Test(ctypes.Structure):
    _fields_ = [
        ("matrix", DP), 
                ("row", ctypes.POINTER(ctypes.c_int16 * 9)), 
    ]

class Sudoku:
    def __init__(self):
        self.board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                       [6, 0, 0, 1, 9, 5, 0, 0, 0],
                       [0, 9, 8, 0, 0, 0, 0, 6, 0],
                       [8, 0, 0, 0, 6, 0, 0, 0, 3],
                       [4, 0, 0, 8, 0, 3, 0, 0, 1],
                       [7, 0, 0, 0, 2, 0, 0, 0, 6],
                       [0, 6, 0, 0, 0, 0, 2, 8, 0],
                       [0, 0, 0, 4, 1, 9, 0, 0, 5],
                       [0, 0, 0, 0, 8, 0, 0, 7, 9]]


'''file scope lol'''
s = Sudoku()

grey = (127, 127, 127)

''' Checks if the array contains duplicates '''
def checkArray(arr):
    arr2 = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(arr)):
        if arr2[arr[i]] == 1:
            return False
        arr2[arr[i]] += 1
    return True


''' Creates an array for the block that contains the coordinates '''
def createArrFromBlock(x, y):
    newX = x//3*3
    newY = y//3*3
    arr = []
    for i in range(3):
        for j in range(3):
            arr.append(s.board[newY+i][newX+j])
    return arr

''' Solves the sudoku '''
def solve(x, y, screen, depth):
    ''' First check if the current place satisfies the sudoku rules.
        Then if both x and y are 8 this sudoku is solved so return True.
        then increment x and y to get to the next space in the board.
        Then iterate through the possible values of the current spot
        and recursivly call the solve function. '''
    ''' This might not work if the first entry is empty in the double array-----------------------------------------------------'''
    if(s.board[y][x] == 0):
        newX = x + 1
        newY = y
        if(newX > 8):
            newX = 0
            newY += 1
        if(newY > 8):
            for i in range(9):
                s.board[y][x] = i + 1
                """drawSquare(screen, x, y, i + 1, True)"""
                if(checkArray(s.board[y]) and checkArray(s.board[:][x]) and checkArray(createArrFromBlock(x, y))):
                    return True
            s.board[y][x] = 0
            drawSquare(screen, x, y, 0)
            return False
        for i in range(9):
            s.board[y][x] = i + 1
            """drawSquare(screen, x, y, i + 1, True)"""
            if(checkArray(s.board[y]) and checkArray(s.board[:][x]) and checkArray(createArrFromBlock(x, y))):
                if(solve(newX, newY, screen, depth + 1)):
                    return True
        s.board[y][x] = 0
        '''drawSquare(screen, x, y, 0)'''
        return False
    else:
        newX = x + 1
        newY = y
        if(newX > 8):
            newX = 0
            newY += 1
        if(newY > 8):
            return True
        else:
            return solve(newX, newY, screen, depth + 1)

def drawSquare(screen, x, y, num, notZero=False):
    font = pygame.font.SysFont('arial', 100)
    pygame.draw.rect(screen, grey, pygame.Rect(5+92*x, 5+92*y, 85, 85))
    if(notZero):
        screen.blit(font.render(
            str(num), True, (0, 255, 0)), (23+x*92, y*92-10))
    pygame.display.update(pygame.Rect(92*x, 92*y, 92, 92))


def createWindow(screen):
    screen.fill(grey)
    font = pygame.font.SysFont('arial', 100)
    '''Displays a number on that tile'''
    for i in range(10):
        if(i % 3 == 0):
            weight = 5
        else:
            weight = 1
        pygame.draw.line(screen, (255, 255, 255), (92*i, 0), (92*i, 828), weight)
        pygame.draw.line(screen, (255, 255, 255), (0, 92*i), (828, 92*i), weight)
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
                    createWindow(screen)
                    start = time.time()
                    print(solve(0, 0, screen, 0))
                    end = time.time()
                    print(end - start)
                    count += 1
                else:
                    createWindow(screen)


if __name__ == "__main__":
    main()
