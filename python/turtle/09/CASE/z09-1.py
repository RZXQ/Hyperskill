import turtle as t

t.pensize(10)
# 绘制等边三角形
t.forward(90)
t.left(120)
t.forward(180)
t.left(120)
t.forward(180)
t.left(120)
t.forward(90)
# 绘制圆
t.fillcolor('blue')
t.begin_fill()
t.circle(50)
t.end_fill()
# 绘制线
t.forward(90)
t.left(120)
t.forward(180)
t.goto(0, 0)
t.done()
