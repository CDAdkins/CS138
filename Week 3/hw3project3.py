# Exercise No.   3
# File Name:     hw3project3.py
# Programmer:    Chris Adkins
# Date:          Feb. 11, 2020
#
# Problem Statement: This program calculates the length needed for a ladder when given the height needed to reach
#                    and the angle the angle at which the ladder will be leaning against a surface.
#
# Overall Plan:
# 1. Define height from user input.
# 2. Define angle from user input.
# 3. Define the angle in radians by using the formula from the book.
# 4. Define length using the formula given in the book.
# 5. Print the length to the user.
#
# Import the necessary python libraries
# math - for sin()

import math


def main():
    height = eval(input("In feet, how high do you need to reach? "))
    angle = eval(input("In degrees, what is the angle of the ladder when leaned against the house? "))
    radian = (3.14/180) * angle
    length = height/math.sin(radian)
    print("You will need a ladder that is ", length, "ft long.")


main()
