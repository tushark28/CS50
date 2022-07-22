// Implements a dictionary's functionality

#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
unsigned int count = 0;
// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int hash_place = hash(word);
    node *head = table[hash_place];
    while (head != NULL)
    {
        if (strcasecmp(head->word, word) == 0)
        {
            return true;
        }
        head = head->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dic = fopen(dictionary, "r");
    if (dic == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(dic, "%s", word) != EOF)
    {
        unsigned int hash_place = hash(word);
        node *ptr = (node *)malloc(sizeof(node));
        if (ptr == NULL)
        {
            return false;
        }

        strcpy(ptr->word, word);
        node *head = table[hash_place];
        ptr->next = head;
        table[hash_place] = ptr;
        count++;
    }
    fclose(dic);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int loopcount=0;
    for (int i = 0; i < N; i++)
    {
        node* head = table[i];
        while (head != NULL)
        {
            node* wastage = head;
            head=head->next;
            free(wastage);
            loopcount++;
        }

    }
    if(count==loopcount){
        return true;
    }
    return false;

}
