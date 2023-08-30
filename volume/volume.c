#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./music input.wav output.wav factor");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    FILE *output = fopen(argv[2], "w");
    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

    // TODO: Read data from input file and write updated data to output file

    // Close files
    fclose(input);
    fclose(output);
}
