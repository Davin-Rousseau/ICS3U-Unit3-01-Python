#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on September 2019
# This program the sum of 2 integers
# with user input


def main():
    # This function calculates the sum of two integers

    # input
    number1 = int(input("Enter first number (integer): "))
    number2 = int(input("Enter second number (integer): "))

    # process
    answer = number1 + number2

    # output
    print("")
    print("{} + {} = {}".format(number1, number2, answer))


if __name__ == "__main__":
    main()
