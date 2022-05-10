def main():
    greeting = input("Greeting: ").strip()
    print("$", value(greeting), sep="")


def value(greeting):
    s = greeting.lower()
    if s.startswith("hello"):
        return 100
    elif s.startswith("h"):
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()
