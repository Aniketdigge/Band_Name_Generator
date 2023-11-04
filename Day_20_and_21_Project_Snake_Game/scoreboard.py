from turtle import Turtle
FONT = ('Arial', 14, 'bold')
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("White")
        self.goto(0, 270)
        self.hideturtle()
        self.Updat_score()

    def Updat_score(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.Updat_score()
        
        