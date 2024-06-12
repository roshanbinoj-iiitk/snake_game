import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

SCREEN.listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")

GAME_IS_ON = True
while GAME_IS_ON:
    SCREEN.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if (snake.head.xcor() > 280 or
            snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280):
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()

SCREEN.exitonclick()
