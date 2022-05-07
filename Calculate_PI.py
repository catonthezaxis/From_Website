import matplotlib.pyplot as plt
import numpy as np
import random
import math
import turtle

def draw_board(circle_radius):
    myPen.up()
    myPen.setposition(-1*circle_radius, -1*circle_radius)
    myPen.down()
    for i in range(4):
        myPen.fd(circle_radius * 2)
        myPen.left(90)
    myPen.up()
    
    #draw the circle
    myPen.setposition(0, -1 * circle_radius)
    myPen.down()
    myPen.circle(circle_radius)


myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)

circle_radius = 300
in_circle = 0
out_circle = 0
n = 10
m = 1000
calculated_pi = []


draw_board(circle_radius)

for i in range(n):
    for j in range(m):
        x = random.randrange(-1 * circle_radius, circle_radius)
        y = random.randrange(-1 * circle_radius, circle_radius)
        
        if (x**2 + y**2 > circle_radius**2):
            myPen.color('black')
            myPen.up()
            myPen.goto(x, y)
            myPen.down()
            myPen.dot()
            out_circle += 1
        else:
            myPen.color('red')
            myPen.up()
            myPen.goto(x, y)
            myPen.down()
            myPen.dot()
            in_circle += 1
        pi_value = 4 * in_circle /(in_circle + out_circle)
        calculated_pi.append(pi_value)
    print('after {} iterations, the calculated pi value is {}'.format((i+1)*m, pi_value))
    
pi_errors = [abs(math.pi - pi) for pi in calculated_pi]


fig, a = plt.subplots(1,2,figsize = (11, 5))
a[0].axhline(y = math.pi, color = 'r', linestyle = '-')
a[0].plot(calculated_pi)
a[0].set_xlabel('Iterations')
a[0].set_ylabel('Calcualted PI')

a[1].axhline(y = 0, color = 'r', linestyle = '-')
a[1].plot(pi_errors)
a[1].set_xlabel('Iterations')
a[1].set_ylabel('Error')
plt.show()


    
