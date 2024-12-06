import turtle

class Ball:
    def __init__(self, color, size, x, y, xpos, ypos, vx, vy, i, canvas_width, canvas_height, ball_radius):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.i = i
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius

    def draw_ball(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x,self.y-self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self, dt):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[self.i] += self.vx[self.i]*dt
        self.ypos[self.i] += self.vy[self.i]*dt


    def update_ball_velocity(self):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[self.i]) > (self.canvas_width - self.ball_radius):#check self.x xpos
            self.vx[self.i] = -self.vx[self.i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[self.i]) > (self.canvas_height - self.ball_radius):
            self.vy[self.i] = -self.vy[self.i]



