#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../helper/FileReader.h"

typedef unsigned long long ul;

void getMaxValue(char* line, int start, int end, int* res){
    for (int idx = start; idx < end; idx++){
        int num = line[idx]-'0';
        if (num > res[0]){
            res[0] = num;
            res[1] = idx;
        }
    }
}

int main(int argc, char *argv[]) {
    const char *inputFile = (argc > 1) ? argv[1] : "Day2/in.txt";
    
    FileContent lines = readLines(inputFile);
    
    int dial = 50;
    ul res[2] = {0,0};

    for (int i = 0; i < lines.count; i++) {
        for (int p = 0; p < 2; p++){
            ul num = 0;
            int numL = p==0 ? 1 : 11;
            int start = 0;
            for (int end = numL; end >= 0; end--){
                int maxVal[2] = {0, 0};
                getMaxValue(lines.content[i], start, strlen(lines.content[i])-end, maxVal);
                num = num*10+maxVal[0];
                start = maxVal[1]+1;
            }
            res[p] += num;
        }
    }
    
    freeFileLines(&lines);
    printf("Part 1: %llu\n", res[0]);
    printf("Part 2: %llu\n", res[1]);
    
    return 0;
}