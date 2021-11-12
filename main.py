import turtle
import math
# comment for push test

def graph(n):
    for line in range(1, n):
        angle = 180 / n
        arc = circumference / n * line
        chord = 2 * rad * math.sin(arc/(2*rad))

        t.left(angle)
        t.forward(chord)
        position.append(t.position())
        t.penup()
        t.backward(chord)
        t.pendown()

    for nextVertex in range(0, len(position)):
        t.penup()
        t.goto(position[0])
        for nextLine in range(0, len(position)):
            t.pendown()
            t.goto(position[nextLine])
            t.penup()
            if len(position) > 2:
                t.goto(position[0])
                t.pendown()

        del position[0]


numOfVertex = int(input("Number of vertices: ") or "3")
if numOfVertex < 3:
    numOfVertex = 3

rad = 250
circumference = 2 * math.pi * rad

turtle.screensize(1000, 1000)
s = turtle.getscreen()
s.clear()

t = turtle.Turtle()
t.hideturtle()
t.speed(100000)
t.penup()
t.goto(rad, 0)

t.pendown()
t.left(90)

position = []

graph(numOfVertex)
print("Done")
turtle.done()
