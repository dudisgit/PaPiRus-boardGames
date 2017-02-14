#This is used for testing the games you make
#
#It uses a simple tkinter window and some buttons to emulate the actual PaPiRus screen

from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
import math

class Screen(): #The fake screen
    def __init__(self,parent):
        self.draw = Canvas(parent,width=400,height=192)
        self.imgDraw = Image.new("1", (200,96), "white")
        self.img = ImageDraw.Draw(self.imgDraw)
        self.drawAll()
    def setPixel(self,x,y,On):
        if x>=0 and x<200 and y>=0 and y<96:
            self.board[x,y]=On
    def drawAll(self): #Draws everything to the canvas
        self.draw.delete(ALL)
        phot = ImageTk.PhotoImage(self.imgDraw.resize((400,192)))
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
        screen.img.rectangle((px,py,tx,ty),1)
    else:
        screen.img.rectangle((px,py,tx,ty))
def circle(px,py,rad,fill): #Creates a circle
    #'px' and 'py' are the position of the circle
    #'rad' is the radius
    #'fill' is wether it is filled or not
    if fill:
        screen.img.ellipse((px-int(rad/2),py-int(rad/2),px+int(rad/2),py+int(rad/2)),1)
    else:
        screen.img.ellipse((px-int(rad/2),py-int(rad/2),px+int(rad/2),py+int(rad/2)))
def line(px,py,tx,ty):
    #'px' and 'py' are the start of the rectangle
    #'tx' and 'ty' are the end of the rectangle
    screen.img.line((px,py,tx,ty))
def text(px,py,text):
    screen.img.text( (px,py), text, font=font, fill="black")




main = Tk()
main.title("Screen tester")
screen = Screen(main)
screen.draw.pack()

#Testing
line(10,10,80,120)
circle(60,30, 12, True)
rectangle(160,30,180,40,True)
text(10,10, "Testing")
update()
main.mainloop()
