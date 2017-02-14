#This is used for testing the games you make
#
#It uses a simple tkinter window and some buttons to emulate the actual PaPiRus screen

from tkinter import *
from PIL import Image, ImageTk

class Screen(): #The fake screen
    def __init__(self,parent):
        self.draw = Canvas(parent,width=400,height=192)
        self.img = Image.new("1", (200,96), "white")
        self.board = self.img.load()
        self.drawAll()
    def drawAll(self): #Draws everything to the canvas
        self.draw.delete(ALL)
        phot = ImageTk.PhotoImage(self.img.resize((400,192)))
        self.draw.img = phot
        self.draw.create_image(200,96,image=phot)

def update(): #Updates the screen
    screen.drawAll()
def rectangle(px,py,tx,ty,fill): #Creates a rectangle
    #'px' and 'py' are the start of the rectangle
    #'tx' and 'ty' are the end of the rectangle
    #'fill' is wether it is filled or now
    if fill:
        pass
    else:
        for x in range(px,tx):
            screen.board[x,py]=1
            screen.board[x,ty]=1
        for y in range(py,ty):
            screen.board[px,y]=1
            screen.board[tx,y]=1



main = Tk()
main.title("Screen tester")
screen = Screen(main)
screen.draw.pack()

#Testing
rectangle(10,10,20,20,False)
update()

main.mainloop()
