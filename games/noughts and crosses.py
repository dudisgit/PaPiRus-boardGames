#noughts and crosses game
from random import randint

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.board = [0,0,0,0,0,0,0,0,0]
        self.ind = 0
        self.quitBind = exitGame
        game.downBind[0] = self.slideSmall
        game.downBind[1] = self.slideBig
        game.downBind[2] = self.place
        game.downBind[3] = self.Quit
        game.downBind[4] = self.AINo
        game.clear()
        game.text(60,40,"Controlls")
        game.text(5,50,"1 - Switch column")
        game.text(5,60,"2 - Switch row")
        game.text(5,70,"3 - Place spot")
        game.text(5,80,"4 - Exit game")
        game.text(40,12,"Play againsed AI?")
        game.text(5,3,"Yes")
        game.text(175,3,"No")
        self.starting = True
        self.win = 0
        self.winPos = []
        self.AI = False
        self.turn = randint(0,1)
        game.update()
    def Quit(self): #Quit button was pressed
        if self.win!=0:
            self.win = 0
            self.board = [0,0,0,0,0,0,0,0,0]
            self.render()
        else:
            self.quitBind()
    def AINo(self): #Button to not play againsed AI was clicked
        if self.starting:
            self.AI = False
            self.starting = False
            self.render()
    def detectWin(self,p,brd): #Detects if there is a win on the board
        win = brd[0]==p and brd[1]==p and brd[2]==p
        winPos = [0,1,2]
        if not win:
            win = brd[3]==p and brd[4]==p and brd[5]==p
            winPos = [3,4,5]
        if not win:
            win = brd[6]==p and brd[7]==p and brd[8]==p
            winPos = [6,7,8]
        if not win:
            win = brd[0]==p and brd[3]==p and brd[6]==p
            winPos = [0,3,6]
        if not win:
            win = brd[1]==p and brd[4]==p and brd[7]==p
            winPos = [1,4,7]
        if not win:
            win = brd[2]==p and brd[5]==p and brd[8]==p
            winPos = [2,5,8]
        if not win:
            win = brd[0]==p and brd[4]==p and brd[8]==p
            winPos = [0,4,8]
        if not win:
            win = brd[2]==p and brd[4]==p and brd[6]==p
            winPos = [2,4,6]
        return win,winPos
    def minimax(self,brd,trn): #An algorithm for finding the best move
        #brd is a board
        #trn is the turn its working on
        ls = 0
        for i in range(0,9):
            if brd[i]==0:
                brd[i] = trn
                isWin,ps = self.detectWin(trn,brd)
                if isWin:
                    ls+=trn
                else:
                    ls-=self.minimax(brd,trn*-1)
                brd[i] = 0
        return ls
    def AITurn(self): #Figure out what the current move should be
        ls = [0,0]
        if self.turn==1:
            ls[0]=99999999 #Makes sure the AI has to go (else it might skip)
        for i in range(0,9):
            if self.board[i]==0:
                self.board[i] = (2*self.turn)-1
                val = self.minimax(self.board,1-(2*self.turn))
                if self.turn==1:
                    if val<ls[0]:
                        ls = [val+0,i+0]
                else:
                    if val>ls[0]:
                        ls = [val+0,i+0]
                self.board[i] = 0
        self.board[ls[1]] = (2*self.turn)-1
    def place(self): #Middle button was clicked
        if not self.starting and self.win==0:
            self.board[self.ind] = (2*self.turn)-1
            self.turn = int(self.turn==0)
            win1,wpos1 = self.detectWin(-1,self.board)
            win2,wpos2 = self.detectWin(1,self.board)
            if win1 or win2:
                if win1:
                    self.win = -1
                    self.winPos = wpos1
                else:
                    self.win = 1
                    self.winPos = wpos2
            else:
                if self.AI:
                    self.AITurn()
                    self.turn = int(self.turn==0)
                    win1,wpos1 = self.detectWin(-1,self.board)
                    win2,wpos2 = self.detectWin(1,self.board)
                    if win1 or win2:
                        if win1:
                            self.win = -1
                            self.winPos = wpos1
                        else:
                            self.win = 1
                            self.winPos = wpos2
                        self.render()
                        return 0
                loopAround = self.ind+0
                while self.board[self.ind]!=0:
                    self.ind+=1
                    if self.ind>=9:
                        self.ind = 0
                    if self.ind==loopAround:
                        break
                if self.ind==loopAround: #Draw
                    self.win = 2
            self.render()
    def drawWin(self): #Draws the winning screen
        if self.win!=2:
            st = self.getItemPos(self.winPos[0])
            en = self.getItemPos(self.winPos[2])
            self.scr.line((st[0]+st[2])/2,(st[1]+st[3])/2,(en[0]+en[2])/2,(en[1]+en[3])/2)
        if self.win==-1:
            self.scr.line(150,10,190,40)
            self.scr.line(190,10,150,40)
        elif self.win==1:
            self.scr.circle(170,25,20,False)
        else:
            self.scr.text(150,30,"NOBODY")
        self.scr.text(160,40,"WINS")
        self.scr.text(0,0,"Press 4")
        self.scr.text(20,10,"to")
        self.scr.text(0,20,"restart")
    def getItemPos(self,ind): #Returns the position of a cell
        ps = [0,0,0,0]
        if ind==0:
            ps = [52,0,81,29]
        elif ind==1:
            ps = [81,0,119,29]
        elif ind==2:
            ps = [119,0,148,29]
        elif ind==3:
            ps = [52,29,81,67]
        elif ind==4:
            ps = [81,29,119,67]
        elif ind==5:
            ps = [119,29,148,67]
        elif ind==6:
            ps = [52,67,81,96]
        elif ind==7:
            ps = [81,67,119,96]
        elif ind==8:
            ps = [119,67,148,96]
        return ps
    def drawItem(self,ind,typ): #Draw an object in cell index <ind>
        ps = self.getItemPos(ind)
        if typ=="sel":
            self.scr.rectangle(ps[0]+4,ps[1]+4,ps[2]-4,ps[3]-4,False)
        elif typ=="x":
            self.scr.line(ps[0]+4,ps[1]+4,ps[2]-4,ps[3]-4)
            self.scr.line(ps[2]-4,ps[1]+4,ps[0]+4,ps[3]-4)
        elif typ=="o":
            self.scr.circle((ps[0]+ps[2])/2,(ps[1]+ps[3])/2,20,False)
    def render(self): #Draw the game screen
        self.scr.clear()
        self.scr.line(52,29,148,29)
        self.scr.line(52,67,148,67)
        self.scr.line(81,0,81,96)
        self.scr.line(119,0,119,96)
        for i in range(0,9):
            if self.board[i]!=0:
                if self.board[i]==-1:
                    self.drawItem(i,"x")
                else:
                    self.drawItem(i,"o")
        if self.win!=0:
            self.drawWin()
        else:
            self.drawItem(self.ind,"sel")
            if self.turn==0:
                self.scr.line(10,10,40,40)
                self.scr.line(40,10,10,40)
            else:
                self.scr.circle(25,25,20,False)
            self.scr.text(10,40,"TURN")
        self.scr.update()
    def slideBig(self):
        if self.starting or self.win!=0:
            return 0
        self.ind+=3
        if self.ind>=9:
            self.ind-=9
        while self.board[self.ind]!=0:
            self.ind+=1
            if self.ind>=9:
                self.ind = 0
        self.render()
    def slideSmall(self):
        if self.starting or self.win!=0:
            self.AI = True
            self.starting = False
            self.render()
            return 0
        self.ind+=1
        if self.ind>=9:
            self.ind = 0
        while self.board[self.ind]!=0:
            self.ind+=1
            if self.ind>=9:
                self.ind = 0
        self.render()
    def loop(self):
        pass
