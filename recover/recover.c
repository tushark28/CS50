#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    //If no argument for forensic image is given as input
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    //Opening forensic file
    FILE *input = fopen(argv[1], "r");

    //If forensic file is empty
    if (input == NULL)
    {
        printf("Empty forensic image");
        return 1;
    }

    //buffer for each 512 bytes block
    BYTE buffer[BLOCK_SIZE];
    int jpgflag = 0, jpgcounter = -1;
    FILE *output;

    //looping through every 512 bytes till no 512 block is left.
    while (fread(&buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {
        //if the starting 4 bytes is a header of a jpg file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //if a file is already on write
            if (jpgflag != 0)
            {
                fclose(output);
            }
            char filename[8];
            jpgcounter++;
            sprintf(filename, "%03i.jpg", jpgcounter);
            output = fopen(filename, "w");
            fwrite(&buffer, 1, BLOCK_SIZE, output);
            jpgflag = 1;
        }

        else
        {
            //if a file is already on write
            if (jpgflag != 0)
            {
                fwrite(&buffer, 1, BLOCK_SIZE, output);
            }
        }
    }

    fclose(output);
    fclose(input);
    return 0;
}