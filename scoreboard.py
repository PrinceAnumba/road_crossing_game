from turtle import Turtle
ALIGNMENT = "left"
RIGHT = "right"

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
  def __init__(self):
      super().__init__()
      self.penup()
      self.color("black")
      self.level = 0
      self.goto(-260, 260)
      self.update()
      self.hideturtle()




  def update(self):
      self.write(f"level: {self.level}", align=ALIGNMENT, font=FONT)

  def game_over(self):
      self.goto(200,260)
      self.write(f"Game_Over: {self.level}", align=RIGHT, font=FONT)

  def increase_level(self):
      self.level += 1
      self.clear()
      self.update()


  

