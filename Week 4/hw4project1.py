# Exercise No.   1
# File Name:     hw4project1.py
# Programmer:    Chris Adkins
# Date:          Feb. 17, 2020
#
# Problem Statement: This program is an edited version of the one found in the book.
#
# Overall Plan:
# 1. Change the shape from Circle() to Rectangle()
# 2. change the shape.move() method to a shape = in order to make more squares appear.
# 3. After the for loop, create a new text object before another getMouse() call.
#
# Import the necessary python libraries
# graphics.py

from graphics import *
from math import sqrt


def main():
    win = GraphWin("Five Click House", 500, 500)
    win.setBackground(color_rgb(43, 43, 43))

    p = win.getMouse()
    p1 = Point(p.getX(), p.getY())
    p = win.getMouse()
    p2 = Point(p.getX(), p.getY())
    base = Rectangle(p1, p2)  # Base of the house, initial rectangle.
    base.setOutline(color_rgb(180, 180, 180))
    base.draw(win)

    dist = sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)  # Distance between p1 and p2.
    baseHeight = p1.getY() - p2.getY()  # Height of the 'base' object.
    baseWidth = p2.getX() - p1.getX()  # Width of the 'base' object.
    doorWidth = (baseWidth / 5)

    p = win.getMouse()
    p3 = Point(p.getX(), p.getY())  # Third Mouse Click.
    p4 = Point((p3.getX() - doorWidth/2), p3.getY())  # Top left of door.
    p5 = Point(p3.getX() + doorWidth/2, p1.getY())  # Bottom right of the door.
    door = Rectangle(p4, p5)
    door.setOutline(color_rgb(180, 180, 180))
    door.draw(win)

    p = win.getMouse()
    p6 = Point(p.getX(), p.getY())  # Fourth Click.
    p7 = Point(p6.getX() - doorWidth/4, p6.getY() - doorWidth/4)  # Top left of the window.
    p8 = Point(p6.getX() + doorWidth/4, p6.getY() + doorWidth/4)  # Bottom right of the window
    window = Rectangle(p7, p8)
    window.setOutline(color_rgb(180, 180, 180))
    window.draw(win)

    p = win.getMouse()
    p9 = Point(p.getX(), p.getY())  # Fifth Mouse Click, also tip of roof.
    p10 = Point(p1.getX(), p1.getY() - baseHeight)  # Left corner of roof.
    p11 = Point(p2.getX(), p2.getY())  # Right corner of roof.
    roof = Polygon(p9, p10, p11)
    roof.setOutline(color_rgb(180, 180, 180))
    roof.draw(win)

    print("Distance between p1 and p2:", dist)
    print("p1 x:", p1.getX(), "\np1 y:", p1.getY(), "\np2 x:", p2.getX(), "\np2 y:", p2.getY())
    print("Base Height:", baseHeight, "\nBase Width:", baseWidth)
    win.getMouse()
    win.close()


main()
