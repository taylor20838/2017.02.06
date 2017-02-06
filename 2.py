# -*- coding: utf8 -*-
import turtle               # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()        # 產生畫布以進行畫圖
john = turtle.Turtle()# 建立一個海龜turtle，它的名字叫john

for i in range(5):
    colors = ["yellow", "red", "purple", "blue","pink"]
for pen_color in colors:
    john.color(pen_color)
    john.forward(100)
    john.right(144)

window.exitonclick() 
