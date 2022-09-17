#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    // Get user input
    string u_input = get_string("Text: ");

    float sentences = 0;
    float words = 1; // Initialized to 1 otherwise it will not count the 1st word
    float letters = 0;

    // Iterate over the user input
    for (int i = 0; i < strlen(u_input); i++)
    {
        
        if (u_input[i] == '!' || u_input[i] == '.' || u_input[i] == '?')
        {
            sentences++;
        }

        if (u_input[i] == ' ')
        {
            words++;
        }

        if (islower(u_input[i]) || isupper(u_input[i]))
        {
            letters++;
        }
    }

    float L = 100 * letters / words;   // L = Number of letters per 100 words
    float S = 100 * sentences / words; // S = Number of sentences per 100 words

    // Formula for evaluating grade
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