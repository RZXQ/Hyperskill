import turtle as t

t.bgpic('bg1.gif')
t.setup(1600, 800)
t.penup()
t.goto(300, -300)
t.pendown()
# 绘制右半边的黑色大半圆
t.color("black", "black")  # 画笔颜色：黑色；填充颜色：黑色
t.begin_fill()  # 确定填充开始点
t.circle(150, 180)
t.circle(-150, 180)
t.circle(-300, 180)
t.end_fill()  # 确定填充结束点，开始填充
# 绘制左半边的大圆
t.circle(-300, 180)

# 绘制第一个小圆
t.penup()  # 抬笔，移动时不会留下痕迹
t.goto(240, -180)  # 移动到坐标(0,25)的位置
t.pendown()  # 落笔，准备绘制
t.color('black')  # 设置画笔颜色
t.begin_fill()
t.circle(35)  # 绘制半径为20的圆
t.end_fill()

# 绘制第二个小圆		
t.penup()  # 抬笔，移动时不会留下痕迹
t.goto(370, 115)  # 移动到指定坐标
t.pendown()  # 落笔，准备绘制
t.color("black", "white")  # 设置画笔颜色为黑色，填充色为白色
t.begin_fill()
t.circle(35)  # 绘制半径为20的圆
t.end_fill()
t.hideturtle()
t.done()
