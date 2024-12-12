from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.direction = 90
        self.shape("turtle")
        self.penup()
        self.setheading(self.direction)
        self.goto(STARTING_POSITION)
        self.xbound = list(range(int(self.xcor())-10, int(self.xcor())+10))
        self.ybound = list(range(int(self.ycor())-10, int(self.ycor())+10))
    
    def turn_north(self):
        if self.heading == 90 or self.heading == 270:
            self.move()
        else:
            self.direction = 90
            self.setheading(self.direction)
            self.move()

    def turn_west(self):
        if self.heading == 180 or self.heading == 0:
            self.move()
        else:
            self.direction = 180
            self.setheading(self.direction)
            self.move()

    def turn_south(self):
        if self.heading == 270 or self.heading == 90:
            self.move()
        else:
            self.direction = 270
            self.setheading(self.direction)
            self.move()

    def turn_east(self):
        if self.heading == 180 or self.heading == 0:
            self.move()
        else:
            self.direction = 0
            self.setheading(self.direction)
            self.move()

    def move(self):
        self.forward(MOVE_DISTANCE)
        self.xbound = list(range(int(self.xcor())-10, int(self.xcor())+10))
        self.ybound = list(range(int(self.ycor())-10, int(self.ycor())+10))

    def player_reset(self):
        self.goto(STARTING_POSITION)