#include <stdio.h>

#include "wav.h"
#include "helpers.h"

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: duration FRACTION\n");
        return 1;
    }

    int length = duration(argv[1]);
    printf("%i\n", length);
}
