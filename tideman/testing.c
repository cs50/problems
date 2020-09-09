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
            candidates[0] = "Alice";
            candidates[1] = "Bob";
            candidates[2] = "Charlie";
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    preferences[i][j] = 0;
            break;

        case 1:
            candidate_count = 3;
            preferences[0][0] = 0;
            preferences[0][1] = 5;
            preferences[0][2] = 6;
            preferences[1][0] = 4;
            preferences[1][1] = 0;
            preferences[1][2] = 4;
            preferences[2][0] = 3;
            preferences[2][1] = 5;
            preferences[2][2] = 0;
            break;

        case 2:
            candidate_count = 3;
            preferences[0][0] = 0;
            preferences[0][1] = 6;
            preferences[0][2] = 8;
            preferences[1][0] = 6;
            preferences[1][1] = 0;
            preferences[1][2] = 3;
            preferences[2][0] = 4;
            preferences[2][1] = 9;
            preferences[2][2] = 0;
            break;

        case 3:
            candidate_count = 3;
            pair_count = 3;
            preferences[0][0] = 0;
            preferences[0][1] = 6;
            preferences[0][2] = 7;
            preferences[1][0] = 3;
            preferences[1][1] = 0;
            preferences[1][2] = 4;
            preferences[2][0] = 2;
            preferences[2][1] = 5;
            preferences[2][2] = 0;
            pairs[0].winner = 0;
            pairs[0].loser = 1;
            pairs[1].winner = 0;
            pairs[1].loser = 2;
            pairs[2].winner = 2;
            pairs[2].loser = 1;
            break;

        case 4:
            candidate_count = 4;
            candidates[0] = "Alice";
            candidates[1] = "Bob";
            candidates[2] = "Charlie";
            candidates[3] = "David";
            break;

        case 5:
            candidate_count = 5;
            candidates[0] = "Alice";
            candidates[1] = "Bob";
            candidates[2] = "Charlie";
            candidates[3] = "David";
            candidates[4] = "Erin";
            break;

        case 6:
            candidate_count = 6;
            candidates[0] = "Alice";
            candidates[1] = "Bob";
            candidates[2] = "Charlie";
            candidates[3] = "David";
            candidates[4] = "Eric";
            candidates[5] = "Frank";
            break;
    }

    // Test
    int ranks3[3];
    int temp;
    switch(test)
    {
        case 0:
            ranks3[0] = ranks3[1] = ranks3[2] = 0;
            printf("%s", vote(0, "Bob", ranks3) ? "true" : "false");
            break;

        case 1:
            ranks3[0] = ranks3[1] = ranks3[2] = 0;
            printf("%s", vote(0, "David", ranks3) ? "true" : "false");
            break;

        case 2:
            ranks3[0] = ranks3[1] = ranks3[2] = 0;
            vote(0, "Bob", ranks3);
            vote(1, "Charlie", ranks3);
            vote(2, "Alice", ranks3);
            printf("%i %i %i", ranks3[0], ranks3[1], ranks3[2]);
            break;

        case 3:
            ranks3[0] = 1;
            ranks3[1] = 2;
            ranks3[2] = 0;
            record_preferences(ranks3);
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    printf("%i ", preferences[i][j]);
            break;

        case 4:
            preferences[0][0] = 0;
            preferences[0][1] = 2;
            preferences[0][2] = 1;
            preferences[1][0] = 3;
            preferences[1][1] = 0;
            preferences[1][2] = 4;
            preferences[2][0] = 3;
            preferences[2][1] = 5;
            preferences[2][2] = 0;
            ranks3[0] = 1;
            ranks3[1] = 0;
            ranks3[2] = 2;
            record_preferences(ranks3);
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    printf("%i ", preferences[i][j]);
            break;

        case 5:
            add_pairs();
            printf("%i\n", pair_count);
            break;

        case 6:
            add_pairs();
            for (int i = 0; i < 3; i++)
                if (pairs[i].winner == 0 && pairs[i].loser == 1)
                    printf("true ");
                else if (pairs[i].winner == 0 && pairs[i].loser == 2)
                    printf("true ");
                else if (pairs[i].winner == 2 && pairs[i].loser == 1)
                    printf("true ");
            break;

        case 7:
            add_pairs();
            temp = 0;
            for (int i = 0; i < 3; i++)
            {
                if (pairs[i].winner == 1 && pairs[i].loser == 0)
                    temp++;
                else if (pairs[i].winner == 2 && pairs[i].loser == 0)
                    temp++;
                else if (pairs[i].winner == 1 && pairs[i].loser == 2)
                    temp++;
            }
            printf("%i", temp);
            break;

        case 8:
            sort_pairs();
            for (int i = 0; i < 3; i++)
                printf("%i %i ", pairs[i].winner, pairs[i].loser);
            break;

        case 9:
            pair_count = 4;
            pairs[0].winner = 0; pairs[0].loser = 1;
            pairs[1].winner = 1; pairs[1].loser = 2;
            pairs[2].winner = 2; pairs[2].loser = 3;
            pairs[3].winner = 1; pairs[3].loser = 3;
            lock_pairs();
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    printf("%s ", locked[i][j] ? "true" : "false");
            break;

        case 10:
            pair_count = 4;
            pairs[0].winner = 0; pairs[0].loser = 1;
            pairs[1].winner = 1; pairs[1].loser = 2;
            pairs[2].winner = 2; pairs[2].loser = 3;
            pairs[3].winner = 3; pairs[3].loser = 0;
            lock_pairs();
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    printf("%s ", locked[i][j] ? "true" : "false");
            break;

        case 11:
            pair_count = 4;
            pairs[0].winner = 0; pairs[0].loser = 1;
            pairs[1].winner = 1; pairs[1].loser = 2;
            pairs[2].winner = 2; pairs[2].loser = 0;
            pairs[3].winner = 2; pairs[3].loser = 3;
            lock_pairs();
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    printf("%s ", locked[i][j] ? "true" : "false");
            break;

        case 12:
            pair_count = 6;
            locked[0][0] = false;
            locked[0][1] = locked[0][2] = locked[0][3] = true;
            locked[1][0] = locked[1][1] = false;
            locked[1][2] = locked[1][3] = true;
            locked[2][0] = locked[2][1] = locked[2][2] = false;
            locked[2][3] = true;
            locked[3][0] = locked[3][1] = locked[3][2] = locked[3][3] = false;
            print_winner();
            break;

        case 13:
            pair_count = 4;
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++)
                    locked[i][j] = false;
            locked[2][0] = true;
            locked[0][1] = true;
            locked[0][3] = true;
            locked[1][3] = true;
            print_winner();
            break;

        case 14:  //lock final pair test
            pair_count = 7;
            pairs[0].winner = 0; pairs[0].loser = 1;
            pairs[1].winner = 1; pairs[1].loser = 4;
            pairs[2].winner = 4; pairs[2].loser = 2;
            pairs[3].winner = 4; pairs[3].loser = 3;
            pairs[4].winner = 3; pairs[4].loser = 5;
            pairs[5].winner = 5; pairs[5].loser = 1;
            pairs[6].winner = 2; pairs[6].loser = 1;

            lock_pairs();
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    printf("%s ", locked[i][j] ? "true" : "false");
            break;

        case 15: //lock middle pair test
            pair_count = 5;
            pairs[0].winner = 2; pairs[0].loser = 0;
            pairs[1].winner = 4; pairs[1].loser = 1;
            pairs[2].winner = 1; pairs[2].loser = 3;
            pairs[3].winner = 3; pairs[3].loser = 4;
            pairs[4].winner = 4; pairs[4].loser = 2;

            lock_pairs();
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    printf("%s ", locked[i][j] ? "true" : "false");
            break;

        case 16: //lock all pairs if no cycles
            pair_count = 4;
            pairs[0].winner = 4; pairs[0].loser = 2;
            pairs[1].winner = 0; pairs[1].loser = 3;
            pairs[2].winner = 1; pairs[2].loser = 0;
            pairs[3].winner = 3; pairs[3].loser = 4;

            lock_pairs();
            for (int i = 0; i < candidate_count; i++)
                for (int j = 0; j < candidate_count; j++)
                    printf("%s ", locked[i][j] ? "true" : "false");
            break;
    }
}