import turtle
turtle.hideturtle()
class Bomb:
    def __init__(self, x, y):
        self.bomb = turtle.Turtle()
        self.bomb.shape("circle")
        self.bomb.color("firebrick4")
        self.bomb.penup()
        self.bomb.goto(x, y)
        self.dy = -3

    def move(self):
        self.bomb.sety(self.bomb.ycor() + self.dy)

    def out_bounds(self):
        return self.bomb.ycor() < -300
