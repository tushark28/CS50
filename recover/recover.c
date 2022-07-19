#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    FILE *input = fopen(argv[1], "r");
    BYTE buffer[512];
    while (fread(&buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {

    }

    return 0;
}