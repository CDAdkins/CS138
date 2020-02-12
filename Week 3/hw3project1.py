#! /usr/bin/python
# Exercise No.   1
# File Name:     hw3project1.py
# Programmer:    Chris Adkins
# Date:          Feb. 11, 2020
#
# Problem Statement: A program to calculate the cost per square inch of a circular pizza.
#
# Overall Plan:
# 1. Define pi as 3.14.
# 2. Get the diameter from the user.
# 3. Get the cost from the user.
# 4. Define the area using the given formula.
# 5. calculate the cost per square inch by dividing the cost by the area.
#
# Import the necessary python libraries
# For this example none are needed


def main():

    pi = 3.14
    print("Pizza Pricer Pro 9000\n---------------------")
    diameter = eval(input("Enter the diameter of the pizza in inches: "))  # Getting the diameter from the user.
    cost = eval(input("How much does the pizza cost? "))  # Getting the total cost of the pizza.

    area = pi * ((diameter/2) ** 2)  # This formula gives us the area of the pizza.
    costPerInch = cost/area  # Dividing the cost by the area gives us the cost per inch.
    print("Summary\nRadius:", diameter/2, "in\nArea:", area, "in\nCost: $", cost, "\nCost Per Inch: $", costPerInch)


main()
