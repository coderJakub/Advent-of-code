#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../helper/FileReader.h"

typedef unsigned long long ul;

int countAdjecent(int i, int j, char** grid, int R){
    int C = strlen(grid[0]);
    int adj = 0;
    for (int ni=i-1; ni<=i+1; ni++){
        for (int nj=j-1; nj<=j+1; nj++){
            if (ni>=0 && ni<R && nj>=0 && nj<C && (ni!=i || nj!=j) && grid[ni][nj]=='@') adj++;
        }
    }
    return adj;
}

int main(int argc, char *argv[]) {
    const char *inputFile = (argc > 1) ? argv[1] : "Day4/in.txt";
    
    FileContent lines = readLines(inputFile);
    char** grid = lines.content;
    
    int p1 = 0;
    int p2 = 0;

    int first = 1;
    while (1){
        int changes = 0;
        for(int i=0; i<lines.count; i++){
            for(int j=0; j<strlen(grid[0]); j++){
                if (grid[i][j]=='@' && countAdjecent(i, j, grid, lines.count) < 4){
                    changes = 1;
                    if(first) p1++;
                    else{
                        p2++;
                        grid[i][j] = '.';
                    }
                }
            }
        }
        first = 0;
        if(!changes)break;
    }
    
    freeFileLines(&lines);
    printf("Part 1: %d\n", p1);
    printf("Part 2: %d\n", p2);
    
    return 0;
}