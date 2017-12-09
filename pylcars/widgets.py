# -*- coding: utf-8 -*-
from PyQt4 import  QtCore
from orientation import Orientation 

class Widgets():
    halfdot=('<svg height="{h}" width="{w}">'
            '<circle cx="{r}" cy="{r}" r="{r}" fill="{c}" />'
            '<rect height="{rh}" width="{rw}" x="{rx}" y="{ry}" fill="{c}" />'
            '</svg>')

    def halfDot(self,rect,text,color,orientation):
        print str(rect)
        print rect.height
        rh=h=rect.height()
        rw=w=rect.width()
        rx=ry=0
        r=h/2
        if orientation==Orientation.left:
          rx=r  
        elif orientation==Orientation.right:
          rw=r  
        elif orientation==Orientation.top:
          rh=r  
        elif orientation==Orientation.bottom:
          ry=r  
            
        svg=self.halfdot.format(h=h,w=w,
                           r=r,
                           rh=rh,rw=rw,rx=rx,ry=ry,
                           c=color)        
        print svg
        button = self.gui.createButton(svg,QtCore.QSize(w,h),text)
        button.setGeometry(rect)
        return button


    def __init__(self, gui):
        self.gui=gui
