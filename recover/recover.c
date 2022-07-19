#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Empty forensic image");
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];
    int jpegflag = 0, jpegcounter = -1;
    FILE *output;
    while (fread(&buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (jpegflag != 0)
            {
                fclose(output);
            }
            char filename[8];
            jpegcounter++;
            sprintf(filename, "%03i.jpg", jpegcounter);
            output = fopen(filename, "w");
            fwrite(&buffer, 1, BLOCK_SIZE, output);
            jpegflag = 1;
        }

        else
        {
            if (jpegflag != 0)
            {
                fwrite(&buffer, 1, BLOCK_SIZE, output);
            }
        }
    }

    fclose(output);
    fclose(input);
    return 0;
}