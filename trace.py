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
            turtle.screensize(3000, 3000, "white")
            turtle.Pen()
            turtle.pensize(5)
            turtle.pencolor("blue")
        if name == "beginspot":
            print("begin beginspot")
        if name == "step":
            print("begin step")

    def endElement(self,name):          #读取结束标签和标签内的内容
        if name == "trace":
            print("end trace")
            turtle.done()
        if name == "beginspot":                     #读取起始坐标
            print("beginspot is "+self._content)
            coordinate = self._content.split(",")
            print(coordinate)
            self.x = int(coordinate[0])
            self.y = int(coordinate[1])
            print("x is " + str(self.x))
            print("y is " + str(self.y))
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.pencolor("green")
            turtle.pendown()
            if self.x >= 0 and self.x <=3000 and self.y >= 0 and self.y <= 3000:    #判断起始坐标是否在3000*3000范围
                print("ready to trace")
            else:
                print("请设定起始坐标在3000*3000的范围内")
        if name == "step":                                  #判断移动方向，并按照相应方向进行坐标计算
            print("step is "+self._content)                 #超出3000*3000就会撞墙
            if self.x >= 0 and self.x <= 3000 and self.y >= 0 and self.y <= 3000:
                if self._content == "up":
                    self.y = self.y +100
                    #if self.y >= 0 and self.y <= 3000:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    if self.y > 3000:
                        print("hit wall! cannot move like this!")
                    else:
                        turtle.goto(self.x,self.y)
                    # else:
                    #     print("hit wall")
                    #     turtle.penup()
                    #     turtle.done()

                if self._content == "down":
                    self.y = self.y - 100
                    #if self.y >= 0 and self.y <= 3000:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    if self.y < 0:
                        print("hit wall! cannot move like this!")
                    else:
                        turtle.goto(self.x, self.y)
                    # else:
                    #     print("hit wall")
                    #     turtle.penup()
                    #     turtle.done()

                if self._content == "left":
                    self.x = self.x -100
                    #if self.x >= 0 and self.x <= 3000:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    if self.x< 0:
                        print("hit wall! cannot move like this!")
                    else:
                        turtle.goto(self.x, self.y)
                    # else:
                    #     print("hit wall")
                    #     turtle.penup()
                    #     turtle.done()

                if self._content == "right":
                    self.x = self.x +100
                    #if self.x >= 0 and self.x <= 3000:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    if self.x>3000:
                        print("hit wall! cannot move like this!")
                    else:
                        turtle.goto(self.x, self.y)
                    # else:
                    #     print("hit wall")
                    #     turtle.penup()
                    #     turtle.done()

                if self._content == "leftup":
                    self.x = self.x -100
                    self.y = self.y +100
                    #if self.x >= 0 and self.x <= 3000 and self.y >= 0 and self.y <= 3000:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    if self.x<0 or self.y >3000:
                        print("hit wall! cannot move like this!")
                    else:
                        turtle.goto(self.x, self.y)
                    # else:
                    #     print("hit wall")
                    #     turtle.penup()
                    #     turtle.done()

                if self._content == "leftdown":
                    self.y = self.y -100
                    self.x = self.x -100
                    #if self.x >= 0 and self.x <= 3000 and self.y >= 0 and self.y <= 3000:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    if self.x<0 or self.y <0:
                        print("hit wall! cannot move like this!")
                    else:
                        turtle.goto(self.x, self.y)
                    # else:
                    #     print("hit wall")
                    #     turtle.penup()
                    #     turtle.done()

                if self._content == "rightup":
                    self.y = self.y +100
                    self.x = self.x +100
                    #if self.x >= 0 and self.x <= 3000 and self.y >= 0 and self.y <= 3000:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    if self.x>3000 or self.y >3000:
                        print("hit wall! cannot move like this!")
                    else:
                        turtle.goto(self.x, self.y)
                    # else:
                    #     print("hit wall")
                    #     turtle.penup()
                    #     turtle.done()

                if self._content == "rightdown":
                    self.y = self.y -100
                    self.x = self.x +100
                    #if self.x >= 0 and self.x <= 3000 and self.y >= 0 and self.y <= 3000:
                    print("x is " + str(self.x))
                    print("y is " + str(self.y))
                    if self.y<0 or self.x >3000:
                        print("hit wall! cannot move like this!")
                    else:
                        turtle.goto(self.x, self.y)
                    # else:
                    #     print("hit wall")
                    #     turtle.penup()
                    #     turtle.done()
            else:
                print("hit wall! cannot move like this!")
                turtle.penup()
                turtle.done()

            # ###########################################
    def characters(self,content):
        self._content = content

if __name__ == "__main__":
    handler = MoveHandler()
    #sax.parse("eightDirctions.xml",handler)
    sax.parse("testHitWall.xml", handler)
    #sax.parse("testAllDict.xml",handler)