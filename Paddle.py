import turtle
turtle.hideturtle()
class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("DodgerBlue4")
        self.paddle.shapesize(stretch_wid=1, stretch_len=6)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def move_left(self):
        x = self.paddle.xcor() - 25
        self.paddle.setx(max(x, -350))

    def move_right(self):
        x = self.paddle.xcor() + 25
        self.paddle.setx(min(x, 350))
