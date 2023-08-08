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
            voter_count = 5;
            candidate_count = 3;
            candidates[0].name = "Alice";
            candidates[0].votes = 0;
            candidates[0].eliminated = false;
            candidates[1].name = "Bob";
            candidates[1].votes = 0;
            candidates[1].eliminated = false;
            candidates[2].name = "Charlie";
            candidates[2].votes = 0;
            candidates[2].eliminated = false;
            break;

        case 1:
            voter_count = 7;
            candidate_count = 4;
            candidates[0].name = "Alice";
            candidates[0].votes = 0;
            candidates[0].eliminated = false;
            candidates[1].name = "Bob";
            candidates[1].votes = 0;
            candidates[1].eliminated = false;
            candidates[2].name = "Charlie";
            candidates[2].votes = 0;
            candidates[2].eliminated = false;
            candidates[3].name = "David";
            candidates[3].votes = 0;
            candidates[3].eliminated = false;
            preferences[0][0] = preferences[1][0] = 0;
            preferences[0][1] = preferences[1][1] = 1;
            preferences[0][2] = preferences[1][2] = 2;
            preferences[0][3] = preferences[1][3] = 3;
            preferences[2][0] = preferences[3][0] = preferences[4][0] = 1;
            preferences[2][1] = preferences[3][1] = preferences[4][1] = 3;
            preferences[2][2] = preferences[3][2] = preferences[4][2] = 0;
            preferences[2][2] = preferences[3][2] = preferences[4][2] = 2;
            preferences[5][0] = 2;
            preferences[5][1] = 1;
            preferences[5][2] = 3;
            preferences[5][3] = 0;
            preferences[6][0] = 0;
            preferences[6][1] = 2;
            preferences[6][2] = 1;
            preferences[6][3] = 3;
            break;

        case 2:
            voter_count = 28;
            candidate_count = 4;
            candidates[0].name = "Alice";
            candidates[0].votes = 8;
            candidates[0].eliminated = false;
            candidates[1].name = "Bob";
            candidates[1].votes = 15;
            candidates[1].eliminated = false;
            candidates[2].name = "Charlie";
            candidates[2].votes = 4;
            candidates[2].eliminated = false;
            candidates[3].name = "David";
            candidates[3].votes = 1;
            candidates[3].eliminated = false;
            break;
    }

    // Test
    switch(test)
    {
        case 0:
            printf("%s", vote(0, 0, "Bob") ? "true" : "false");
            break;

        case 1:
            printf("%s", vote(1, 2, "David") ? "true" : "false");
            break;

        case 2:
            vote(0, 0, "Charlie");
            printf("%i", preferences[0][0]);
            break;

        case 3:
            vote(1, 2, "Alice");
            printf("%i", preferences[1][2]);
            break;

        case 4:
            vote(1, 0, "Bob");
            vote(1, 1, "Alice");
            vote(1, 2, "Charlie");
            printf("%i %i %i", preferences[1][0], preferences[1][1], preferences[1][2]);
            break;

        case 5:
            tabulate();
            for (int i = 0; i < candidate_count; i++)
                printf("%i ", candidates[i].votes);
            break;

        case 6:
            candidates[3].eliminated = true;
            tabulate();
            for (int i = 0; i < candidate_count; i++)
                printf("%i ", candidates[i].votes);
            break;

        case 7:
            candidates[2].eliminated = true;
            candidates[3].eliminated = true;
            tabulate();
            for (int i = 0; i < candidate_count; i++)
                printf("%i ", candidates[i].votes);
            break;

        case 8:
            print_winner();
            break;

        case 9:
            printf("%s", print_winner() ? "true" : "false");
            break;

        case 10:
            candidates[0].votes = 11;
            candidates[1].votes = 12;
            printf("%s", print_winner() ? "true" : "false");
            break;

        case 11:
            candidates[0].votes = 9;
            candidates[1].votes = 14;
            printf("%s", print_winner() ? "true" : "false");
            break;

        case 12:
            printf("%i", find_min());
            break;

        case 13:
            candidates[0].votes = 7;
            candidates[1].votes = 7;
            candidates[2].votes = 7;
            candidates[3].votes = 7;
            printf("%i", find_min());
            break;

        case 14:
            candidates[3].eliminated = true;
            printf("%i", find_min());
            break;

        case 15:
            candidates[0].votes = 7;
            candidates[1].votes = 7;
            candidates[2].votes = 7;
            candidates[3].votes = 7;
            printf("%s", is_tie(7) ? "true" : "false");
            break;

        case 16:
            candidates[0].votes = 5;
            candidates[1].votes = 6;
            candidates[2].votes = 8;
            candidates[3].votes = 9;
            printf("%s", is_tie(5) ? "true" : "false");
            break;

        case 17:
            candidates[0].votes = 6;
            candidates[1].votes = 6;
            candidates[2].votes = 8;
            candidates[3].votes = 8;
            printf("%s", is_tie(6) ? "true" : "false");
            break;

        case 18:
            candidates[0].votes = 14;
            candidates[1].votes = 14;
            candidates[2].votes = 0;
            candidates[3].votes = 0;
            candidates[2].eliminated = true;
            candidates[3].eliminated = true;
            printf("%s", is_tie(14) ? "true" : "false");
            break;

        case 19:
            eliminate(1);
            for (int i = 0; i < candidate_count; i++)
                printf("%s ", candidates[i].eliminated ? "true" : "false");
            break;

        case 20:
            candidates[0].votes = 6;
            candidates[1].votes = 8;
            candidates[2].votes = 6;
            candidates[3].votes = 8;
            eliminate(6);
            for (int i = 0; i < candidate_count; i++)
                printf("%s ", candidates[i].eliminated ? "true" : "false");
            break;

        case 21:
            candidates[0].votes = 5;
            candidates[0].eliminated = true;
            candidates[1].votes = 10;
            candidates[2].votes = 6;
            candidates[3].votes = 7;
            eliminate(6);
            for (int i = 0; i < candidate_count; i++)
                printf("%s ", candidates[i].eliminated ? "true" : "false");
            break;

        // additional tabulate check
        case 22:
            preferences[5][1] = 3;
            preferences[5][2] = 1;
            candidates[2].eliminated = true;
            candidates[3].eliminated = true;
            tabulate();
            for (int i = 0; i < candidate_count; i++)
                printf("%i ", candidates[i].votes);
            break;

    }
}
