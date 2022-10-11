#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc != 3)
    {
        return 1;
    }

    // Determine which test to run
    int setup = atoi(argv[1]);
    int test = atoi(argv[2]);

    // Setup
    switch (setup)
    {
        case 0:
            candidate_count = 3;
            candidates[0].name = "Alice";
            candidates[0].votes = 0;
            candidates[1].name = "Bob";
            candidates[1].votes = 0;
            candidates[2].name = "Charlie";
            candidates[2].votes = 0;
            break;
    }

    // Test

    char alice[] = "Alice";
    char bob[] = "Bob";
    char charlie[] = "Charlie";
    char david[] = "David";

    switch(test)
    {
        case 0:
            printf("%s", vote(alice) ? "true" : "false");
            break;

        case 1:
            printf("%s", vote(bob) ? "true" : "false");
            break;

        case 2:
            printf("%s", vote(charlie) ? "true" : "false");
            break;

        case 3:
            printf("%s", vote(david) ? "true" : "false");
            break;

        case 4:
            vote(alice);
            printf("%i %i %i", candidates[0].votes, candidates[1].votes, candidates[2].votes);
            break;

        case 5:
            candidates[0].votes = 2;
            candidates[1].votes = 7;
            candidates[2].votes = 0;
            vote(bob);
            printf("%i %i %i", candidates[0].votes, candidates[1].votes, candidates[2].votes);
            break;

        case 6:
            candidates[0].votes = 2;
            candidates[1].votes = 8;
            candidates[2].votes = 0;
            vote(david);
            printf("%i %i %i", candidates[0].votes, candidates[1].votes, candidates[2].votes);
            break;

        case 7:
            candidates[0].votes = 8;
            candidates[1].votes = 2;
            candidates[2].votes = 0;
            print_winner();
            break;

        case 8:
            candidates[0].votes = 1;
            candidates[1].votes = 8;
            candidates[2].votes = 2;
            print_winner();
            break;

        case 9:
            candidates[0].votes = 1;
            candidates[1].votes = 8;
            candidates[2].votes = 9;
            print_winner();
            break;

        case 10:
            candidates[0].votes = 8;
            candidates[1].votes = 8;
            candidates[2].votes = 5;
            print_winner();
            break;

        case 11:
            candidates[0].votes = 8;
            candidates[1].votes = 8;
            candidates[2].votes = 8;
            print_winner();
            break;
    }
}
