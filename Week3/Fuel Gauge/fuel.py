def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = map(int, fraction.split('/'))
            if denominator == 0:
                raise ValueError("ZeroDivisionError")
            if numerator > denominator:
                raise ValueError("ValueError")
            return numerator, denominator
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def calculate_fuel_percentage(numerator, denominator):
    fuel_percentage = (numerator / denominator) * 100
    return round(fuel_percentage)


def main():
    numerator, denominator = get_fraction()
    fuel_percentage = calculate_fuel_percentage(numerator, denominator)

    if fuel_percentage <= 1:
        print("E")
    elif fuel_percentage >= 99:
        print("F")
    else:
        print(f"{fuel_percentage}%")


if __name__ == "__main__":
    main()
