#!/usr/bin/env python
#coding=utf-8

from Tkinter import *

def beenClick():
	print "Click!!!"

def buttonClick():
	print "botton click!!!"

root=Tk()


text = Label(root, text="哈哈哈!!!",width="50",height="15")
butt = Button(root, text="click me",command=buttonClick)
text.pack()
butt.pack()

rad = Radiobutton(root,text="click",command=beenClick).pack()

root.mainloop()



