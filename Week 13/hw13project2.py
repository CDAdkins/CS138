# Exercise No.   5
# File Name:     hw13project2.py
# Programmer:    Chris Adkins
# Date:          May. 12, 2020
#
# Problem Statement: This program recursively converts a user-defined number to a base of their choosing.
#
# Overall Plan:
# 1. Get input from the user. Create a variable for the number to be converted and for the base.
# 2. Create a method to convert the number.
#       a. If the number is greater than 0.
#       b. Call the convert function with the number divided by the base.
#       c. Print the number % base.
#
# Import the necessary python libraries.
# None needed.

def main():
    num = eval(input("Enter a number: "))
    base = eval(input("Enter the base: "))
    convert(num, base)
    print()

def convert(num, base):    
    if (num > 0):
        convert(num // base, base)
        print(num % base, end=" ")
    
main()
