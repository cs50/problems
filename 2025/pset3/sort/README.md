# Sort

Analyze three sorting programs to determine which algorithms they use.

## Background

Recall from class a few algorithms in which we can sort a list of numbers: selection sort, bubble sort, and merge sort. 

* Selection sort iterates through the unsorted portions of a list, selecting the smallest element each time and moving it to its correct location. 
* Bubble sort compares two adjacent values at a time and swaps them if they are in the incorrect order. This continues until the list is sorted.
* Merge sort divides the list into two repeatedly and then combines the smaller lists back into a larger one in the correct order. 

## Instructions

Provided to you are three sorts, `sort1`, `sort2`, and `sort3`. The three sorts implemented are selection sort, bubble sort, and merge sort. Determine the sorting algorithms each sort implements. 

* `sort1`, `sort2`, and `sort3` are binary files and cannot be opened by the user. To assess which sort implements which algorithm, run the sorts on different lists of values. 
* Multiple `.txt` files are provided to you. These files contain `n` lines of values, either reversed, shuffled, or sorted. 
  * For example, `reversed10000.txt` contains 10000 lines of numbers that are reversed from `10000`, while `shuffled100000.txt` contains 100000 lines of numbers that are in random order. 
* To run the sorts on the text files, in the terminal, run `./[sort_file] [text_file.txt]`. 
  * For example, to sort `reversed10000.txt` with `sort1`, run `./sort1 reversed10000.txt`. 
* Record your predictions in `answers.txt`. 

### Hints

* You may find it helpful to time your sorts. To do so, run `time ./[sort_file] [text_file.txt]`. 
* The different types of `.txt` files may help you determine which sort is which. Consider how each algorithm performs with an already sorted list. How about a reversed list? Or shuffled list? It may help to work through a smaller list of each type and walk through each sorting process. 

{% next %}

## How to Submit

TODO
