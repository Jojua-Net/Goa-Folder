#print("Vaxtang Jojua")

#print(5)
#print("5")

#print(5 + int("5"))


#print("Vaxtang Jojua " + "5" + " wlis")


from turtle import *

# we wanto to paint a house


#step 1: draw a square
speed(30)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)
penup()
goto(60, 180)
pendown()
color("yellow")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()




left(0)
penup()
goto(140, 180)
pendown()
color("yellow")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


color("green")

exitonclick()