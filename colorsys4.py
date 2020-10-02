import colorsys
import turtle

turtle.pensize(40)

hue=0.0
i = 0

while True:
    turtle.color(colorsys.hsv_to_rgb(hue, 1, 1))
    
    turtle.forward(2)
    turtle.left(1)
    
    hue+=0.0027
    i = i + 1
    if i >= 360:
        break

