#Testing game
import time

class Main():
    def __init__(self,game,stopGame):
        #game is a pointer to the library controlling the screen
        #stopGame is a function that stops playing the current game
        self.scr = game
        self.bars = [0,0,0,0] #List to store a basic bar animation
        self.drawScreen()
        #Bind all the buttons to call different functions when pressed
        game.downBind[0] = self.up1
        game.downBind[1] = self.up2
        game.downBind[3] = self.up3
        game.downBind[4] = self.up4
        game.downBind[2] = stopGame #Stops the game when pressed
        self.updateTime = time.time()+0.1 #To count when the screen needs updating
        #0.1 so it is 10 FPS
    def up1(self): #Make a bar move corresponding to the button 0
        self.bars[0] = 1
    def up2(self): #Make a bar move corresponding to the button 1
        self.bars[1] = 1
    def up3(self): #Make a bar move corresponding to the button 3
        self.bars[2] = 1
    def up4(self): #Make a bar move corresponding to the button 4
        self.bars[3] = 1
    def drawScreen(self): #Clears and draws everything on the screen
        self.scr.clear() #Clear the screen
        self.scr.text(0,0,"This is a test game")
        self.scr.text(0,10,"Press middle button to exit")
        #Draw the rectangles
        self.scr.rectangle(0,96-(self.bars[0]*70),50,96,True)
        self.scr.rectangle(50,96-(self.bars[1]*70),100,96,True)
        self.scr.rectangle(100,96-(self.bars[2]*70),150,96,True)
        self.scr.rectangle(150,96-(self.bars[3]*70),200,96,True)
        self.scr.update() #Show the changes done
    def loop(self): #Repeatedly called by the script that called this one
        if time.time()>self.updateTime: #Is it time to update the screen?
            self.updateTime = time.time()+0.1
            for i in range(0,4): #Decrease all the bars by a small amount
                self.bars[i]*=0.9
            self.drawScreen()
