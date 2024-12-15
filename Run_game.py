import turtle
import random
turtle.hideturtle()


class Run_game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("BOMB Bouncing")
        self.screen.bgcolor("PaleGoldenrod")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.paddle = Paddle()
        self.ball = Ball()
        self.barriers = []
        self.bombs = []
        self.bonuses = []
        self.score = 0

        self.score_display = turtle.Turtle()
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)
        self.update_score(0)

        self.create_barriers()

    def input_name(self):
        turtle.penup()
        turtle.goto(0, 150)
        turtle.write("Hello, what's your name?", align="center", font=("Arial", 16, "bold"))

        self.name = self.screen.textinput("Your name", "Name")
        if not self.name:
            self.name = "Player"
        turtle.clear()

    def create_barriers(self):
        colors = ["SteelBlue2", "SkyBlue3", "SkyBlue4", "SteelBlue4", "DodgerBlue4"]
        for row in range(5):
            for col in range(24):
                x = -400 + col * 35
                y = 230 - row * 35
                color = colors[row % len(colors)]
                self.barriers.append(Barrier(x, y, color))

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.paddle.move_left, "Left")
        self.screen.onkey(self.paddle.move_right, "Right")

    def update_score(self, points):
        self.score += points
        self.score_display.clear()
        self.score_display.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))

    def drop_bomb(self, x, y):
        self.bombs.append(Bomb(x, y))

    def drop_bonus(self, x, y):
        new_bonus = Bonus(x, y)
        self.bonuses.append(new_bonus)

    def play(self):
        game_over = False
        self.input_name()

        while not game_over:
            self.setup_controls()
            self.screen.update()
            self.ball.move()

            # Ball collision with walls
            if self.ball.ball.xcor() > 390 or self.ball.ball.xcor() < -390:
                self.ball.bounce_x()

            if self.ball.ball.ycor() > 290:
                self.ball.bounce_y()

            # Ball collision with paddle
            if (self.ball.ball.ycor() - 13.5 < -240 and self.ball.ball.ycor() - 13.5 > -250) and \
                    (self.paddle.paddle.xcor() - 100 < self.ball.ball.xcor() - 13.5 < self.paddle.paddle.xcor() + 100):
                self.ball.bounce_y()

            # Ball collision with barriers
            for barrier in self.barriers:
                if barrier.visible() and \
                        (barrier.barrier.xcor() - 20 < self.ball.ball.xcor() < barrier.barrier.xcor() + 20) and \
                        (barrier.barrier.ycor() - 20 < self.ball.ball.ycor() < barrier.barrier.ycor() + 20):
                    barrier.hide()
                    self.barriers.remove(barrier)
                    self.ball.bounce_y()
                    self.update_score(10)

                    # Drop bomb with 30% chance
                    if random.random() < 0.30:
                        self.drop_bomb(barrier.barrier.xcor(), barrier.barrier.ycor())
                        break

                    if random.random() < 0.30:
                        self.drop_bonus(barrier.barrier.xcor(), barrier.barrier.ycor())
                        break

            # Check for game win
            if not self.barriers:
                self.win()

            # Check if ball falls below the paddle
            if self.ball.ball.ycor() < -300:
                game_over = True
                self.end_out()

            # Move bonuses
            for bonus in self.bonuses:
                bonus.move()
                turtle.update()

                # Remove bonus if it falls out of bounds
                if bonus.out_bounds():
                    bonus.bonus.hideturtle()
                    self.bonuses.remove(bonus)

                # Bonus collision with paddle
                if (bonus.bonus.ycor() - 13.5 < -240 and bonus.bonus.ycor() - 13.5 > -250) and \
                        (self.paddle.paddle.xcor() - 100 < bonus.bonus.xcor() - 13.5 < self.paddle.paddle.xcor() + 100):
                    self.update_score(30)
                    bonus.bonus.hideturtle()
                    self.bonuses.remove(bonus)

            # Move bombs
            for bomb in self.bombs:
                bomb.move()

                # Remove bomb if it falls out of bounds
                if bomb.out_bounds():
                    bomb.bomb.hideturtle()
                    self.bombs.remove(bomb)

                # Bomb collision with paddle
                if (bomb.bomb.ycor() - 13.5 < -240 and bomb.bomb.ycor() - 13.5 > -250) and \
                        (self.paddle.paddle.xcor() - 100 < bomb.bomb.xcor() - 13.5 < self.paddle.paddle.xcor() + 100):
                    self.end_bomb()
                    game_over = True

    def end_bomb(self):
        self.screen.clear()
        self.screen.bgcolor("cornsilk2")
        game_over_text = turtle.Turtle()
        game_over_text.color("DarkRed")
        game_over_text.hideturtle()
        game_over_text.write(f"\nGame Over! \n \nBomb hit the paddle\n \n{self.name}'s "
                             f"Score: {self.score}", align="center", font=("Arial", 36, "bold"))
        self.screen.mainloop()

    def end_out(self):
        self.screen.clear()
        self.screen.bgcolor("cornsilk2")
        game_over_text = turtle.Turtle()
        game_over_text.color("DarkRed")
        game_over_text.hideturtle()
        game_over_text.write(f"\nGame Over!\n \nYou missed the ball\n \n{self.name}'s "
                             f"Score: {self.score}", align="center", font=("Arial", 36, "bold"))
        self.screen.mainloop()

    def win(self):
        self.screen.clear()
        self.screen.bgcolor("DarkGoldenrod2")
        game_over_text = turtle.Turtle()
        game_over_text.color("DarkRed")
        game_over_text.hideturtle()
        game_over_text.write(f"\n{self.name} WIN\n \nFinal Score: {self.score}",
                             align="center", font=("Arial", 36, "bold"))
        self.screen.mainloop()

game = Run_game()
game.play()
