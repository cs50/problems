def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2:
        return False
    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False
    if len(s) > 6:
        return False
    for i in range(len(s) - 1):
        if s[i].isdecimal() and s[i + 1].isalpha():
            return False
#    for c in s:
#        if c.isdecimal():
#            if c == "0":
#                return False
#            break
    return True


if __name__ == "__main__":
    main()
