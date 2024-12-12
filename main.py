import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT =600
SLEEP_TIME = 0.1
INIT_NUMBER_OF_CARS = 20
screen = Screen()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

car_manager = CarManager(INIT_NUMBER_OF_CARS)
player = Player()
scoreboard = Scoreboard((-250,250))
sleep_time = SLEEP_TIME

screen.onkey(key="Up", fun=player.turn_north)
screen.onkey(key="Right", fun=player.turn_east)
screen.onkey(key="Down", fun=player.turn_south)
screen.onkey(key="Left", fun=player.turn_west)

screen.listen()
game_over = False
while not game_over:
    time.sleep(sleep_time)
    # do the things
    car_manager.move_cars()
    #check collisions
    game_over = car_manager.detect_collision(player)
    if (player.ycor()+20)>=SCREEN_HEIGHT/2:
        scoreboard.add_level()
        sleep_time *= 0.9
        player.player_reset()
    #update the screen
    screen.update()
scoreboard.game_over()
screen.exitonclick()