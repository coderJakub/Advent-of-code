#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../helper/FileReader.h"

typedef unsigned long long ul;

int solutionP1(ul** fresh, int l, FileContent ingr){
    int res = 0;
    for (int i=0; i<ingr.count; i++){
        ul id = atoll(ingr.content[i]);
        for (int j=0; j<l; j++){
            if(fresh[j][0]<=id && id<=fresh[j][1]){
                res++;
                break;
            }
        }
    }
    return res;
}

ul solutionP2(ul** fresh, int l){
    ul res = 0;
    for(int i=0; i<l; i++){
        res += fresh[i][1]-fresh[i][0]+1;
    }
    return res;
}

int comp(const void* a, const void* b){
    ul x = (*(ul**)a)[0];
    ul y = (*(ul**)b)[0];
    return (x > y) - (x < y);
}

void getSortedLongArray(FileContent stringArr, ul** intArray){
    for (int i=0; i<stringArr.count; i++){
        char* str = strdup(stringArr.content[i]);
        ul start = atoll(strtok(str, "-"));
        ul end = atoll(strtok(NULL, "-"));
        free(str);
        intArray[i][0] = start;
        intArray[i][1] = end;
    }
    qsort(intArray, stringArr.count, sizeof(ul*), comp);
}

int getDistinctIntervalls(FileContent stringArr, ul** intArray){
    ul **original = malloc(stringArr.count * sizeof(ul*));
    for (int i = 0; i < stringArr.count; i++) {
        original[i] = malloc(2 * sizeof(ul));
    }
    getSortedLongArray(stringArr, original);

    int len = 0;
    for (int i = 0; i < stringArr.count; i++) {
        if (len > 0 && intArray[len-1][1] >= original[i][0]) {
            if (original[i][1] > intArray[len-1][1])
                intArray[len-1][1] = original[i][1];
        }
        else {
            intArray[len][0] = original[i][0];
            intArray[len][1] = original[i][1];
            len++;
        }
    }
    for (int i = 0; i < stringArr.count; i++)
        free(original[i]);
    free(original);

    return len;
}

int main(int argc, char *argv[]) {
    const char *inputFile = (argc > 1) ? argv[1] : "Day5/in.txt";
    
    FileContent fresh = readBlock(inputFile, 0);
    FileContent ingr = readBlock(inputFile, 1);

    ul **intArray = malloc(fresh.count * sizeof(ul*));
    for (int i = 0; i < fresh.count; i++) {
        intArray[i] = malloc(2 * sizeof(ul));
    }
    int l = getDistinctIntervalls(fresh, intArray);

    int p1 = solutionP1(intArray, l, ingr);
    ul p2 = solutionP2(intArray, l);
    
    freeFileLines(&fresh);
    freeFileLines(&ingr);
    for (int i = 0; i < fresh.count; i++)
        free(intArray[i]);
    free(intArray);
    printf("Part 1: %d\n", p1);
    printf("Part 2: %llu\n", p2);
    
    return 0;
}