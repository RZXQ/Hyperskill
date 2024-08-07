# 导入turtle库，并用t作为别名
import turtle as t

# 设置背景图片，图片名称为bg.gif
t.bgpic('bg.gif')
# 设置窗口大小，宽为1003，高为600
t.setup(1003, 600)
# 绘制风车杆
t.right(90)
t.pensize(15)
t.color('gray', 'gray')
t.forward(260)
t.backward(260)
# 变量存储输入的扇叶数
n = int(t.numinput('风车扇叶数', '建议范围3-15之间：'))
# 绘制扇叶
t.left(160)
t.pensize(2)
t.color('black', 'orange')
i = 0
while i < n:
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.circle(75, 180)
    t.end_fill()
    i = i + 1
    t.left(90)
    t.left(360 / n)
# 绘制固定点
t.dot(30, 'white')
# 窗口暂停展示
t.done()
