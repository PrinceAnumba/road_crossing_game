from turtle import Turtle

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car_Manager:
  def __init__(self):
    self.car_list = []
    self.car_speed = 5

  def create_car(self):
    random_outcome = random.randint(1, 7)

    if random_outcome == 6:
      new_car = Turtle('square')
      new_car.penup()
      new_car.shapesize(stretch_len=2, stretch_wid=1)
      new_car.color(random.choice(COLORS))
      y_cordinate = random.randint(-250, 250)
      new_car.goto(300, y_cordinate)
      self.car_list.append(new_car)

  def move_car(self):
    for car in self.car_list:
      car.backward(self.car_speed)

  def update_speed(self):
    self.car_speed +=MOVE_INCREMENT