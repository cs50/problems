# Blood Types

Determine the blood types of each member of a family. 

```
$ ./inheritance
Generation 0, blood type OO
    Generation 1, blood type AO
        Generation 2, blood type OA
        Generation 2, blood type BO
    Generation 1, blood type OB
        Generation 2, blood type AO
        Generation 2, blood type BO

```

## Background

Blood types are determined by two alleles (forms of a gene), and the possible alleles include A, B, and O. Each of a child's parents will randomly pass one of their two blood type alleles to their child. 

For example, if one parent has blood type AO and the other parent has blood type BB, then the child's possible blood types would be AB and OB, depending on which allele is received from each parent. Similarly, if one parent has blood type AO and the other OB, then the child's possible blood types would be AO, OB, AB, and OO.

## Implementation Details

Complete the implementation of `inheritance.c` at right, such that it creates a family of a specified generation size and assigns blood type alleles to each family member. The oldest generation will have alleles assigned randomly to them.

* First, notice that we've created a `struct` named `person`. Each `person` will have two parents, each being a pointer that points to a `person`. They are stored in an array named `parents`. Additionally, each `person` will have two alleles, one from each parent, stored in an array named `alleles`. 
* Notice that there are four helper functions. 
  * `create_family()` takes as input an integer, allocates memory for the family, and returns a person with a family of that specified number of generations.
    * For example, `create_family(3)` will return a person with parents and grandparents.  
  * `print_family()` takes as input a person and a number signifying the generation that the person is in. This function prints the entire family, their generation numbers, and their blood types, as per the sample output. 
  * `free_family()` takes as input a person and frees the memory associated with this person and the person's family. Remember that all the memory we allocate, we also have to free. 
  * `random_allele()` returns a random allele between `A`, `B`, and `O`. 
* Notice that `main()` is already implemented. 
  * First, a random seed is set, which depends on the time of executing the program. This allows for different random values to be generated when we call functions incorporating randomness. 
  * A new family with three generations is then created using `create_family(3)`, and it is stored in a person of type `person` and name `p`. 
  * The family of `p` is then printed with `print_family(p, 0)`.
  * Finally, the memory associated with this family is freed with `free_family(p)`. 
* In `create_family()`, your program should create a family with the specified number of generations. 
  * When creating a family, first allocate memory for a new person. 
  * Then, if the input to the function is not `1`, recursively create the person's parents and use the parents' alleles to assign the child's alleles. Note the rules for assigning alleles described above—the determination of which of the two alleles the child gets from a parent is random.
  * If the input to the function is `1`, set the person's parent pointers to `NULL` and randomly assign its alleles. 
  * For example, your program should work as follows for a family of generation size three. 
    * A person, the child, is created. Currently, the child has no parents and no alleles. 
    * The person's parents are created. Neither parent has parents or alleles. 
    * The grandparents are created, and alleles are randomly assigned to the grandparents. 
    * Now that the grandparents have been created and have alleles, the parents' alleles can also be assigned. 
    * Now that the parents' alleles are assigned, the child's alleles can be assigned.
* In `free_family()`, your program should free the memory associated with a particular person and their family. To do so, you should first handle the base case, then free the parents, and then free the child. Note that if `free_family()` is not written in this order and the child is freed first, we will not be able to access the parents anymore, losing that memory. 

### Hints

* You might find the `rand()` function useful for randomly assigning alleles. This function returns an integer between `0` and `RAND_MAX`, or `32767`. For inspiration on how `rand()` can be used on a smaller scale, consider looking at how `random_allele()` is implemented. 
* Remember, to allocate memory for a particular person, we can use `malloc(n)`, which takes a size as argument and will allocate `n` bytes of memory.
* Remember, to access a variable via a pointer, we can use arrow notation. 
  * For example, if `p` is a person, then this person's first parent can be accessed by `p->parents[0]`. 
* Recursion is particularly helpful in this problem, and looking at `print_family()` for inspiration may be helpful. In `print_family()`, we print the person and their blood type, and then we call `print_family()` again on the person's parents to print the person's parents, which will call the person's parents' parents, and so on. Additionally note that when we call `print_family()` on the person's parents, we increment the generation number.
* For `create_family()`, sometimes it is not necessary to create parents for a person and sometimes it is. Consider this: assume we have already created the child and a parent for a family of three generations. We're now creating a grandparent. Is it necessary for the grandparent to have parent pointers, and how might we keep track of that? 
* For the base case in `free_family()`, consider the edge cases in this family tree. Specifically, for a family with three generations, how do we represent the parents of the grandparents?


### How to Test Your Code

Upon running `./inheritance`, your program should adhere to the rules described in the background. The child should have two alleles, one from each parent. The parents should each have two alleles, one from each of their parents. 

For example, in the example below, the child in Generation 0 received an O allele from both Generation 1 parents. The first parent received an A from the first grandparent and a O from the second grandparent. Similarly, the second parent recieved an O and a B from their grandparents.

```
$ ./inheritance
Generation 0, blood type OO
    Generation 1, blood type AO
        Generation 2, blood type OA
        Generation 2, blood type BO
    Generation 1, blood type OB
        Generation 2, blood type AO
        Generation 2, blood type BO

```



{% next %}

## How to Submit

TODO
