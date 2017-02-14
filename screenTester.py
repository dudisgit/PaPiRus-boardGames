#This is used for testing the games you make
#
#It uses a simple tkinter window and some buttons to emulate the actual PaPiRus screen

from tkinter import *
import time

class Screen(): #The fake screen
    def __init__(self,parent):
        self.draw = Canvas(parent,width=400,height=192)
        self.board = [] #The matrix of pixels on the board
        self.boardObj = [] #Used to store the canvas id's of the pixels used
        self.boardChange = [] #For tracking changes in the screen (for faster rendering)
        for x in range(0,200):
            self.board.append([])
            self.boardChange.append([])
            for y in range(0,96):
                self.board[x].append(False)
                self.boardChange[x].append(False)
        self.drawAll()
    def drawAll(self): #Draws all the pixels from scratch
        self.draw.delete(ALL) #Delete everything from the screen
        self.boardObj = []
        for x,a in enumerate(self.board): #Loop through each pixel
            self.boardObj.append([])
            for y,b in enumerate(a):
                if b: #Pixel is on
                    self.boardObj[x].append(self.draw.create_rectangle(x*2,y*2,(x*2)+2,(y*2)+2,outline="",fill="black"))
                else:
                    self.boardObj[x].append(self.draw.create_rectangle(x*2,y*2,(x*2)+2,(y*2)+2,outline="",fill="light gray"))
    def updateAll(self): #Updates all the pixels on the screen
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                if b: #Pixel is on
                    self.draw.itemconfig(self.boardObj[x][y],fill="black")
                else:
                    self.draw.itemconfig(self.boardObj[x][y],fill="light gray")
    def update(self): #Update pixels that have changed
        for x,a in enumerate(self.board):
            if a!=self.boardChange[x]: #Has the column changed?
                for y,b in enumerate(a):
                    if b!=self.boardChange[x][y]:
                        self.boardChange[x][y] = b == True #Makes sure it doesen't turn into a pointer!
                        if b: #Pixel is on
                            self.boardObj[x].append(self.draw.create_rectangle(x*2,y*2,(x*2)+2,(y*2)+2,outline="",fill="black"))
                        else:
                            self.boardObj[x].append(self.draw.create_rectangle(x*2,y*2,(x*2)+2,(y*2)+2,outline="",fill="light gray"))




main = Tk()
main.title("Screen tester")



test = Screen(main)
test.draw.pack()

main.update()

for xr in range(0,200):
    for yr in range(0,96):
        test.board[xr][yr]=True
        test.drawAll()
        main.update()

main.mainloop()
