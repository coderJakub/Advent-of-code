#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../helper/FileReader.h"

typedef unsigned long long ul;

int solutionP1(FileContent fresh, FileContent ingr){
    int res = 0;
    for (int i=0; i<ingr.count; i++){
        ul id = atoll(ingr.content[i]);
        for (int j=0; j<fresh.count; j++){
            char *str_copy = strdup(fresh.content[j]);
            ul start = atoll(strtok(str_copy, "-"));
            ul end = atoll(strtok(NULL, "-"));
            if(start<=id && id<=end){
                res++;
                break;
            }
        }
    }
    return res;
}

int main(int argc, char *argv[]) {
    const char *inputFile = (argc > 1) ? argv[1] : "Day5/in.txt";
    
    FileContent fresh = readBlock(inputFile, 0);
    FileContent ingr = readBlock(inputFile, 1);


    int p1 = solutionP1(fresh, ingr);
    int p2 = 0;
    
    freeFileLines(&fresh);
    freeFileLines(&ingr);
    printf("Part 1: %d\n", p1);
    printf("Part 2: %d\n", p2);
    
    return 0;
}