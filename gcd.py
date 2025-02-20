def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    print("Програма для знаходження найбільшого спільного дільника (НСД)")
    try:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        result = gcd(num1, num2)
        print(f"НСД({num1}, {num2}) = {result}")
    except ValueError:
        print("Будь ласка, вводьте лише цілі числа.")


if __name__ == "__main__":
    main()
