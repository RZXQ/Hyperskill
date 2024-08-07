# 导入turtle库，并用t作为别名
import turtle as t

# 设置背景图片，图片名称为bg.gif
t.bgpic('bg.gif')
# 设置窗口大小，宽为1000，高为500
t.setup(1000, 500)
# 绘制支撑杆
t.penup()
t.goto(40, 100)
t.pendown()
t.right(90)
t.pensize(10)
t.color('gray', 'gray')
t.forward(180)
# 绘制菱形扇叶
t.backward(180)
t.right(30)
t.pensize(3)
t.color('black', 'silver')
i = 0
while i < 3:
    t.begin_fill()
    t.forward(80)
    t.right(60)
    t.forward(80)
    t.right(120)
    t.forward(80)
    t.right(60)
    t.forward(80)
    t.end_fill()
    i = i + 1
# 绘制固定点
t.dot(15, 'white')
# 书写文字
t.penup()
t.goto(-260, 160)
t.pendown()
t.write('风叶时时转不停', font=('微软雅黑', 15))
t.penup()
t.goto(-260, 120)
t.pendown()
t.write('任劳任怨一生行', font=('微软雅黑', 15))
t.penup()
t.goto(-260, 80)
t.pendown()
t.write('无私奉献非求报', font=('微软雅黑', 15))
t.penup()
t.goto(-260, 40)
t.pendown()
t.write('造福人寰留美名', font=('微软雅黑', 15))
# 窗口暂停展示
t.done()
