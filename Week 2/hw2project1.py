#! /usr/bin/python
# Exercise No.   1
# File Name:     hw2project1.py
# Programmer:    Chris Adkins
# Date:          Feb. 4, 2020
#
# Problem Statement: Modify the convert.py program to have an introduction.
#
#
# Overall Plan:
# 1. add a print statement to the beginning of the program.
#
# Import the necessary python libraries
# For this example none are needed


def main():
    print("This program takes a celsius temperature given by the user and converts that number to the equivalent "
          "fahrenheit temperature.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
