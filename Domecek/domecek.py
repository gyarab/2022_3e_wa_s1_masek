from turtle import *
from math import sqrt
from random import *

penup()
goto(-1800, -450)
pendown()
def draw_house(a):
    left(90)
    forward(a)
    right(135)
    forward(sqrt(a * a * 2))
    left(135)
    forward(a)
    left(90)
    forward(a)
    right(135)
    forward(sqrt(a * a * 2) / 2)
    right(90)
    forward(sqrt(a * a * 2) / 4)
    left (135)
    forward(a * 0.2)
    right(90)
    forward(a * 0.1)
    right(90)
    forward(a * 0.3)
    left(45)
    forward(sqrt(a * a * 2) / 6.6)
    right(90)
    forward(sqrt(a * a * 2))
    left (135)
    forward(a)
while(True):
    draw_house(randrange(50, 300))

exitonclick()
