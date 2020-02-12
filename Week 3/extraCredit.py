#! /usr/bin/python
# Exercise No.   4
# File Name:     extraCredit.py
# Programmer:    Chris Adkins
# Date:          Feb. 11, 2020
#
# Problem Statement: This program takes two numbers and divides them outputting using whole numbers and remainders.
#
# Overall Plan:
# 1. Define the numerator and denominator using user input.
# 2. define the result as the integer division of the two numbers.
# 3. define the remainder as numerator % denominator.
# 4. Print the result to the user.
#
# Import the necessary python libraries
# For this example none are needed


def main():
    numerator = eval(input("Enter the numerator: "))
    denominator = eval(input("Enter the denominator: "))
    result = numerator // denominator
    remainder = numerator % denominator
    print(result, "R", remainder)


main()
