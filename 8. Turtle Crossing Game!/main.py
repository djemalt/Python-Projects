import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    #check if Leven UP
    if player.ycor() > 280:
        car_manager.level_up()
        player.reset()
        scoreboard.increase_level()

screen.exitonclick()

