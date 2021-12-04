import turtle
radius = 20
turtle.fillcolor("red")
turtle.begin_fill()

while radius <= 80:
      radius+=10
      turtle.circle(radius)
turtle.end_fill()    