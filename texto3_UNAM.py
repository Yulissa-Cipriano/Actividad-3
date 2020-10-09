import turtle

t=turtle.Turtle()
can = turtle.Screen()

tam=16
t.color("green","white")

for i in range(80):
    
    can.clear()
    can.bgcolor("midnightblue")
    t.write("U N A M", move=False, align="center", font=("Verdana", tam, "normal", 'italic', 'bold'))
    turtle.delay(100)
    t.forward(8)
    t.backward(8)
    
    tam+=1
    

