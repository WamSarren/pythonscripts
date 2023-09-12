# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:17:31 2022
# Pong
@author: Sam Warren
"""
import turtle
# Screen
wn = turtle.Screen()
wn.title("Pong by Sam Warren")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Ball hit
ball_hit = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto((-350, 0))

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto((350, 0))

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Pen streak
streak_pen = turtle.Turtle()
streak_pen.speed(0)
streak_pen.color("white")
streak_pen.penup()
streak_pen.hideturtle()
streak_pen.goto(0,220)
streak_pen.write("Streak: 0", align="center", font=("Courier", 24, "normal"))



# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        streak_pen.clear()
        ball_hit = 0
        streak_pen.write("Streak: 0", align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        streak_pen.clear()
        ball_hit = 0
        streak_pen.write("Streak: 0", align="center", font=("Courier", 24, "normal"))
        
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
            
    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)
            
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    
    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)
        
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        ball_hit += 1
        streak_pen.clear()
        streak_pen.write("Streak: {}".format(ball_hit), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        ball_hit += 1
        streak_pen.clear()
        streak_pen.write("Streak: {}".format(ball_hit), align="center", font=("Courier", 24, "normal"))
        
    # Speed increase
    if ball_hit >= 3:
        ball.setx(ball.xcor() + ball.dx * 1.1)
        ball.sety(ball.ycor() + ball.dy * 1.1)