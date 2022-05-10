def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if 0.0 <= percentage <= 1.0:
                break
    print(gauge(percentage))


def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator, denominator = int(numerator), int(denominator)
    return numerator / denominator


def gauge(percentage):
    if percentage < 0.01:
        return "E"
    elif percentage > 0.99:
        return "F"
    else:
        return f"{round(percentage * 100)}%"


if __name__ == "__main__":
    main()
