#! /usr/bin/python
# Exercise No.   2
# File Name:     hw2project2.py
# Programmer:    Chris Adkins
# Date:          Feb. 4, 2020
#
# Problem Statement: This program will convert a fahrenheit temperature supplied by the user to celsius.
#
#
# Overall Plan:
# 1. Create an int and use eval(input()) to receive the Fahrenheit temperature from the user.
# 2. create an int to hold celsius and use the given formula to convert the given fahrenheit number.
# 3. Print the converted temperature to the user.
#
# Import the necessary python libraries
# For this example none are needed


def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5 * (fahrenheit-32) / 9
    print("The temperature is ", celsius, "degrees Celsius.")


main()
