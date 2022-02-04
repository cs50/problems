#include <cs50.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    string test = argv[1];

    if (strcmp(test, "get_guess") == 0)
    {
        printf("%s", get_guess(5));
    }
    else if (strcmp(test, "check_word") == 0)
    {
        int status[5] = {0};
        printf("%i", check_word(argv[2], 5, status, argv[3]));
    }
}