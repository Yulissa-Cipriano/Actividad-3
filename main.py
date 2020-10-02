import colorsys
import turtle

turtle.speed(7)

t = turtle.Turtle()

for c in range(0,360,1):
  #coordenadas hsv
  h = c/100
  s = 1.0
  v = 1.0

  #convertir el color de hsv a rgb
  rgb = colorsys.hsv_to_rgb(h, s, v)

  t.color(rgb)

  t.begin_fill()
  t.circle(100)
  t.end_fill()