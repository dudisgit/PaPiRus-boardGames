#A snake game
from random import randint
import time

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.exitGame = exitGame
        self.tail = [[10,4]]
        self.dir = 1 #Direction
        self.startup = True
        self.dific = 0 #Dificulty
        self.apple = [randint(0,19),randint(0,7)]
        self.score = 0
        self.dead = False
        self.updateTime = time.time()+0.1
        game.downBind[0] = self.but1
        game.downBind[1] = self.but2
        game.downBind[2] = self.but3
        game.downBind[3] = self.but4
        game.downBind[4] = self.but5        
        game.clear()
        game.text(0,0,"1")
        game.text(45,0,"2")
        game.text(90,0,"3")
        game.text(135,0,"4")
        game.text(180,0,"5")
        game.text(35,10,"Select a dificulty")
        game.text(60,32,"Controlls")
        game.text(0,42,"1 - Left")
        game.text(0,52,"2 - Up")
        game.text(0,62,"3 - Exit/reset game")
        game.text(0,72,"4 - Down")
        game.text(0,82,"5 - Right")
        game.update()
    def but1(self): #Button 1
        if self.startup:
            self.dific = 1
            self.startup = False
        else:
            self.dir=3
    def but2(self): #Button 2
        if self.startup:
            self.dific = 2
            self.startup = False
        else:
            self.dir=2
    def but3(self): #Button 3
        if self.startup:
            self.dific = 3
            self.startup = False
        else:
            if self.dead:
                self.tail = [[10,4]]
                self.score = 0
                self.dead = False
                self.dir = 1
                self.apple = [randint(0,19),randint(0,7)]
            else:
                self.exitGame()
    def but4(self): #Button 4
        if self.startup:
            self.dific = 4
            self.startup = False
        else:
            self.dir=0
    def but5(self): #Button 5
        if self.startup:
            self.dific = 5
            self.startup = False
        else:
            self.dir=1
    def render(self): #Draw the snake game
        self.scr.clear()
        self.scr.rectangle(1,15,199,95,False)
        self.scr.text(1,2,"Score: "+str(self.score))
        for a in self.tail:
            self.scr.rectangle(a[0]*10,(a[1]*10)+15,(a[0]*10)+10,(a[1]*10)+25,True)
        self.scr.rectangle(self.apple[0]*10,(self.apple[1]*10)+15,(self.apple[0]*10)+5,(self.apple[1]*10)+20,True)
        self.scr.rectangle((self.apple[0]*10)+5,(self.apple[1]*10)+20,(self.apple[0]*10)+10,(self.apple[1]*10)+25,True)
        if self.dead:
            self.scr.text(100,2,"GAME OVER")
        self.scr.update()
    def loop(self):
        if time.time()>self.updateTime and not self.startup and not self.dead:
            for i in range(1,len(self.tail)):
                self.tail[len(self.tail)-i] = [self.tail[len(self.tail)-i-1][0]+0,self.tail[len(self.tail)-i-1][1]+0]
            if not self.dead:
                if self.dir==0:
                    self.tail[0][1]+=1
                elif self.dir==1:
                    self.tail[0][0]+=1
                elif self.dir==2:
                    self.tail[0][1]-=1
                elif self.dir==3:
                    self.tail[0][0]-=1
            if self.tail[0][0]<0:
                self.tail[0][0]=19
            if self.tail[0][0]>19:
                self.tail[0][0]=0
            if self.tail[0][1]<0:
                self.tail[0][1]=7
            if self.tail[0][1]>7:
                self.tail[0][1]=0
            if self.tail[0] in self.tail[1:]:
                self.dead = True
            
            if self.tail[0]==self.apple:
                self.apple = [randint(0,19),randint(0,7)]
                self.tail.append([self.tail[-1][0]+0,self.tail[-1][1]+0])
                while self.apple in self.tail:
                    self.apple = [randint(0,19),randint(0,7)]
                self.score+=1
            self.render()
            self.updateTime = time.time()+(1/self.dific)
