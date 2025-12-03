#ifndef FILEREADER_H
#define FILEREADER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char **content;
    size_t count;
} FileContent;

/**
 * Reads all lines from a file.
 * @param filename Path to the file.
 * @return FileLines Structure with all lines (must be released with freeFileLine()).
 */
FileContent readLines(const char *filename);

/**
 * Splits string into tokens.
 * @param str String.
 * @param delimiter Delimiter according to which splitting should be performed.
 * @return FileLines Structure with all lines (must be released with freeFileLine()).
 */
FileContent splitString(const char *str, const char *delimiter);

/**
 * Frees the memory of a FileLines structure.
 * @param fl Pointer to FileLines structure.
 */
void freeFileLines(FileContent *fl);

/**
 * Reads the entire file content as a string.
 * @param filename Path to the file.
 * @return Dynamically allocated string with file content (must be released with free()).
 */
char* readAll(const char *filename);

#endif // FILEREADER_H