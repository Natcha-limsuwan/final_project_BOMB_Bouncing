import turtle
import random
turtle.hideturtle()


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("DarkGoldenrod")
        self.ball.penup()
        self.ball.speed(0)
        self.ball.circle(20)
        self.ball.goto(0, -200)
        self.dx = random.choice([3, -3])
        self.dy = 3

    def move(self):
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1
