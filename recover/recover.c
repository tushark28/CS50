#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    FILE *input = fopen(argv[1], "r");
    BYTE buffer[BLOCK_SIZE];
    int jpegflag = 0;
    while (fread(&buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {
        if(buffer[0]==0xff && buffer[1]==0xd8 && buffer[2]==0xff && (buffer[3] & 0xf0) == 0xe0){
            if(jpegflag==0){
                char filename[8];
                sprintf(filename,"%03i.jpg",jpegflag);
                FILE* output = fopen(filename,"w");
                fwrite(&buffer,1,BLOCK_SIZE,output);
            }
        }
    }

    return 0;
}