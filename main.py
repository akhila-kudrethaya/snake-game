import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - 2022")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh_food()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_game()
        snake.snake_reset()

    # detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset_game()
            snake.snake_reset()

screen.exitonclick()
