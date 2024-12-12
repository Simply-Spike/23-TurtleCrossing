from turtle import Turtle

FONT = ("Courier", 24 , "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left",move=False, font=FONT)    

    def add_level(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.goto((0,0))
        self.write(f"GAME OVER", align="center",move=False, font=FONT)    
