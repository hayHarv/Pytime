# write a function called "square" that takes a parameter called t, which is a Turtle

import turtle
import math

# exercise 1
# def square(t):
#     """Takes a turtle object 't' and draws a square"""
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
#
# bob = turtle.Turtle()
#
# square(bob)

# exercise 2
# def square(t,length):
#     """Takes a turtle object 't' and a 'length' parameter to determine how large of a square to draw"""
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
#
# bob = turtle.Turtle()
#
# square(bob,100)
# square(bob,50)

# exercise 3
# def polygon(t,n,length):
#     """Creates an 'n'-sided polygon with sides of 'length' for a turtle object 't' to draw"""
#     angle = 360.0 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

bob = turtle.Turtle()

# polygon(bob,10,360)

# exercise 4
# def circle(t,r):
#     """Draws a circle from turtle object 't', with a radius of 'r'"""
#     circumference = 2 * math.pi * r
#     n = 360 # number of segments, a higher number means more segments
#     length = circumference / n
#     polygon(t,n,length)

# alternative code for exercise 4 that is 'clean'
# def circle(t,r):
#     """Draws a circle from turtle object 't', with a radius of 'r'"""
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 3
#     length = circumference / n
#     polygon(t,n,length)
#
# circle(bob,50)

# exercise 5
# def arc(t,r,angle):
#     """Draws a section of circle equal to 'angle' from turtle object 't', with a radius of 'r'"""
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
#
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)

# arc(bob,30,270)

# refactored exercise 5
# make a function called polyline which takes angle

def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,n,length):
    angle = 360 / n
    polyline(t,n,length,angle)

def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t,n,step_length,step_angle)

def circle(t,r):
    arc(t,r,360)

arc(bob,30,270)

circle(bob,40)
