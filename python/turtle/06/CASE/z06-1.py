import turtle as t

t.bgpic('bg.gif')
t.setup(700, 700)
# 绘制黄色的圆
t.penup()
t.goto(0, -300)
t.pendown()
t.color('yellow', 'yellow')
t.begin_fill()
t.circle(230)
t.end_fill()
# 绘制橙色的圆环
t.pensize(25)
t.penup()
t.goto(0, -270)
t.pendown()
t.color('orange')
t.circle(200)
# 绘制五角星
t.penup()
t.goto(-130, -30)
t.pendown()
t.color('gold', 'gold')
t.begin_fill()
i = 1
while i <= 5:
    t.forward(260)
    t.right(144)
    i = i + 1
t.end_fill()
t.done()
