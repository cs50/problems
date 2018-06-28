#include <stdio.h>

#include "helpers.h"
#include "wav.h"

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: is_rest LINE\n");
        return 2;
    }

    // Check output of to_rest
    return is_rest(argv[1]);
}
