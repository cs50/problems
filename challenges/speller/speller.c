/**
 * Implements a spell-checker.
 * Adapted for big board testing.
 * Takes argument mode: 0 for printing words, 1 for times.
 */

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/resource.h>
#include <sys/time.h>

#include "dictionary.h"

/* stop the user from overriding anything */
#undef a
#undef after
#undef argc
#undef argv
#undef atoi
#undef b
#undef before
#undef c
#undef calculate
#undef char
#undef check
#undef const
#undef define
#undef dictionaries
#undef dictionary
#undef double
#undef else
#undef fclose
#undef ferror
#undef FILE
#undef fopen
#undef fp
#undef fread
#undef getrusage
#undef if
#undef index
#undef int
#undef isalnum
#undef isalpha
#undef isdigit
#undef load
#undef loaded
#undef main
#undef misspelled
#undef misspellings
#undef mode
#undef n
#undef printf
#undef return
#undef rusage
#undef ru_stime
#undef ru_utime
#undef size
#undef sizeof
#undef struct
#undef text
#undef time_check
#undef time_load
#undef time_size
#undef time_unload
#undef undef
#undef unload
#undef unloaded
#undef unsigned
#undef while
#undef word
#undef words

// default dictionary
#define DICTIONARY "dictionaries/large"

// prototype
double calculate(const struct rusage *b, const struct rusage *a);

int main(int argc, char *argv[])
{
    // check for correct number of args
    if (argc != 4)
    {
        printf("Usage: speller dictionary text mode\n");
        return 1;
    }

    int mode = atoi(argv[3]);

    // structs for timing data
    struct rusage before, after;

    // benchmarks
    double time_load = 0.0, time_check = 0.0, time_size = 0.0, time_unload = 0.0;

    // determine dictionary to use
    char* dictionary = argv[1];

    // load dictionary
    getrusage(RUSAGE_SELF, &before);
    bool loaded = load(dictionary);
    getrusage(RUSAGE_SELF, &after);

    // abort if dictionary not loaded
    if (!loaded)
    {
        printf("Could not load %s.\n", dictionary);
        return 1;
    }

    // calculate time to load dictionary
    time_load = calculate(&before, &after);

    // try to open text
    char *text = argv[2];
    FILE *fp = fopen(text, "r");
    if (fp == NULL)
    {
        printf("Could not open %s.\n", text);
        unload();
        return 1;
    }

    // prepare to report misspellings
    if (mode == 0)
        printf("\nMISSPELLED WORDS\n\n");

    // prepare to spell-check
    int index = 0, misspellings = 0, words = 0;
    char word[LENGTH+1];

    // spell-check each word in text
    char c;
    while (fread(&c, sizeof(char), 1, fp))
    {
        // allow only alphabetical characters and apostrophes
        if (isalpha(c) || (c == '\'' && index > 0))
        {
            // append character to word
            word[index] = c;
            index++;

            // ignore alphabetical strings too long to be words
            if (index > LENGTH)
            {
                // consume remainder of alphabetical string
                while (fread(&c, sizeof(char), 1, fp) && isalpha(c));

                // prepare for new word
                index = 0;
            }
        }

        // ignore words with numbers (like MS Word can)
        else if (isdigit(c))
        {
            // consume remainder of alphanumeric string
            while (fread(&c, sizeof(char), 1, fp) && isalnum(c));

            // prepare for new word
            index = 0;
        }

        // we must have found a whole word
        else if (index > 0)
        {
            // terminate current word
            word[index] = '\0';

            // update counter
            words++;

            // check word's spelling
            getrusage(RUSAGE_SELF, &before);
            bool misspelled = !check(word);
            getrusage(RUSAGE_SELF, &after);

            // update benchmark
            time_check += calculate(&before, &after);

            // print word if misspelled
            if (misspelled)
            {
                if (mode == 0)
                    printf("%s\n", word);
                misspellings++;
            }

            // prepare for next word
            index = 0;
        }
    }

    // check whether there was an error
    if (ferror(fp))
    {
        fclose(fp);
        printf("Error reading %s.\n", text);
        unload();
        return 1;
    }

    // close text
    fclose(fp);

    // determine dictionary's size
    getrusage(RUSAGE_SELF, &before);
    unsigned int n = size();
    getrusage(RUSAGE_SELF, &after);

    // calculate time to determine dictionary's size
    time_size = calculate(&before, &after);

    // unload dictionary
    getrusage(RUSAGE_SELF, &before);
    bool unloaded = unload();
    getrusage(RUSAGE_SELF, &after);

    // abort if dictionary not unloaded
    if (!unloaded)
    {
        printf("Could not unload %s.\n", dictionary);
        return 1;
    }

    // calculate time to unload dictionary
    time_unload = calculate(&before, &after);

    // report benchmarks
    if (mode == 0)
    {
        printf("\nWORDS MISSPELLED:     %d\n", misspellings);
        printf("WORDS IN DICTIONARY:  %d\n", n);
        printf("WORDS IN TEXT:        %d\n", words);
        printf("CANARY\n");
    }
    else
    {
        printf("%.5f\n", time_load);
        printf("%.5f\n", time_check);
        printf("%.5f\n", time_size);
        printf("%.5f\n", time_unload);
    }

    // that's all folks
    return 0;
}

/**
 * Returns number of seconds between b and a.
 */
double calculate(const struct rusage *b, const struct rusage *a)
{
    if (b == NULL || a == NULL)
    {
        return 0.0;
    }
    else
    {
        return ((((a->ru_utime.tv_sec * 1000000 + a->ru_utime.tv_usec) -
                 (b->ru_utime.tv_sec * 1000000 + b->ru_utime.tv_usec)) +
                ((a->ru_stime.tv_sec * 1000000 + a->ru_stime.tv_usec) -
                 (b->ru_stime.tv_sec * 1000000 + b->ru_stime.tv_usec)))
                / 1000000.0);
    }
}
