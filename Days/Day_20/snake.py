from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments: list = []
        self.create_snake()
        self.snake_head = []
        self.add_segment_part = False
        self.parts_added = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newXcor = self.segments[seg_num - 1].xcor()
            newYcor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newXcor, newYcor)
        self.segments[0].forward(MOVE_DISTANCE)

    def heading_up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)

    def heading_left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)

    def heading_down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)

    def heading_right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)

    def snake_head_pos(self):
        return self.segments[0].position()

    def add_segment(self):
        if self.add_segment_part:
            tail = self.segments[-1]  # current tail
            tail_x = tail.xcor()  # current tails x pos
            tail_y = tail.ycor()  # current tails y pos

            new_tail = Turtle("square")  # create new tail piece
            new_tail.color("white")
            new_tail.penup()

            if tail.heading() == 0:
                new_tail_x = tail_x - 20
                new_tail_y = tail_y
                new_tail.goto(new_tail_x, new_tail_y)
                self.segments.append(new_tail)
            elif tail.heading() == 180:
                new_tail_x = tail_x + 20
                new_tail_y = tail_y
                new_tail.goto(new_tail_x, new_tail_y)
                self.segments.append(new_tail)
            elif tail.heading() == 90:
                new_tail_x = tail_x
                new_tail_y = tail_y - 20
                new_tail.goto(new_tail_x, new_tail_y)
                self.segments.append(new_tail)
            elif tail.heading() == 270:
                new_tail_x = tail_x
                new_tail_y = tail_y + 20
                new_tail.goto(new_tail_x, new_tail_y)
                self.segments.append(new_tail)
            self.parts_added += 1

        if self.parts_added == 2:
            self.parts_added = 0
            self.add_segment_part = False
