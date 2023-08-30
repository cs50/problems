#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct person
{
    struct person *parents[2];
    char alleles[2];
}
person;

person *create_family(int generations);
void print_family(person *p, int indent);
void free_family(person *p);
char random_allele();

int main(void)
{
    // Seed random number generator
    srand(time(0));

    // Create a new family with three generations
    person *p = create_family(3);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}

person *create_family(int generations)
{
    // TODO: Allocate memory for new person

    // Generation with parent data
    if (generations > 1)
    {
        // TODO: Recursively create blood type histories for parents
        // TODO: Randomly assign child alleles based on parents
    }

    // Generation without parent data
    else
    {
        // TODO: Set parent pointers to NULL
        // TODO: Randomly assign alleles
    }

    // TODO: Return newly created person
}

void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * 4; i++)
    {
        printf(" ");
    }

    // Print person
    printf("Generation %i, blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

void free_family(person *p)
{
    // TODO: Handle base case
    // TODO: Free parents
    // TODO: Free child
}

char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
