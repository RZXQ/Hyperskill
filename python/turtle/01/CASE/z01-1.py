import turtle as t

t.bgpic('bg.gif')
t.setup(800, 600)
t.pensize(20)
# 绘制第一个蓝色圆环
t.penup()
t.goto(-240, 200)
t.pendown()
t.pencolor('blue')
t.circle(-100)
# 绘制第二个金色圆环
t.penup()
t.goto(-120, 100)
t.pendown()
t.color('yellow')
t.circle(-100)
# 绘制第三个黑色圆环
t.penup()
t.goto(0, 200)
t.pendown()
t.color('black')
t.circle(-100)
# 绘制第四个绿色圆环
t.penup()
t.goto(120, 100)
t.pendown()
t.color('green')
t.circle(-100)
# 绘制第五个红色的圆环
t.penup()
t.goto(240, 200)
t.pendown()
t.color('red')
t.circle(-100)
# 补蓝色圆环
t.penup()
t.goto(-240, 200)
t.pendown()
t.pencolor('blue')
t.circle(-100, 120)
# 补黄色圆环
t.penup()
t.goto(-120, 100)
t.pendown()
t.setheading(0)
t.color('yellow')
t.circle(-100, 45)
# 补黑色圆环
t.penup()
t.goto(0, 200)
t.pendown()
t.setheading(0)
t.color('black')
t.circle(-100, 120)
# 补绿色圆环
t.penup()
t.goto(120, 100)
t.pendown()
t.setheading(0)
t.color('green')
t.circle(-100, 45)

t.done()
