int check_alleles(person *p)
{
    if (p -> parents[0] == NULL)
    {
        return 1;
    }

    else
    {
        if ((p->alleles[0] != p->parents[0]->alleles[0]) && (p->alleles[0] != p->parents[0]->alleles[1]))
        {
            return 0;
        }

        if ((p->alleles[1] != p->parents[1]->alleles[0]) && (p->alleles[1] != p->parents[1]->alleles[1]))
        {
            return 0;
        }

        return (check_alleles(p -> parents[0]) && check_alleles(p -> parents[1]));
    }
}

int check_size(person *p, int n)
{
    if (p -> parents[0] == NULL)
    {
        return n == 1;
    }

    else
    {
        return (check_size(p -> parents[0], n - 1));
    }
}


int main(void)
{
    srand(time(0));
    person *p = create_family(3);

    printf(check_size(p, 3) ? "size_true " : "size_false ");
    printf(check_alleles(p) ? "allele_true" : "allele_false");

    free_family(p);
}
