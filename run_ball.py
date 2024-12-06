import turtle
import random
from ball import Ball
from seven_segments_proc import segments

class Runball:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.x = 0
        self.y = 0
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        print(self.canvas_width, self.canvas_height)

    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    def random_stuff(self):
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width +
                        self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height +
                        self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append(
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def run(self):
        dt = 0.2  # time step
        while (True):
            turtle.clear()
            Runball.draw_border()
            for i in range(self.num_balls):
                ball = Ball(self.ball_color[i], 1, self.x, self.y, self.xpos[i], self.ypos[i],
                            self.vx, self.vy, i, self.canvas_width, self.canvas_height, self.ball_radius)
                ball.draw_ball()
                ball.move_ball(dt)
                ball.update_ball_velocity()
            turtle.update()

    def run_seg(self):
        Tom = turtle.Turtle()
        tom_color = (255, 0, 0)
        segments.init(Tom, tom_color)
        delay_in_seconds = 0.2
        while True:
            for i in range(0, 10):
                seg = segments(Tom, tom_color, i)
                seg.clear(Tom)
                seg.draw(Tom, i)
                seg.my_delay(delay_in_seconds)
                turtle.update()


    def run_all():
        Runball.run()
        Runball.run_seg()


my_simulator = Runball(5)
my_simulator.random_stuff()
my_simulator.run_all()
turtle.done

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
