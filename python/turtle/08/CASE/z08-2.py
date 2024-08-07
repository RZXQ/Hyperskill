# 导入turtle库，并用t作为别名
import turtle as t

# 设置背景图片，图片名称为bg.gif
t.bgpic('bg.gif')
# 设置窗口大小，宽为729，高为700
t.setup(729, 700)
# 绘制脸的轮廓
t.pensize(10)
t.color('yellow', 'yellow')
t.begin_fill()
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(200)
t.end_fill()
# 绘制腮红
t.left(90)
t.color('pink', 'pink')
t.penup()
t.goto(-115, 95)
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.goto(115, 95)
t.pendown()
t.begin_fill()
t.circle(-40)
t.end_fill()
# 绘制左眼
# 眼眶
t.color('grey', 'white')
t.penup()
t.goto(-40, 152)
t.pendown()
t.begin_fill()
t.circle(45)
t.end_fill()
# 眼仁
t.color('grey', 'grey')
t.begin_fill()
t.circle(45, -180)
t.end_fill()
# 绘制右眼
# 眼眶
t.setheading(90)
t.color('grey', 'white')
t.penup()
t.goto(40, 152)
t.pendown()
t.begin_fill()
t.circle(-45)
t.end_fill()
# 眼仁
t.color('grey', 'grey')
t.begin_fill()
t.circle(-45, -180)
t.end_fill()
# 绘制嘴巴

# 窗口暂停展示
t.done()
