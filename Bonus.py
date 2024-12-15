import turtle
turtle.hideturtle()
class Bonus:
    def __init__(self, x, y, color="peru", size=20):
        self.size = size
        self.color = color
        self.bonus = turtle.Turtle()
        self.bonus.shape('turtle')
        self.bonus.color(self.color)
        self.bonus.penup()
        self.bonus.goto(x, y)
        self.dy = -1.8

    def move(self):
        self.bonus.sety(self.bonus.ycor() + self.dy)

    def out_bounds(self):
        return self.bonus.ycor() < -300
