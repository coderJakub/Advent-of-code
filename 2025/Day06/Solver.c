#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../helper/FileReader.h"

typedef unsigned long long ul;

int main(int argc, char *argv[]) {
    const char *inputFile = (argc > 1) ? argv[1] : "Day6/in.txt";
    
    FileContent lines = readLines(inputFile);

    ul p1 = 0;
    ul p2 = 0;

    int idx = 0;
    int R = lines.count;
    int C = strlen(lines.content[0]);
    while (idx<C){
        int start = idx;
        while (idx+1==C || idx+1<C && lines.content[R-1][idx+1] == ' ')idx++;
        char op = lines.content[R-1][start];

        ul numP1 = op=='*'?1:0;
        for (int i=0; i<R-1; i++){
            ul curr = 0;
            for (int j=start; j<idx; j++){
                char c = lines.content[i][j];
                if (c != ' ') curr = curr * 10 + (c-'0');
            }
            if (op=='*') numP1*=curr;
            else numP1+=curr;
        }

        ul numP2 = op=='*'?1:0;
        for (int j=start; j<idx; j++){
            ul curr = 0;
            for (int i=0; i<R-1; i++){
                char c = lines.content[i][j];
                if (c != ' ') curr = curr * 10 + (c-'0');
            }
            if (op=='*') numP2*=curr;
            else numP2+=curr;
        }
        p1+=numP1;
        p2+=numP2;
        idx++;
    }
    
    freeFileLines(&lines);

    printf("Part 1: %llu\n", p1);
    printf("Part 2: %llu\n", p2);
    
    return 0;
}