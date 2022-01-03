#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t
ALIGNMENT = 'center'
FONT = ('Arial', 25, 'normal')

class Snake_Scoreboard(t.Turtle):
    def __init__(self):
        #super().__init__() - class inheritance - allows us to take an existing class, and build upon it
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        #t.goto() - make it go to a random x and y location
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align = ALIGNMENT, font = FONT)
    def game_over(self):
        #start it back to its original location 
        self.goto(0, 0)
        self.write('Game Over. Try Again!', align = ALIGNMENT, font = FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


# In[ ]:




