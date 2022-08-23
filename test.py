import ctypes

NineIntegers = ctypes.c_int * 9
DP = NineIntegers * 9

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board2 = DP()

for i in range(9):
    board[i] = NineIntegers()
    for j in range(9):
        board2[i][j] = board[i][j]


'''board2 = [NineIntegers(5, 3, 0, 0, 7, 0, 0, 0, 0),
            NineIntegers(6, 0, 0, 1, 9, 5, 0, 0, 0),
            NineIntegers(0, 9, 8, 0, 0, 0, 0, 6, 0),
            NineIntegers(8, 0, 0, 0, 6, 0, 0, 0, 3),
            NineIntegers(4, 0, 0, 8, 0, 3, 0, 0, 1),
            NineIntegers(7, 0, 0, 0, 2, 0, 0, 0, 6),
            NineIntegers(0, 6, 0, 0, 0, 0, 2, 8, 0),
            NineIntegers(0, 0, 0, 4, 1, 9, 0, 0, 5),
            NineIntegers(0, 0, 0, 0, 8, 0, 0, 7, 9)]'''


lib = ctypes.PyDLL("libtrial.dylib")

for i in range(9):
    lib.printArr(board2[i])
