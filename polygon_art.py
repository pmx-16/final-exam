import turtle
import random

class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def reposition(self):
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

class ArtSimulator:
    def __init__(self, num_polygon):
        self.num_polygon = num_polygon
        self.polygon_list = []
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for i in range(self.num_polygon):
            num_sides = random.randint(3, 5)  # triangle, square, or pentagon
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            border_size = random.randint(1, 10)
            self.polygon_list.append(Polygon(num_sides, size, orientation, location, color, border_size))



    def run(self):
        while (True):
            turtle.clear
            for j in range(num_polygon):
                self.polygon_list[j].draw_polygon()
                self.polygon_list[j].reposition()
            turtle.update()
        # hold the window; close it by clicking the window close 'x' mark
        turtle.done

num_polygon = random.randint(0, 10)
my_sim = ArtSimulator(num_polygon)
my_sim.run()

