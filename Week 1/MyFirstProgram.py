#! /usr/bin/python
# Exercise No.   1
# File Name:     MyFirstProgram.py
# Programmer:    Chris Adkins
# Date:          Jan. 22, 2020
#
# Problem Statement: Ask the user to enter two numbers, calculate the sum of
# these two numbers, and display the sum to the screen
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for two integers
# 3. Calculate the sum of the integers
# 4. Print the sum of the integers to the screen
#
#
# Import the necessary python libraries
# For this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("I can add two numbers for you")
    print("Enter one whole number(Ex. 52):")

    # Variables are declared dynamically no need to pre-define
    num1 = eval(input())
    print("Enter another whole number(Ex. 41):")
    num2 = eval(input())
    print("Enter one more whole number(Ex. 30):")
    num3 = eval(input())
    percentage = (num1 / num2 / num3) * 100
    print("Percentage = ", percentage)

    # Here is the processing that is needed
    sum = num1 + num2 + num3
    product = num1 * num2 * num3
    # Output the results
    print("The sum of the three numbers is", sum)
    print("The product of the three numbers is", product)


main()
