import turtle

turtle.pensize(2)
turtle.speed(100)
turtle.bgcolor('black')

for i in range(10):
    for colours in ['yellow', 'blue', 'white', 
                    'green', 'red', 'pink', 
                    'purple', 'brown', 'orange'
]:
        turtle.color(colours)
        turtle.circle(125)
        turtle.left(15)

turtle.hideturtle()
turtle.mainloop()