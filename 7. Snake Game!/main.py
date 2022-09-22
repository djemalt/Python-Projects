from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

COLLISION = 295

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_on = True

while game_on:
    screen.update()

    # To make it Harder and Faster when you collect more, numbers can change but this is for example
    if score_board.score < 5:
        time.sleep(0.1)
    elif score_board.score >= 5 and score_board.score < 10:
        time.sleep(0.05)
    elif score_board.score >= 10 and score_board.score < 15:
        time.sleep(0.025)
    elif score_board.score >= 15:
        time.sleep(0.02)
    snake.move()

    # Detect Collision with Food!
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.add_score()

    # Detect Collision with Wall!
    if snake.head.xcor() > COLLISION or snake.head.xcor() < -COLLISION or snake.head.ycor() > COLLISION or snake.head.ycor() < -COLLISION:
        game_on = False
        score_board.game_over()

    # Detect Collision with Tail!
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()

screen.exitonclick()
