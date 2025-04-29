#include <stdlib.h>

int main(int argc, string argv[])
{
    int test = atoi(argv[1]);

    switch (test)
    {
        case 0:
            printf("%i", get_cents());
            break;
        
        case 1:
            printf("%i", calculate_quarters(50));
            break;

        case 2:
            printf("%i", calculate_quarters(42));
            break;
        
        case 3:
            printf("%i", calculate_dimes(10));
            break;
        
        case 4:
            printf("%i", calculate_dimes(15));
            break;

        case 5:
            printf("%i", calculate_nickels(5));
            break;

        case 6:
            printf("%i", calculate_nickels(28));
            break;

        case 7:
            printf("%i", calculate_pennies(4));
            break;

        case 8:
            printf("%i", calculate_dimes(73));
            break;
            
    }
}
