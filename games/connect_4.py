#Connect 4 game
import pickle #For saving a game

class Main():
    def __init__(self,game,exitGame):
        game.downBind[0] = self.left
        game.downBind[1] = self.saveGame
        game.downBind[4] = self.right
        game.downBind[2] = self.place
        game.downBind[3] = exitGame
        self.scr = game
        self.ind = 0 #Index inserting to
        self.turn = -1
        self.board = []
        self.win = False
        self.AI = False
        self.winPos = []
        for y in range(6):
            self.board.append([])
            for x in range(7):
                self.board[y].append(0)
        self.startup = True
        game.clear()
        game.text(0,0,"Yes")
        game.text(180,0,"No")
        game.text(80,0,"LOAD")
        game.text(40,10,"Play againsed AI?")
        game.text(60,32,"Controlls")
        game.text(0,42,"1 - Move left")
        game.text(0,52,"2 - Save game")
        game.text(0,62,"3 - Place point")
        game.text(0,72,"4 - Exit game")
        game.text(0,82,"5 - Move right")
        game.update()
    def left(self): #Left button was pressed
        if self.startup:
            self.AI = True
            self.startup = False
            self.render()
            self.scr.updateFull()
            return 0
        if self.win:
            return 0
        self.ind-=1
        if self.ind<0:
            self.ind=0
        self.render()
    def right(self): #Right button was pressed
        if self.startup:
            self.AI = False
            self.startup = False
            self.render()
            self.scr.updateFull()
            return 0
        if self.win:
            return 0
        self.ind+=1
        if self.ind>=7:
            self.ind=6
        self.render()
    def saveGame(self):
        if not self.win and not self.startup:
            file = open("connect_4.save","wb")
            file.write(pickle.dumps([self.board,self.turn,self.AI]))
            file.close()
            self.scr.text(0,50,"saved")
            self.scr.text(3,60,"game")
            self.scr.update()
    def detectWinner(self,brd,p): #Detects a player winning
        win = False
        ps = [[0,0],[0,0]]
        for a in range(7):
            for b in range(3):
                if brd[b][a]==p and brd[b+1][a]==p and brd[b+2][a]==p and brd[b+3][a]==p:
                    win = True
                    ps = [[a,b],[a,b+3]]
                    break
            if win:
                break
        if not win:
            for a in range(6):
                for b in range(4):
                    if brd[a][b]==p and brd[a][b+1]==p and brd[a][b+2]==p and brd[a][b+3]==p:
                        win = True
                        ps = [[b,a],[b+3,a]]
                        break
                if win:
                    break
        if not win:
            for a in range(4):
                for b in range(3):
                    if brd[b][a]==p and brd[b+1][a+1]==p and brd[b+2][a+2]==p and brd[b+3][a+3]==p:
                        win = True
                        ps = [[a,b],[a+3,b+3]]
                        break
                    if brd[b+3][a]==p and brd[b+2][a+1]==p and brd[b+1][a+2]==p and brd[b][a+3]==p:
                        win = True
                        ps = [[a,b+3],[a+3,b]]
                        break
                if win:
                    break
        return win,ps
    def minimax(self,brd,trn,depth): #Uses the same AI as the noughts and crosses but it has a search depth
        rs = 0
        for i in range(7):
            if brd[0][i]==0:
                #Find the bottom of the row
                ind = 0
                for y in range(6):
                    if brd[y][i]!=0:
                        ind = y-1
                        break
                else:
                    ind = 5
                brd[ind][i] #Pretend to put the peace there
                w,wp = self.detectWinner(brd,trn)
                if w: #Won?
                    rs+=trn*2
                elif depth>0: #Go in more depth
                    rs-=self.minimax(brd,trn*-1,depth-1)
                brd[ind][i] = 0
        return rs
    def AITurn(self): #Take the go as an AI
        ls = [0,[0,0],True]
        if self.turn==1:
            ls[0]=0 #Makes sure the ai doesen't get stuck
        self.scr.text(0,0,"Thinking...")
        self.scr.update()
        for i in range(7):
            if self.board[0][i]==0:
                #Find the bottom of the row
                ind = 0
                for y in range(6):
                    if self.board[y][i]!=0:
                        ind = y-1
                        break
                else:
                    ind = 5
                self.board[ind][i]=self.turn
                val = self.minimax(self.board,self.turn,3)
                if self.turn==1:
                    if val<ls[0] or ls[2]:
                        ls = [val+0,[ind+0,i+0],False]
                else:
                    if val>ls[0]:
                        ls = [val+0,[ind+0,i+0]]
                self.board[ind][i]=0
        self.board[ls[1][0]][ls[1][1]]=self.turn+0
    def place(self):
        if self.startup:
            self.startup = False
            file = open("connect_4.save","rb")
            gd = pickle.loads(file.read())
            file.close()
            self.board = gd[0]
            self.turn = gd[1]
            self.AI = gd[2]
            self.render()
            self.scr.updateFull()
            return 0
        if self.win:
            self.board = []
            for y in range(6):
                self.board.append([])
                for x in range(7):
                    self.board[y].append(0)
            self.ind = 0
            self.win = False
            self.render()
            return 0
        if self.board[0][self.ind]!=0:
            return 0
        for i in range(0,6):
            if self.board[i][self.ind]!=0:
                self.board[i-1][self.ind]=self.turn+0
                break
        else:
            self.board[5][self.ind] = self.turn+0
        w,wpos = self.detectWinner(self.board,self.turn)
        if w:
            self.win = True
            self.winPos = wpos
        else:
            self.turn*=-1
        if self.AI and not self.win:
            self.AITurn()
            w,wpos = self.detectWinner(self.board,self.turn)
            if w:
                self.win = True
                self.winPos = wpos
            else:
                self.turn*=-1
        self.render()
    def render(self): #Draw the grid and game
        self.scr.clear()
        self.scr.rectangle(40,15,160,95,False)
        for i in range(1,7):
            self.scr.line(40+(i*17),15,40+(i*17),95)
        for i in range(1,6):
            self.scr.line(40,15+(i*13),160,15+(i*13))
        for a,y in enumerate(self.board):
            for b,x in enumerate(y):
                if x!=0:
                    if x==1:
                        self.scr.circle(32+((b+1)*17),8+((a+1)*13),8,True)
                    elif x==-1:
                        self.scr.circle(32+((b+1)*17),8+((a+1)*13),8,False)
                        self.scr.text(29+((b+1)*17),(a+1)*13,"x")
        if self.turn==1 and not self.win:
            self.scr.circle(32+((self.ind+1)*17),8,8,True)
        elif self.turn==-1 and not self.win:
            self.scr.circle(32+((self.ind+1)*17),8,8,False)
            self.scr.text(29+((self.ind+1)*17),0,"x")
        if self.win:
            self.scr.line(32+((self.winPos[0][0]+1)*17),8+((self.winPos[0][1]+1)*13),32+((self.winPos[1][0]+1)*17),8+((self.winPos[1][1]+1)*13))
            if self.turn==1:
                self.scr.circle(180,20,18,True)
            else:
                self.scr.circle(180,20,18,False)
                self.scr.line(175,15,185,25)
                self.scr.line(185,15,175,25)
            self.scr.text(167,30,"WINS")
            self.scr.text(0,0,"Press 3 to restart")
        self.scr.update()
    def loop(self):
        pass
