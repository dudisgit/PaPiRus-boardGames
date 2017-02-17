#This is the script to run on the pi to display the content
#
#Most of the code is copied from the screenTester.py file

from PIL import Image, ImageFont, ImageDraw, ImageOps
import math
from papirus import Papirus
import RPi.GPIO as GPIO

def nil():
    pass

downBind = [nil,nil,nil,nil,nil]
upBind =   [nil,nil,nil,nil,nil]

#Screen items
class Screen(): #The fake screen
    def __init__(self):
        self.draw = Papirus()
        self.imgDraw = Image.new("1", (200,96), "white")
        self.img = ImageDraw.Draw(self.imgDraw)
        self.drawAll()
    def drawAll(self): #Draws everything to the canvas
        self.draw.display(self.imgDraw)
        self.draw.partial_update()

font = ImageFont.truetype("windows_command_prompt.ttf",16)

#Functions used when programming a game
def button(index):
    global buttons
    return not GPIO.input(buttons[index])
def update(): #Updates the screen
    screen.drawAll()
def updateFull(): #Fully updates the screen
    screen.draw.update()
def clear(): #Clears the screen
    screen.img.rectangle((0,0,200,96),"white")
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
def image(px,py,imgPath):
    img = Image.open(imgPath)
    #img=ImageOps.invert(img)
    img = Image.eval(img, lambda x: 255-x)
    img=img.convert("1")
    screen.img.bitmap((px,py),img)

screen = Screen()
buttonChange = [False,False,False,False,False]

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)
GPIO.setup(26,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(21,GPIO.IN)
buttons = {}
buttons[0]=26
buttons[1]=19
buttons[2]=20
buttons[3]=16
buttons[4]=21


def updateLoop(): #This should be called ALLWAYS
    active = [not GPIO.input(26),not GPIO.input(19),not GPIO.input(20),not GPIO.input(16),not GPIO.input(21)]
    if buttonChange!=active:
        if buttonChange[0]!=active[0]:
            if active[0]:
                downBind[0]()
            else:
                upBind[0]()
            buttonChange[0] = active[0] == True
        if buttonChange[1]!=active[1]:
            if active[1]:
                downBind[1]()
            else:
                upBind[1]()
            buttonChange[1] = active[1] == True
        if buttonChange[2]!=active[2]:
            if active[2]:
                downBind[2]()
            else:
                upBind[2]()
            buttonChange[2] = active[2] == True
        if buttonChange[3]!=active[3]:
            if active[3]:
                downBind[3]()
            else:
                upBind[3]()
            buttonChange[3] = active[3] == True
        if buttonChange[4]!=active[4]:
            if active[4]:
                downBind[4]()
            else:
                upBind[4]()
            buttonChange[4] = active[4] == True
