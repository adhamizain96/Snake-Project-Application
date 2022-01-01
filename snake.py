import turtle as t
#constants need to be in all caps
#starting_pos = [0,1,2]
STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_seg(pos)
    def add_seg(self, pos):
        new_seg = t.Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)
    def extend(self):
        self.add_seg(self.segments[-1].pos())
    def move_snake(self):
        #len(segments) - [1,2,3] -> len(segments)-1 - [0,1,2]
        #how the snake moves - have to go in reverse
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[seg_num - 1].xcor()
            y_new = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_new, y_new)
        self.head.forward(MOVE_DIS)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)