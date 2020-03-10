# Exercise No.   3
# File Name:     hw6project1.py
# Programmer:    Chris Adkins
# Date:          Mar. 3, 2020
#
# Problem Statement: This program takes a radius from the user and calculates a sphere's area and volume with it.
#
# Overall Plan:
# 1. Get the radius from the user.
# 2. Create a function for both the area and volume calculations.
# 3. Pass the radius as an argument to the functions.
# 4. Use the respective formulas to get the area and volume.
# 5. Print the results to the user
#
# Import the necessary python libraries.
# None needed.


def main():  # Our main function.
    radius = eval(input("What is the radius of the sphere? "))  # Getting the radius from the user.
    sphereArea(radius)  # Calling our area function.
    sphereVolume(radius)  # Calling our volume function.


def sphereVolume(radius):
    pi = 3.1415  # Defining pi.
    volume = (4/3) * pi * radius ** 3  # This is our implementation of the volume formula.
    print("Volume:", volume)  # Printing the volume to the user.


def sphereArea(radius):
    pi = 3.1415
    area = (4*pi*radius ** 2)  # Our implementation of tha area formula.
    print("Area:", area)  # Printing the area to the user.


main()
