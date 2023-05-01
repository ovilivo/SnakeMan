from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.evolve_at(position)

    def evolve_at(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.turtles.append(turtle)




    def evolve(self):
        self.evolve_at(self.turtles[-1].position())


    def move(self):
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
