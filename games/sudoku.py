#Idk the name of this game
from random import randint

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.exitGame = exitGame
        game.downBind[0] = self.nextIn
        game.downBind[1] = self.nextOut
        self.ind = 0
        self.board = []
        for y in range(9):
            self.board.append([])
            for x in range(9):
                self.board[y].append(randint(1,16))
        self.render()
    def nextIn(self):
        self.ind+=1
        if self.ind%3==0:
            if (int(self.ind/9)+1)%3==0 and int(self.ind/9)!=0:
                self.ind-=21
            else:
                self.ind+=6
        print(int(self.ind/9),(int(self.ind/9))%3)
        self.render()
    def nextOut(self):
        self.ind+=3
        self.render()
    def render(self): #Draws the game
        self.scr.clear()
        self.scr.rectangle(40,1,160,95,False)
        for i in range(1,9):
            self.scr.line(40+int(i*13.2),0,40+int(i*13.2),95)
            if i%3==0:
                self.scr.line(39+int(i*13.2),0,39+int(i*13.2),95)
        for i in range(1,9):
            self.scr.line(40,1+int(i*10.5),160,1+int(i*10.5))
            if i%3==0:
                self.scr.line(40,int(i*10.5),160,int(i*10.5))
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                if b<10:
                    self.scr.text(45+int(x*13.2),1+int(y*10.5),str(b))
            self.scr.rectangle(41+int((self.ind%9)*13.2),2+int(int(self.ind/9)*10.5),
                               53+int((self.ind%9)*13.2),10+int(int(self.ind/9)*10.5),
                               False)
        self.scr.update()
    def loop(self):
        pass
