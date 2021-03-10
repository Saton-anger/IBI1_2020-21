#倒入海龟绘图模块
import turtle
t = turtle.Pen()
#这是一个循环
for x in range(360):
    t.forward(x)
    t.left(59)
#解释器
'''
    1.三个单引号表示段注释
    2.# 表示行注释
    3.59可以换成其他数字
'''
