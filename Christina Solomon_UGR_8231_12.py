import turtle
import time

display = turtle.Screen()
display.bgcolor("beige")
display.setup(width=600, height=600)
display.title("My Watch")
display.tracer(0)

tick = turtle.Turtle()
tick.hideturtle()
tick.speed(0)

hour = turtle.Turtle()
hour.hideturtle()
hour.speed(0)

min = turtle.Turtle()
min.hideturtle()
min.speed(0)

sec = turtle.Turtle()
sec.hideturtle()
sec.speed(0)


x = 0
y = -200
tick.penup()
tick.goto(x,y)
tick.pendown()
tick.pencolor("dark slate gray")
tick.pensize(3)
tick.begin_fill()
tick.fillcolor("teal")
tick.circle(200)
tick.end_fill()
tick.color('orange')

tick.penup()
tick.goto(0, 0)
tick.left(90)

for _ in range(60):
    tick.forward(194)
    tick.pencolor('navy')
    tick.pensize(4)
    tick.pendown()
    tick.pensize(4)
    tick.forward(6)
    tick.penup()
    tick.goto(0, 0)
    tick.right(6)

for i in range(12):
    tick.forward(180)
    tick.pendown()
    tick.color('orange')
    tick.forward(20)
    tick.penup()
    tick.goto(0, 0)
    tick.right(30)




num = 200
for i in range(12):
    tick.goto(2, -15)
    tick.right(30)
    tick.forward(163)
    tick.pencolor("white smoke")
    if 0x1369+i == 0x1373:
        tick.write(chr(0x1369) +""+ chr(0x1369), align="center", font=("broadway", 20, "normal"))
    elif 0x1369+i == 0x1374:
        tick.write(chr(0x1369) +" "+ chr(0x1369 + 1), align="center", font=("broadway", 20, "normal"))
    else:
        tick.write(chr(0x1369 + i), align="center", font=("broadway", 20, "normal"))
    num+=1

def draw_clock(h, m, s):
    hour.clear()
    hour.penup()
    hour.goto(0, 0)
    hour.color("aqua")
    hour.setheading(90)
    angle = (h / 12) * 360
    hour.right(angle)
    hour.pensize(5)
    hour.pendown()
    hour.forward(100)

    min.clear()
    min.penup()
    min.goto(0, 0)
    min.color("saddle brown")
    min.setheading(90)
    angle = (m / 60) * 360
    min.right(angle)
    min.pensize(4)
    min.pendown()
    min.forward(90)

    sec.clear()
    sec.penup()
    sec.goto(0, 0)
    sec.color("yellow")
    sec.setheading(90)
    angle = (s / 60) * 360
    sec.right(angle)
    sec.pensize(3)
    sec.pendown()
    sec.forward(150)

    pen=turtle.Turtle()
    pen.goto(0,0)
    pen.pensize(10)
    pen.dot()

    brand = turtle.Turtle()
    brand.penup()
    brand.goto(0,100)
    brand.hideturtle()
    brand.write("SHBAC", align="center", font=("Imprint MT Shadow", 15, "normal"))


while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h, m, s)
    display.update()
    time.sleep(1)

turtle.done()

