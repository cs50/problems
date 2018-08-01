/**
 * Prompts user for as many as MAX values until EOF is reached,
 * then prints the values in sorted order. Used to test `sort`.
 *
 * Usage: ./sort
 *
 */

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

#include "helpers.h"

// maximum amount of hay
const int MAX = 65536;

int main(int argc, string argv[])
{
    fprintf(stderr, "RUNNING SORT\n");
    // fill haystack
    int size;
    int haystack[MAX];
    for (size = 0; size < MAX; size++)
    {
        // wait for hay until EOF
        int straw = get_int("item: ");
        if (straw == INT_MAX)
        {
            break;
        }

        // add hay to stack
        haystack[size] = straw;
    }
    printf("\n");

    // sort the haystack
    sort(haystack, size);

    // print the haystack, one item per line
    for (int i = 0; i < size; i++)
    {
        printf("%i\n", haystack[i]);
    }
}
