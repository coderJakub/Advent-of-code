#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../helper/FileReader.h"

typedef unsigned long long ul;

int main(int argc, char *argv[]) {
    const char *inputFile = (argc > 1) ? argv[1] : "Day6/in.txt";
    
    FileContent lines = readLines(inputFile);

    int p1 = 0;
    ul p2 = 0;

    int C = strlen(lines.content[0]);

    ul* beams = (ul*)malloc(C*sizeof(ul));
    for (int i=0; i<C; i++) beams[i] = lines.content[0][i]!='S'?0:1;

    for (int layer=1; layer<lines.count; layer++){
        ul* temp = (ul*)malloc(C*sizeof(ul));
        for (int i=0; i<C; i++) temp[i] = 0;
        for (int i=0; i<C; i++){
            if (beams[i]==0)continue;
            if (lines.content[layer][i]=='.')temp[i] += beams[i];
            else{
                p1++;
                if(i+1<C) temp[i+1] += beams[i];
                if(i-1>=0) temp[i-1] += beams[i];
            }
        }
        free(beams);
        beams = temp;
    }

    for(int i=0; i<C; i++) p2 += beams[i];
    free(beams);
    freeFileLines(&lines);

    printf("Part 1: %d\n", p1);
    printf("Part 2: %lld\n", p2);
    
    return 0;
}