from turtle import Turtle, screensize, getscreen, done
import math


def draw_graph(n):
    # radius and circumference of the circle which the regular graph will be contained in
    rad = 250
    circumference = 2 * math.pi * rad

    screensize(1000, 1000)  # define the screen size
    screen = getscreen()  # open the window for the user
    screen.clear()  # delete arrow sprite

    turtle_pen = Turtle()  # init a turtle to draw with
    # turtle_pen.hideturtle()  # hide the turtle while drawing
    turtle_pen.speed(10)  # max speed
    turtle_pen.penup()  # up to not draw straight line

    # go to x coordinate equal to the radius of the circle the graph is contained in
    # y coordinate 0
    turtle_pen.goto(rad, 0)

    # pen down and prepare to draw
    turtle_pen.pendown()

    # rotate 90 degrees to tangent the circle
    turtle_pen.left(90)

    # list of positions of all vertices
    # which must still be travelled to
    positions: list[tuple[float, float]] = []

    # ALL INITIAL VERTICES
    for line in range(1, n):
        # calculate the distance to rotate from the starting point tangent line
        angle = 180 / n

        # calculate the arc length based on number of vertices
        # and based on what line we are drawing
        arc = circumference / n * line

        # calculate chord length, or length of line
        # see also: https://en.wikipedia.org/wiki/Chord_(geometry)
        chord = 2 * rad * math.sin(arc/(2*rad))

        turtle_pen.left(angle)
        turtle_pen.forward(chord)

        positions.append(turtle_pen.position())

        turtle_pen.penup()
        turtle_pen.backward(chord)
        turtle_pen.pendown()

    for nextVertex in range(0, len(positions)):
        turtle_pen.penup()
        turtle_pen.goto(positions[0])
        for nextLine in range(0, len(positions)):
            turtle_pen.pendown()
            turtle_pen.goto(positions[nextLine])
            turtle_pen.penup()
            if len(positions) > 2:
                turtle_pen.goto(positions[0])
                turtle_pen.pendown()

        del positions[0]


def main():
    # ask the user for the number of vertices their regular graph should have
    num_of_vertex = int(input("Number of vertices: ") or "3")

    # default the number of vertices to three
    if num_of_vertex < 3:
        num_of_vertex = 3

    draw_graph(num_of_vertex)
    print("Done")
    done()


if __name__ == "__main__":
    main()
