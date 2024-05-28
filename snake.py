import random
import turtle
import time

delay = 0.1

#score
score=0
high_score = 0

#setting up the screen
t=turtle.Screen()
t.title("Snake game")
t.bgcolor("blue")
t.setup(width=600, height=600)
t.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,100)
food.direction ="stop"

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0   High Score: 0" , align="center", font=("Courier", 24, "normal"))

#funtion

def go_up():
    if head.direction != "down":
        head.direction="up"
def go_down():
    if head.direction != "up":
       head.direction="down"
def go_left():
    if head.direction != "right":
        head.direction="left"
def go_right():
    if head.direction != "left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
#keyboard binding
t.listen()
t.onkeypress(go_up, "w")
t.onkeypress(go_down, "s")
t.onkeypress(go_left, "a")
t.onkeypress(go_right, "d")

#main game Look

while True:
    t.update()

    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide segment(reset)
        for i in segments:
            i.goto(1000,1000)
        #clear segment list
        segments.clear()

        #reset score
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))



    #checking for collision with food
    if head.distance(food)<20:
        #move food randomply on screen
        x=random.randint(-290, 290)
        y=random.randint(-290, 290)
        food.goto(x,y)

        #add segment to snake
        add_segment = turtle.Turtle()
        add_segment.speed(0)
        add_segment.shape("square")
        add_segment.color("grey")
        add_segment.penup()
        segments.append(add_segment)

        delay-=0.001

        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
    #move the end segment first in reverse order
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    #move segment 0 to where the head is 
    if (len(segments)>0):
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #checking for head collision with other body part of snake
    for i in segments:
        if i.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide segment(reset)
            for i in segments:
                i.goto(1000,1000)
            #clear segment list
            segments.clear()
            score =0
            delay=0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))



    time.sleep(delay)

t.mainloop()