#! /usr/bin/python
# Exercise No.   2
# File Name:     hw3project2.py
# Programmer:    Chris Adkins
# Date:          Feb. 11, 2020
#
# Problem Statement: A program to calculate the epact used in calculating the day of Easter.
#
# Overall Plan:
# 1. Get the current year from the user.
# 2. Define variable 'c' as year//100
# 3. Implement the formula given in the book to get the epact.
# 4. Print the result of the epact formula back to the user.
#
# Import the necessary python libraries
# For this example none are needed


def main():
    year = eval(input("What year is it? "))  # Getting the year from the user.
    c = year//100  # Defining 'c' as the current year//100
    epact = (8 + (c//4) - c + ((8 * c + 13)//25) + 11 * (year % 19)) % 30
    print(epact)


main()
