# Exercise No.   12
# File Name:     hw8project2.py
# Programmer:    Chris Adkins
# Date:          Apr. 7, 2020
#
# Problem Statement: This program takes an image and (slowly) converts it into grayscale.
#
# Overall Plan:
# 1. Find the image using the path given to you.
# 2. Create a for-loop to iterate over every pixel and change it to grayscale.
#   a. Create an int to represent rows, as well as one to represent columns.
#   b. Get the rgb value from the current pixel.
#   c. Use the given formula to convert the pixel to grayscale.
#   d. call win.update() so you can see the process as it's happening.
# 3. Save the image.
#
# Import the necessary python libraries.
# graphics.py

from graphics import Image, GraphWin, Point, color_rgb

def main():  
    fileInput = "C:\Programming\CS138\Week 8\canoe.gif"
    fileOutput = "C:\Programming\CS138\Week 8\grayCanoe.gif"

    image = Image(Point(400,300), fileInput)  # Getting our image.
    width = image.getWidth()
    height = image.getHeight()
    win = GraphWin("Monochromatic Conversion", width, height)  # Creating our window.
    image.draw(win)

    row = 0  # The starting pixel for our x-axis
    column = 0  # The starting pixel for our y-axis

    win.getMouse()

    for row in range(image.getWidth()):
        for column in range(image.getHeight()):
            r, g, b = image.getPixel(row, column)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            image.setPixel(row, column, color_rgb(brightness, brightness, brightness))
            win.update()

    image.save(fileOutput)
    win.getMouse()
    win.close()

main()