#include <stdlib.h>
#include <stdio.h>
#include "Brains.h"

int sudoku[9][9] = { { 5, 3, 0, 0, 7, 0, 0, 0, 0 },
                     { 6, 0, 0, 1, 9, 5, 0, 0, 0 },
                     { 0, 9, 8, 0, 0, 0, 0, 6, 0 },
                     { 8, 0, 0, 0, 6, 0, 0, 0, 3 },
                     { 4, 0, 0, 8, 0, 3, 0, 0, 1 },
                     { 7, 0, 0, 0, 2, 0, 0, 0, 6 },
                     { 0, 6, 0, 0, 0, 0, 2, 8, 0 },
                     { 0, 0, 0, 4, 1, 9, 0, 0, 5 },
                     { 0, 0, 0, 0, 8, 0, 0, 7, 9 } };

void printString(char *string)
{
    printf("%s\n", string);
}

int checkArr(int *arr)
{
    int buf[10] = {100, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for(int i = 0; i < 9; i++) {
        if(buf[arr[i]] == 1) {
            return 0;
        }
        buf[arr[i]] += 1;
    }
    return 1;
}

void printArr(int *arr)
{
    printf("[");
    for(int j = 0; j < 9; j++) {
        printf("%d ", arr[j]);
    }
    printf("]\n");
}

void testSudoku(int *test, int j)
{
    for(int i = 0; i < 9; i++) {
        sudoku[j][i] = test[i];
    }
}
