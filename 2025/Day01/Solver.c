#include <stdio.h>
#include <stdlib.h>
#include "../helper/FileReader.h"

int main(int argc, char *argv[]) {
    const char *inputFile = (argc > 1) ? argv[1] : "Day1/in.txt";
    
    FileContent lines = readLines(inputFile);
    
    int dial = 50;
    unsigned long p1 = 0;
    unsigned long p2 = 0;

    for (int i = 0; i < lines.count; i++) {
        int amount = atoi(lines.content[i]+1);
        int inc = lines.content[i][0]=='R' ? 1 : -1;
        dial += inc*amount;
        p2 += abs(dial/100) + (dial <= 0 && dial !=-amount);
        dial = ( (dial%100) + 100) % 100;
        p1 += (dial==0);
    }
    
    freeFileLines(&lines);
    printf("Part 1: %u\n", p1);
    printf("Part 2: %u\n", p2);
    
    return 0;
}