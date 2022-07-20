from math import pi, sin
from turtle import Turtle, screensize, getscreen, done, TurtleScreen


def draw_graph(vertices: int) -> None:
    # radius and circumference of the circle which the regular graph will be contained in
    rad: int = 250
    circumference: float = 2 * pi * rad

    screensize(1000, 1000)  # define the screen size
    screen: TurtleScreen = getscreen()  # open the window for the user
    screen.clear()  # delete arrow sprite

    turtle_pen: Turtle = Turtle()  # init a turtle to draw with
    turtle_pen.hideturtle()  # hide the turtle while drawing
    turtle_pen.speed(10)  # max speed
    turtle_pen.penup()  # up to not draw any lines during setup

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

    # calculate the degrees to rotate
    # each time we draw a new line
    angle: float = 180 / vertices

    # ALL INITIAL VERTICES
    # draw all lines from initial point
    # and save positions of all the other vertices
    for line in range(1, vertices):
        # calculate the arc length based on number of vertices
        # and based on what line we are drawing
        arc: float = circumference / vertices * line

        # calculate chord length, or length of line
        # see also: https://en.wikipedia.org/wiki/Chord_(geometry)
        chord: float = 2 * rad * sin(arc / (2 * rad))

        # rotate to the angle the next chord is at
        # and draw the chord
        turtle_pen.left(angle)
        turtle_pen.forward(chord)

        # save position after motion
        # the endpoint of each chord is the location for a vertex
        positions.append(turtle_pen.position())

        # pen up and return to original position
        # and pen down to prepare for next line
        turtle_pen.penup()
        turtle_pen.backward(chord)
        turtle_pen.pendown()

    # CONNECT ALL VERTICES TO EACH OTHER
    # move to the next vertex
    # and draw all its chords
    for _ in range(0, len(positions)):
        current_vertex: tuple[float, float] = positions[0]

        # pen up and move to next vertex in queue
        turtle_pen.penup()
        turtle_pen.goto(current_vertex)

        # draw all chords for current vertex
        for next_vertex in positions:
            # pen down and draw chord to next vertex
            turtle_pen.pendown()
            turtle_pen.goto(next_vertex)

            # pen up and return to current vertex
            turtle_pen.penup()
            turtle_pen.goto(current_vertex)

        # delete current vertex after all lines drawn from it
        # used to avoid visiting the same vertex twice
        del positions[0]


def main() -> None:
    # ask the user for the number of vertices their regular graph should have
    num_of_vertex: int = int(input("Number of vertices: ") or "3")

    # default the number of vertices to three
    if num_of_vertex < 3:
        num_of_vertex: int = 3

    # run regular graph algorithm
    draw_graph(num_of_vertex)

    done()  # turtle event loop


if __name__ == "__main__":
    main()
