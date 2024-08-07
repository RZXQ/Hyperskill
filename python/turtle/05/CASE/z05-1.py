import turtle as t

t.bgpic('bg.gif')
t.setup(933, 700)
# 红色国旗面
t.penup()
t.goto(-250, 0)
t.pendown()
t.color('red', 'red')
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(300)
t.left(90)
t.forward(500)
t.left(90)
t.forward(300)
t.left(90)
t.end_fill()

# 大五角星
t.penup()
t.goto(-220, 220)
t.pendown()
t.color('yellow', 'yellow')
t.begin_fill()
i = 1
while i <= 5:
    t.forward(88)
    t.right(144)
    i = i + 1
t.end_fill()
# 第1颗小五角星
t.penup()
t.goto(-96, 282)
t.pendown()
t.color('yellow', 'yellow')
t.setheading(260)
t.begin_fill()
i = 1
while i <= 5:
    t.forward(30)
    t.right(144)
    i = i + 1
t.end_fill()
# 第2颗小五角星
t.penup()
t.goto(-78, 216)
t.setheading(30)
t.color('yellow', 'yellow')
t.pendown()
t.begin_fill()
i = 1
while i <= 5:
    t.forward(30)
    t.right(144)
    i = i + 1
t.end_fill()
# 第3颗小五角星
t.penup()
t.goto(-78, 166)
t.setheading(3)
t.pendown()
t.color('yellow', 'yellow')
t.begin_fill()
i = 1
while i <= 5:
    t.forward(30)
    t.right(144)
    i = i + 1
t.end_fill()
# 第4颗小五角星
t.penup()
t.goto(-120, 130)
t.setheading(330)
t.pendown()
t.color('yellow', 'yellow')
t.begin_fill()
i = 1
while i <= 5:
    t.forward(30)
    t.right(144)
    i = i + 1
t.end_fill()
t.hideturtle()
t.done()
