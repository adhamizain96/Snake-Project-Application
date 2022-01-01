import turtle as t
from snake import Snake
from food import Snake_Food
from scoreboard import Snake_Scoreboard
import time

screen = t.Screen()
screen.setup(width = 500, height = 500)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Snake_Food()
scoreboard = Snake_Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

snake_game_on = True
while snake_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake_game_on = False
        scoreboard.game_over()
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            snake_game_on = False
            scoreboard.game_over

screen.exitonclick()