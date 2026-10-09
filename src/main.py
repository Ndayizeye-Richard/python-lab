from utils import celsius_to_fahrenheit, greet, is_even, square


def main():
    number = float(input("Enter a number: "))
    print(f"Square: {square(number)}")
    print(f"Even: {is_even(number)}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number):.2f}°F")

    name = input("Enter your name: ")
    print(greet(name))


if __name__ == "__main__":
    main()
