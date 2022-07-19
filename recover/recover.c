#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    FILE *input = fopen(argv[1], "r");
    BYTE buffer[BLOCK_SIZE];
    while (fread(&buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {
        if(buffer[0]==0xff && buffer[1]==0xd8 && buffer[2]==0xff && (buffer[3] & 0xf0) == 0xe0){
            
        }
    }

    return 0;
}