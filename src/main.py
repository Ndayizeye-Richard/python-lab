from utils import celsius_to_fahrenheit, is_even, square


def main():
    number = float(input("Enter a number: "))
    print(f"Square: {square(number)}")
    print(f"Even: {is_even(number)}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number):.2f}°F")


if __name__ == "__main__":
    main()
