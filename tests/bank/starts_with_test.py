def main():
    greeting = input("Greeting: ").strip()
    print("$", value(greeting), sep="")


def value(greeting):
    s = greeting.lower()
    if s == "hello":
        return 0
    elif s == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
