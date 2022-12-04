from turtle import *
from Paddle import paddle
from Ball import Ball
import time
from ScoreBoard import ScoreBoard

screen = Screen()
width = 800
height = 600
screen.setup(width,height)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = paddle((350,0))
l_paddle = paddle((-350,0))
ball = Ball()
ScoreBoard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made it")
        ball.bounce_x()

    if ball.xcor() > 380:
       ball.resetposition()
       ScoreBoard.r_point()

    if ball.xcor() < -380:
       ball.resetposition()
       ScoreBoard.l_point()

    if ball.xcor() < -380:
        ball.resetposition()

screen.exitonclick()
