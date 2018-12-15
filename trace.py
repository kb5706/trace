#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml import sax

class MoveHandler(sax.ContentHandler):
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
        if name == "step":
            print("step is "+self._content)

    def characters(self,content):
        self._content = content

if __name__ == "__main__":
    handler = MoveHandler()
    sax.parse("eightDirctions.xml",handler)