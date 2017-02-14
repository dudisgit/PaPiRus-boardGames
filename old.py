#This is used for testing the games you make
#
#It uses a simple tkinter window and some buttons to emulate the actual PaPiRus screen

from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
import math

class Screen(): #The fake screen
    def __init__(self,parent):
        self.draw = Canvas(parent,width=400,height=192)
        self.img = Image.new("1", (200,96), "white")
        self.board = self.img.load()
        self.imgDraw = ImageDraw.Draw(self.img)
        self.drawAll()
    def setPixel(self,x,y,On):
        if x>=0 and x<200 and y>=0 and y<96:
            self.board[x,y]=On
    def drawAll(self): #Draws everything to the canvas
        self.draw.delete(ALL)
        phot = ImageTk.PhotoImage(self.img.resize((400,192)))
        self.draw.img = phot
        self.draw.create_image(200,96,image=phot)

font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf",12)

def update(): #Updates the screen
    screen.drawAll()

def rectangle(px,py,tx,ty,fill): #Creates a rectangle
    #'px' and 'py' are the start of the rectangle
    #'tx' and 'ty' are the end of the rectangle
    #'fill' is wether it is filled or not
    if fill:
        for x in range(px,tx):
            for y in range(py,ty):
                screen.setPixel(x,y,1)
    else:
        for x in range(px,tx):
            screen.setPixel(x,py,1)
            screen.setPixel(x,ty,1)
        for y in range(py,ty):
            screen.setPixel(px,y,1)
            screen.setPixel(tx,y,1)
        screen.setPixel(tx,ty,1)
def circle(px,py,rad,fill): #Creates a circle
    #'px' and 'py' are the position of the circle
    #'rad' is the radius
    #'fill' is wether it is filled or not
    #Used the 'Midpoint circle algorithm'
    if fill:
        for r in range(0,rad):
            x,y = r,0
            err = 0
            while x>=y:
                screen.setPixel(px+x,py+y,1)
                screen.setPixel(px+y,py+x,1)
                screen.setPixel(px-y,py+x,1)
                screen.setPixel(px-x,py+y,1)
                screen.setPixel(px-x,py-y,1)
                screen.setPixel(px-y,py-x,1)
                screen.setPixel(px+y,py-x,1)
                screen.setPixel(px+x,py-y,1)
                if err<=0:
                    y+=1
                    err+=2*y+1
                if err>0:
                    x-=1
                    err-=2*x+1
    else:
        x,y = rad,0
        err = 0
        while x>=y:
            screen.setPixel(px+x,py+y,1)
            screen.setPixel(px+y,py+x,1)
            screen.setPixel(px-y,py+x,1)
            screen.setPixel(px-x,py+y,1)
            screen.setPixel(px-x,py-y,1)
            screen.setPixel(px-y,py-x,1)
            screen.setPixel(px+y,py-x,1)
            screen.setPixel(px+x,py-y,1)
            if err<=0:
                y+=1
                err+=2*y+1
            if err>0:
                x-=1
                err-=2*x+1
def line(px,py,tx,ty):
    #'px' and 'py' are the start of the rectangle
    #'tx' and 'ty' are the end of the rectangle
    #Bresenham's line algorithm
    difx = tx-px
    dify = ty-py
    if abs(difx)>abs(dify):
        step = abs(difx)
    else:
        step = abs(dify)
    if step==0:
        return 0
    xinc = difx/step
    yinc = dify/step
    x = px+0
    y = py+0
    for i in range(0,step):
        x+=xinc
        y+=yinc
        screen.setPixel(x,y,1)
def text(px,py,text):
    screen.imgDraw.text( (px,py), text, font=font, fill="black")
    screen.imgDraw.textsize




main = Tk()
main.title("Screen tester")
screen = Screen(main)
screen.draw.pack()

#Testing

update()
text(0,0,"test")
main.mainloop()
