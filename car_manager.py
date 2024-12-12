import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [1,2,3,4,5,6,7,8,9,10,11,12,13]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_WIDTH = 30
'''
CarManager
holds data and members about ALL the cars.  keeps a list of all car objects in the game.
a car lane is 25px high 
'''

class CarManager:
    
    def __init__(self, init_number_of_cars):
        self.car_list = []
        self.active_cars=[]
        for x in range(init_number_of_cars):
            newcar = Car()
            self.car_list.append(newcar)

    def move_cars(self):
        for car in self.car_list:
            car.move_car()
            if car.xcor() < -300:
                car.setx(300)
                car.lane = random.choice(LANES)
                car.reset_y()

    def detect_collision(self, player):
        self.get_active_cars(player)
        for car in self.active_cars:
            if ((int(car.ycor())+10) in player.ybound) or ((int(car.ycor())-10) in player.ybound):
                #there's been a collision
                return True
            else:
                return False


    def get_active_cars(self,player):
        self.active_cars.clear()
        for car in self.car_list:
            if ((int(car.xcor())+20) in player.xbound) or ((int(car.xcor())-20) in player.xbound):
                self.active_cars.append(car)
            else:
                pass


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.lane = random.choice(LANES)
        self.penup()
        self.setheading(180)
        self.move_distance = STARTING_MOVE_DISTANCE
        self.reset_y()
        self.setx(random.randint(-300,300))


    def move_car(self):
        self.forward(self.move_distance)


    def reset_y(self):
        self.sety((self.lane *LANE_WIDTH)-200)