#include <stdio.h>

#include "helpers.h"
#include "wav.h"

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: frequency NOTE\n");
        return 1;
    }

    int freq = frequency(argv[1]);
    printf("%i\n", freq);
}
