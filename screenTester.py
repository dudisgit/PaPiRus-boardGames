#This is used for testing the games you make
#
#It uses a simple tkinter window and some buttons to emulate the actual PaPiRus screen
#You can click the buttons or use numbers 1-5 on keyboard to press them
#You can use the button() function to get if a button it down or not, or you can use the two lists downBind and upBind to call functions


from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
import math

def nil():
    pass

downBind = [nil,nil,nil,nil,nil]
upBind =   [nil,nil,nil,nil,nil]

#Screen items
class Screen(): #The fake screen
    def __init__(self,parent):
        self.draw = Canvas(parent,width=400,height=192)
        self.imgDraw = Image.new("1", (200,96), "white")
        self.img = ImageDraw.Draw(self.imgDraw)
        self.drawAll()
    def drawAll(self): #Draws everything to the canvas
        self.draw.delete(ALL)
        phot = ImageTk.PhotoImage(self.imgDraw.resize((400,192)))
        self.draw.img = phot
        self.draw.create_image(200,96,image=phot)
class Buttons():
    def __init__(self,parent):
        self.draw = Canvas(parent,width=400,height=55,bg="#e9e9e9")
        self.draw.bind("<Button-1>",self.buttonPress)
        self.draw.bind("<ButtonRelease-1>",self.buttonRelease)
        self.on = PhotoImage(file="onButton.png")
        self.off = PhotoImage(file="offButton.png")
        self.draw.img1 = self.on
        self.draw.img2 = self.off
        self.active = [False,False,False,False,False]
        self.drawAll()
    def buttonRelease(self,ev):
        self.active = [False,False,False,False,False]
        self.drawAll()
    def buttonPress(self,ev):
        ind = round((ev.x-40)/80)
        if ind<0 or ind>4:
            return 0
        self.active[ind]=True
        self.drawAll()
    def drawAll(self): #Draws all the buttons on from scratch
        self.draw.delete(ALL)
        for i in range(0,5):
            if self.active[i]:
                self.draw.create_image((i*80)+40,30,image=self.on)
            else:
                self.draw.create_image((i*80)+40,30,image=self.off)
    def keyDown(self,ev):
        c = ev.char
        if c=="1":
            self.active[0] = True
        elif c=="2":
            self.active[1] = True
        elif c=="3":
            self.active[2] = True
        elif c=="4":
            self.active[3] = True
        elif c=="5":
            self.active[4] = True
        self.drawAll()
    def keyUp(self,ev):
        c = ev.char
        if c=="1":
            self.active[0] = False
        elif c=="2":
            self.active[1] = False
        elif c=="3":
            self.active[2] = False
        elif c=="4":
            self.active[3] = False
        elif c=="5":
            self.active[4] = False
        self.drawAll()

font = ImageFont.truetype("windows_command_prompt.ttf",16)

#Functions used when programming a game
def button(index):
    main.update()
    return buttonObj.active[index]
def update(): #Updates the screen
    screen.drawAll()
    main.update()
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
    img=img.convert("1")
    screen.img.bitmap((px,py),img)

main = Tk()
main.title("Screen tester")
screen = Screen(main)
screen.draw.pack()
buttonObj = Buttons(main)
buttonObj.draw.pack()
buttonChange = [False,False,False,False,False]

main.bind("<Key>",buttonObj.keyDown)
main.bind("<KeyRelease>",buttonObj.keyUp)
main.update()


def updateLoop(): #This should be called ALLWAYS
    if buttonChange!=buttonObj.active:
        if buttonChange[0]!=buttonObj.active[0]:
            if buttonObj.active[0]:
                downBind[0]()
            else:
                upBind[0]()
            buttonChange[0] = buttonObj.active[0] == True
        if buttonChange[1]!=buttonObj.active[1]:
            if buttonObj.active[1]:
                downBind[1]()
            else:
                upBind[1]()
            buttonChange[1] = buttonObj.active[1] == True
        if buttonChange[2]!=buttonObj.active[2]:
            if buttonObj.active[2]:
                downBind[2]()
            else:
                upBind[2]()
            buttonChange[2] = buttonObj.active[2] == True
        if buttonChange[3]!=buttonObj.active[3]:
            if buttonObj.active[3]:
                downBind[3]()
            else:
                upBind[3]()
            buttonChange[3] = buttonObj.active[3] == True
        if buttonChange[4]!=buttonObj.active[4]:
            if buttonObj.active[4]:
                downBind[4]()
            else:
                upBind[4]()
            buttonChange[4] = buttonObj.active[4] == True
    main.update()
