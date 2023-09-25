from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("Yojjal's Snake👀👀👀")
screen.tracer(0)

import time
segments = []


#square making as a snake

snake = Snake()  
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)

    snake.move()

    #DETECT collison with foood.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #detect collison
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() >290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
        
    #Detect collison with tail
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()
    ## if head collides with any segment in the tail:   
        #trigger game_over
    

screen.exitonclick()



