import time
from turtle import Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Call player turtle
player = Player()

# Call cars
car_manager = Car_Manager()

#
scoreboard = Scoreboard()

# Listening for keypress
screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    #Detect collision with cars
    for car in car_manager.car_list:
      if car.distance(player) < 20:
        game_is_on=False
        scoreboard.game_over()

    #Reset player to initial position
    if player.ycor() > 270:
      player.back_to_start()
      scoreboard.increase_level()
      car_manager.update_speed()
      

screen.exitonclick()