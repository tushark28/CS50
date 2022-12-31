#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    //error detection
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // error detection
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    //converting string to integer
    int k = atoi(argv[1]);

    //user input for plain text
    string plain_text = get_string("plaintext: ");
    int l = strlen(plain_text);


    for (int i = 0; i < l; i++)
    {
        //for small letters
        if (plain_text[i] >= 97 && plain_text[i] <= 122)
        {
            plain_text[i] = (char)(((int)plain_text[i] - 97 + k) % 26 + 97);
        }

        //for capital letters
        else if (plain_text[i] >= 65 && plain_text[i] <= 90)
        {
            plain_text[i] = (char)(((int)plain_text[i] - 65 + k) % 26 + 65);
        }
    }

    printf("ciphertext: %s\n", plain_text);
    return 0;
}