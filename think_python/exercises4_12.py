"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

import math
import turtle

def move(t, length, direction):
    if direction == 'up':
        t.pu()
        t.rt(90)
        t.fd(length)
        t.lt(90)
        t.pd()
    elif direction == 'down':
        t.pu()
        t.lt(90)
        t.fd(length)
        t.rt(90)
        t.pd()
    elif direction == 'forward':
        t.pu()
        t.fd(length)
        t.pd()
    elif direction == 'backward':
        t.pu()
        t.bk(length)
        t.pd()
    else:
        print('try again')

def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        t.lt(180 - angle)

def flower(t,n,r,angle):
    for i in range(n):
        petal(t,r,angle)
        t.lt(360/n)

# def pie_slice(t,length,width):
#     inner_length =
#     polyline(t,)
#
# def pie(t,slices,length):
#     for i in range(slices):
#         polygon(t,3,length)
#         t.lt(180)

def draw_pie(t,n,r):
    polypie(t,n,r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

def polypie(t,n,r):
    angle = 360 / n
    for i in range(n):
        isosceles(t,r,angle/2)
        t.lt(angle)

def isosceles(t,r,angle):

    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90 + angle)
    t.fd(2*y)
    t.lt(90 + angle)
    t.fd(r)
    t.lt(180-angle)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    # radius = 100
    # bob.pu()
    # bob.fd(radius)
    # bob.lt(90)
    # bob.pd()
    # circle(bob, radius)

    move(bob, 100, 'backward')
    move(bob, 100, 'up')
    flower(bob, 7, 60, 60)

    move(bob, 100, 'forward')
    flower(bob, 10, 40, 80)

    move(bob, 100, 'forward')
    flower(bob,20,140,20)

    move(bob, 100, 'up')
    draw_pie(bob, 7, 40)

    move(bob, 100, 'backward')
    draw_pie(bob, 6, 40)

    move(bob, 100, 'backward')
    draw_pie(bob, 5, 40)

    bob.hideturtle()
    # wait for the user to close the window
    turtle.mainloop()
