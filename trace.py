#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml import sax

class MoveHandler(sax.ContentHandler): #继承ContentHandler类
    def __init__(self):
        sax.ContentHandler.__init__(self)
        self._content = ""
        self._tag = ""

    def startElement(self,name,attrs):
        self._tag = name
        if name == "trace":
            print("begin trace")
        if name == "beginspot":
            print("begin beginspot")
        if name == "step":
            print("begin step")

    def endElement(self,name):
        if name == "trace":
            print("end trace")
        if name == "beginspot":
            print("beginspot is "+self._content)
            coordinate = self._content.split(",")
            print(coordinate)
            self.x = coordinate[0]
            self.y = coordinate[1]
            print("x is " + self.x)
            print("y is " + self.y)
            print("make the original point green")
        if name == "step":
            print("step is "+self._content)
            # #以下区块是判断移动方向，并按照相应方向进行坐标计算，但是运行报错，所以暂且注释##
            # if self._content == "up":
            #     self.y = self.y  +1
            # if self._content == "down":
            #     self.y = self.y - 1
            # if self._content == "left":
            #     self.x = self.x -1
            # if self._content == "right":
            #     self.x = self.x +1
            # if self._content == "leftup":
            #     self.x = self.x -1
            #     self.y = self.y +1
            # if self._content == "leftdown":
            #     self.y = self.y -1
            #     self.x = self.x -1
            # if self._content == "rightup":
            #     self.y = self.y +1
            #     self.x = self.x +1
            # if self._content == "rightdown":
            #     self.y = self.y -1
            #     self.x = self.x +1
            # ###########################################
    def characters(self,content):
        self._content = content

    def hitwall(self,x,y):#自定义的撞墙方法，用于标注行动轨迹超出30*30范围
        self.x = x
        self.y = y
        if x>30 or x<0 or y>30 or y< 0:
            print("hit wall")
            print("make the point red")

if __name__ == "__main__":
    handler = MoveHandler()
    sax.parse("eightDirctions.xml",handler)
    #sax.parse("testHitWall.xml", handler)