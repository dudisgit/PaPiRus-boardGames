from random import randint
import math as m
import time

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        game.downBind[2] = self.roll
        game.downBind[0] = exitGame
        self.win = True
        
        self.scroll = 150
        self.board = []
        self.generateBoard()
        self.players = [0,0,0,0] #Player list, index 0 is the player, the rest are bots
        self.turn = 0
        
        game.text(60,2,"Controlls")
        game.text(2,14,"0 - Quit game")
        game.text(2,26,"3 - Roll dice and move")
        game.text(2,42,"Press 3 to start game")
        game.update()
    def roll(self): #Button clicked to roll the dice
        if self.win:
            self.win = False
            self.generateBoard()
            self.players = [0,0,0,0]
            self.turn = 0
            self.scroll = 150
            self.render()
            self.scr.updateFull()
            return 0
        for i,a in enumerate(self.players):
            self.turn = i
            rl = randint(1,6)
            self.players[i]+=rl
            if self.players[i]>99:
                self.players[i]+=99-self.players[i]
            if self.players[i]==99:
                self.win = True
                self.scroll = -15
                break
            if i==0:
                self.scroll = 200-((int(self.players[0]/10)*20)+50)
            self.render()
            if self.board[self.players[i]]!=-1:
                time.sleep(0.3)
                self.players[i] = self.board[self.players[i]]+0
                if i==0:
                    self.scroll = 200-((int(self.players[0]/10)*20)+50)
                self.render()
            time.sleep(0.3)
        if not self.win:
            self.turn = 0
        self.render()
    def generateBoard(self):
        self.board = []
        for i in range(100):
            if randint(0,8)==1:
                r = randint(1,98)
                while (r+1)%10==(i+1)%10:
                    r = randint(1,98)
                self.board.append(r+0)
            else:
                self.board.append(-1)
    def drawLadder(self,sx,sy,ex,ey): #Draws a ladder from (sx,sy) to (ex,ey)
        s = 5 #Size
        ang = m.atan2(sx-ex,sy-ey)
        r = m.pi/2 #90 Degreese
        self.scr.line(sx+(m.sin(ang+r)*s),sy+(m.cos(ang+r)*s),ex+(m.sin(ang+r)*s),ey+(m.cos(ang+r)*s))
        self.scr.line(sx+(m.sin(ang-r)*s),sy+(m.cos(ang-r)*s),ex+(m.sin(ang-r)*s),ey+(m.cos(ang-r)*s))
        dist = m.sqrt(((sx-ex)**2)+((sy-ey)**2))
        for i in range(1,int(round(dist/10))):
            x,y=sx+(m.cos(0-r-ang)*(i*10)),sy+(m.sin(0-r-ang)*(i*10))
            self.scr.line(x+(m.sin(ang+r)*s),y+(m.cos(ang+r)*s),x+(m.sin(ang-r)*s),y+(m.cos(ang-r)*s))
    def drawSnake(self,sx,sy,ex,ey): #Draws a snake from (sx,sy) to (ex,ey)
        s = 5 #Size
        ang = m.atan2(sx-ex,sy-ey)
        r = m.pi/2 #90 Degreese
        dist = m.sqrt(((sx-ex)**2)+((sy-ey)**2))
        last = [sx+0,sy+0,0]
        for i in range(1,int(round(dist/10))+1):
            x,y=sx+(m.cos(0-r-ang)*(i*10)),sy+(m.sin(0-r-ang)*(i*10))
            if last[2]==1:
                self.scr.line(x+(m.sin(ang+r)*s),y+(m.cos(ang+r)*s),last[0],last[1])
                last = [x+(m.sin(ang+r)*s),y+(m.cos(ang+r)*s),0]
            else:
                self.scr.line(x+(m.sin(ang-r)*s),y+(m.cos(ang-r)*s),last[0],last[1])
                last = [x+(m.sin(ang-r)*s),y+(m.cos(ang-r)*s),1]
        self.scr.circle(last[0],last[1],5,True)
    def render(self):
        self.scr.clear()
        if self.win:
            if self.turn==0:
                self.scr.text(2,2,"You win!")
            else:
                self.scr.text(2,2,"Player "+str(self.turn+1)+" wins!")
            self.scr.text(2,14,"Press 3 to restart")
        for i,a in enumerate(self.board):
            mult = ((int(i/10)%2)*2)-1
            add = 200*int(int(i/10)%2==0)
            self.scr.rectangle(((i%10)*20*mult)+add,200-(int(i/10)*20)-self.scroll,((((i%10)*20)+20)*mult)+add,200-(int(i/10)*20)+20-self.scroll,False)
            if a!=-1:
                if a>i:
                    self.drawLadder(((((i%10)*20)+10)*mult)+add,200-(int(i/10)*20)-self.scroll+10,((((a%10)*20)+10)*mult)+add,200-(int(a/10)*20)-self.scroll+10)
                else:
                    self.drawSnake(((((a%10)*20)+10)*mult)+add,200-(int(a/10)*20)-self.scroll+10,((((i%10)*20)+10)*mult)+add,200-(int(i/10)*20)-self.scroll+10)
        if self.turn!=0 and not self.win:
            self.scr.rectangle(0,0,self.turn*66,10,True)
        company = {} #Check if more than one player is on a squere
        for i,a in enumerate(self.players):
            mult = ((int(a/10)%2)*2)-1
            add = 200*int(int(a/10)%2==0)
            if a in company:
                company[a]+=1
            else:
                company[a]=0
            if company[a]==0:
                self.scr.circle(((((a%10)*20)+5)*mult)+add,200-(int(a/10)*20)-self.scroll+5,10,i!=0)
            elif company[a]==1:
                self.scr.circle(((((a%10)*20)+15)*mult)+add,200-(int(a/10)*20)-self.scroll+5,10,i!=0)
            elif company[a]==2:
                self.scr.circle(((((a%10)*20)+5)*mult)+add,200-(int(a/10)*20)-self.scroll+15,10,i!=0)
            elif company[a]==3:
                self.scr.circle(((((a%10)*20)+15)*mult)+add,200-(int(a/10)*20)-self.scroll+15,10,i!=0)
        self.scr.update()
    def loop(self):
        pass
