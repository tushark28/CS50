#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    // Get user input
    string text = get_string("Text: ");

    float s = 0;
    float w = 1; // Initialize to 1 because it will not gonna count 1st word
    float l = 0;

    // Iterate over text
    for (int i = 0; i < strlen(text); i++)
    {
        // Check for sentences
        if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            s++;
        }

        // Check for words
        if (text[i] == ' ')
        {
            w++;
        }

        // Check for letters
        if (islower(text[i]) || isupper(text[i]))
        {
            l++;
        }
    }

    float L = 100 * l / w; // L is Number of letters per 100 words
    float S = 100 * s / w; // S is Number of sentences per 100 words

    // Formula to get grade
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }

    return 0;
}