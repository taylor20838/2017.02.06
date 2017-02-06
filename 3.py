import turtle

def draw_multicolor_square(t, sz):
        for i in ["hotpink","hotpink","hotpink","hotpink"]:
                t.color(i)
                t.forward(sz)
                t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

john = turtle.Turtle()
john.pensize(3)

size = 100
for i in range(5):
    draw_multicolor_square(john, size)
    john.right(18)
 

window.exitonclick()
