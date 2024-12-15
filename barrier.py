import turtle
turtle.hideturtle()
class Barrier:
    def __init__(self, x, y, color):
        self.barrier = turtle.Turtle()
        self.barrier.shape("circle")  # Changed to circle
        self.barrier.color(color)
        self.barrier.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Adjusted for circle size
        self.barrier.penup()
        self.barrier.goto(x, y)

    def hide(self):
        self.barrier.hideturtle()

    def visible(self):
        return self.barrier.isvisible()
