#! /usr/bin/python
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


def main():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), (Point(10, 10)))
    shape.setOutline("black")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        shape = (Rectangle(Point(p.getX() - win.getWidth()/10, p.getY() - win.getHeight()/10),
                           (Point(p.getX() + win.getWidth()/10, p.getY() + win.getHeight()/10))))
        shape.setOutline("black")
        shape.setFill("red")
        shape.draw(win)

    quitText = Text((Point(100, 100)), "Click Again to Quit")
    quitText.setSize(16)
    quitText.draw(win)
    win.getMouse()

    win.close()


main()
