import turtle as t
import random

class Snake_Food(t.Turtle):
    def __init__(self):
        #super().__init__() - class inheritance - allows us to take an existing class, and build upon it
        super().__init__()
        self.shape('circle')
        self.penup()
        #t.shapesize() - stretch_wid, stretch_len, and outline - allows us to stretch the length and width of the turtle
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
    def refresh(self):   
        x_rand = random.randint(-280, 280)
        y_rand = random.randint(-280, 280)
        #t.goto() - make it go to a random x and y location
        self.goto(x_rand, y_rand)