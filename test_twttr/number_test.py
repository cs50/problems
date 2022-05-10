def main():
    word = input("Input: ").strip()
    print("Output:", convert(word))


def convert(word):
    converted = ""
    for letter in word:
        if letter.upper() not in list("AEIOU") and letter not in list("0123456789"):
            converted += letter
    return converted


if __name__ == "__main__":
    main()
