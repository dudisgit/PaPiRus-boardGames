#Testing game
import time

class Main():
    def __init__(self,game,stopGame):
        #game is a pointer to the library controlling the screen
        #stopGame is a function that stops playing the current game
        self.scr = game
        self.bars = [0,0,0,0]
        self.drawScreen()
        game.downBind[0] = self.up1
        game.downBind[1] = self.up2
        game.downBind[3] = self.up3
        game.downBind[4] = self.up4
        game.downBind[2] = stopGame
        self.updateTime = time.time()+0.1
    def up1(self):
        self.bars[0] = 1
    def up2(self):
        self.bars[1] = 1
    def up3(self):
        self.bars[2] = 1
    def up4(self):
        self.bars[3] = 1
    def drawScreen(self):
        self.scr.clear()
        self.scr.text(0,0,"This is a test game")
        self.scr.text(0,10,"Press middle button to exit")
        self.scr.rectangle(0,96-(self.bars[0]*70),50,96,True)
        self.scr.rectangle(50,96-(self.bars[1]*70),100,96,True)
        self.scr.rectangle(100,96-(self.bars[2]*70),150,96,True)
        self.scr.rectangle(150,96-(self.bars[3]*70),200,96,True)
        self.scr.update()
    def loop(self): #Repeatedly called by the script that called this one
        if time.time()>self.updateTime:
            self.updateTime = time.time()+0.1
            for i in range(0,4):
                self.bars[i]*=0.9
            self.drawScreen()
