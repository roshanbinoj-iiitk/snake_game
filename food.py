"""This module shows the food on the screen."""
from turtle import Turtle
import random

class Food(Turtle):
    """This class represents the food on the screen and its appearance at different locations."""

    def __init__(self):
        Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
