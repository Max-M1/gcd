import pytest


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


def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(101, 103) == 1
    assert gcd(56, 98) == 14
    assert gcd(0, 5) == 5
    assert gcd(7, 0) == 7
    assert gcd(0, 0) == 0
