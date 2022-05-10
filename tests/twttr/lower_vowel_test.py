def main():
    word = input("Input: ").strip()
    print("Output:", convert(word))


def convert(word):
    converted = ""
    for letter in word:
        if letter not in list("AEIOU"):
            converted += letter
    return converted


if __name__ == "__main__":
    main()
