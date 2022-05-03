import professor
import random
import sys

def main():
    argument = sys.argv[1]
    if argument == "get_level":
        professor.get_level()
    elif argument == "main":
        random.seed(0)
        professor.main()

main()