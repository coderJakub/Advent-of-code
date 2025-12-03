#include "FileReader.h"

#define INITIAL_CAPACITY 100

FileContent readLines(const char *filename) {
    FileContent result = {NULL, 0};
    char *content = readAll(filename);
    if (!content) {
        return result;
    }
    
    result = splitString(content, "\r\n");
    
    free(content);
    return result;
}

FileContent splitString(const char *str, const char *delimiter) {
    FileContent result = {NULL, 0};
    
    if (!str) {
        return result;
    }
    
    // Create a copy of the string (since strtok modifies it)
    char *str_copy = strdup(str);
    if (!str_copy) {
        fprintf(stderr, "memory error\n");
        return result;
    }
    
    // Initial capacity for token array
    size_t capacity = INITIAL_CAPACITY;
    result.content = malloc(capacity * sizeof(char*));
    
    if (!result.content) {
        fprintf(stderr, "memory error\n");
        free(str_copy);
        return result;
    }
    
    // Split string into tokens
    char *token = strtok(str_copy, delimiter);
    while (token != NULL) {
        // Increase capacity if necessary
        if (result.count >= capacity) {
            capacity *= 2;
            char **temp = realloc(result.content, capacity * sizeof(char*));
            if (!temp) {
                fprintf(stderr, "Memory error when enlarging\n");
                freeFileLines(&result);
                free(str_copy);
                result.count = 0;
                return result;
            }
            result.content = temp;
        }
        
        // Copy token (remove whitespace if desired)
        // Remove leading spaces
        while (*token == ' ' || *token == '\t') {
            token++;
        }
        
        result.content[result.count] = strdup(token);
        if (!result.content[result.count]) {
            fprintf(stderr, "Memory error during copying\n");
            freeFileLines(&result);
            free(str_copy);
            result.count = 0;
            return result;
        }
        
        result.count++;
        token = strtok(NULL, delimiter);
    }
    
    free(str_copy);
    return result;
}


void freeFileLines(FileContent *fl) {
    if (fl && fl->content) {
        for (size_t i = 0; i < fl->count; i++) {
            free(fl->content[i]);
        }
        free(fl->content);
        fl->content = NULL;
        fl->count = 0;
    }
}
char* readAll(const char *filename) {
    FILE *file = fopen(filename, "rb");
    
    if (!file) {
        fprintf(stderr, "Error opening the file: %s\n", filename);
        return NULL;
    }
    
    // Determine file size
    fseek(file, 0, SEEK_END);
    long size = ftell(file);
    fseek(file, 0, SEEK_SET);
    
    // Allocate memory
    char *content = malloc(size + 1);
    if (!content) {
        fprintf(stderr, "memory error\n");
        fclose(file);
        return NULL;
    }
    
    // Read file
    size_t read_size = fread(content, 1, size, file);
    content[read_size] = '\0';
    
    fclose(file);
    return content;
}