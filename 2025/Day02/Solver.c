#include <stdio.h>
#include <stdlib.h>
#include "../helper/FileReader.h"

int invalidP1(char* id, int len){
    if (len%2 != 0) return 0;
    for(int i=0; i<len/2; i++){
        if (id[i] != id[len/2+i]) return 0;
    }
    return 1;
}

int invalidP2(char* id, int len){
    for(int chunkSize=1; chunkSize<=len/2; chunkSize++){
        if (len % chunkSize != 0) continue;
        
        int valid = 1;
        for (int i=chunkSize; i<len; i++){
            if (id[i] != id[i % chunkSize]){
                valid = 0;
                break;
            }
        }
        if (valid) return 1;
    }
    return 0;
}

int main(int argc, char *argv[]) {
    const char *inputFile = (argc > 1) ? argv[1] : "Day1/in.txt";
    
    const char* lines = readAll(inputFile);
    FileContent ranges = splitString(lines, ",");
    
    unsigned long long p1 = 0;
    unsigned long long p2 = 0;

    for (int i = 0; i < ranges.count; i++) {
        FileContent parts = splitString(ranges.content[i], "-");
        long long start = strtoll(parts.content[0], NULL, 10);
        long long end = strtoll(parts.content[1], NULL, 10);
        
        for (long long id=start; id <= end; id++){
            int len = snprintf(NULL, 0, "%lld", id);
            char *str = malloc(len + 1);
            snprintf(str, len + 1, "%lld", id);
            if (invalidP1(str, len)) p1 += id;
            if (invalidP2(str, len)) p2 += id;
            free(str);
        }
    }
    
    freeFileLines(&ranges);
    printf("Part 1: %llu\n", p1);
    printf("Part 2: %llu\n", p2);
    
    return 0;
}