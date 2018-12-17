#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml import sax
import turtle

class MoveHandler(sax.ContentHandler): #继承ContentHandler类
    def __init__(self):
        sax.ContentHandler.__init__(self)
        self._content = ""
        self._tag = ""

    def startElement(self,name,attrs): #读取开始标签
        self._tag = name
        if name == "trace":
            print("begin trace")
            print("设定初始值")          #初始化绘制基本参数
            t = turtle.Pen()
            t.pensize(5)
            t.pencolor("blue")
        if name == "beginspot":
            print("begin beginspot")
        if name == "step":
            print("begin step")

    def endElement(self,name):          #读取结束标签和标签内的内容
        if name == "trace":
            print("end trace")
            t.done()
        if name == "beginspot":                     #读取起始坐标
            print("beginspot is "+self._content)
            coordinate = self._content.split(",")
            print(coordinate)
            self.x = int(coordinate[0])
            self.y = int(coordinate[1])
            print("x is " + str(self.x))
            print("y is " + str(self.y))
            t.penup()
            t.goto(self.x, self.y)
            t.pencolor("green")
            t.pendown()
            if self.x >= 0 and self.x <=30 and self.y >= 0 and self.y <= 30:    #判断起始坐标是否在30*30范围
                print("ready to trace")
            else:
                print("请设定起始坐标在30*30的范围内")###########如果不在范围内程序可能仍会运行#
        if name == "step":                                  #判断移动方向，并按照相应方向进行坐标计算
            print("step is "+self._content)                 #超出30*30就会撞墙
            if self._content == "up":
                self.y = self.y +1
                if self.y >= 0 and self.y <= 30:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    t.goto(self.x,self.y)
                else:
                    print("hit wall")
                    t.penup()
                    t.done()

            if self._content == "down":
                self.y = self.y - 1
                if self.y >= 0 and self.y <= 30:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    t.goto(self.x, self.y)
                else:
                    print("hit wall")
                    t.penup()
                    t.done()

            if self._content == "left":
                self.x = self.x -1
                if self.x >= 0 and self.x <= 30:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    t.goto(self.x, self.y)
                else:
                    print("hit wall")
                    t.penup()
                    t.done()

            if self._content == "right":
                self.x = self.x +1
                if self.x >= 0 and self.x <= 30:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    t.goto(self.x, self.y)
                else:
                    print("hit wall")
                    t.penup()
                    t.done()

            if self._content == "leftup":
                self.x = self.x -1
                self.y = self.y +1
                if self.x >= 0 and self.x <= 30 and self.y >= 0 and self.y <= 30:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    t.goto(self.x, self.y)
                else:
                    print("hit wall")
                    t.penup()
                    t.done()

            if self._content == "leftdown":
                self.y = self.y -1
                self.x = self.x -1
                if self.x >= 0 and self.x <= 30 and self.y >= 0 and self.y <= 30:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    t.goto(self.x, self.y)
                else:
                    print("hit wall")
                    t.penup()
                    t.done()

            if self._content == "rightup":
                self.y = self.y +1
                self.x = self.x +1
                if self.x >= 0 and self.x <= 30 and self.y >= 0 and self.y <= 30:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    t.goto(self.x, self.y)
                else:
                    print("hit wall")
                    t.penup()
                    t.done()

            if self._content == "rightdown":
                self.y = self.y -1
                self.x = self.x +1
                if self.x >= 0 and self.x <= 30 and self.y >= 0 and self.y <= 30:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    t.goto(self.x, self.y)
                else:
                    print("hit wall")
                    t.penup()
                    t.done()

            # ###########################################
    def characters(self,content):
        self._content = content

if __name__ == "__main__":
    handler = MoveHandler()
    #sax.parse("eightDirctions.xml",handler)
    sax.parse("testHitWall.xml", handler)