#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        // Input of Pyramid Height
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Loop for Rows
    for (int i = 0; i < height; i++)
    {
        // Loop for Spaces
        for (int space = 0; space < height - i - 1; space++)
        {
            printf(" ");
        }
        // Loop for Hash Symbols
        for (int hash = 0; hash < i + 1; hash++)
        {
            printf("#");
        }

        // Bridge Space
        printf("  ");

        // Loop for Hash Symbols
        for (int hash = 0; hash < i + 1; hash++)
        {
            printf("#");
        }

        printf("\n");
    }
    return 0;
}