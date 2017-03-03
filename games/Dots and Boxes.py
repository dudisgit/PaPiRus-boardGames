
class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.exitGame = exitGame
        game.downBind[0] = self.left
        game.downBind[1] = self.up
        game.downBind[2] = self.place
        game.downBind[3] = self.down
        game.downBind[4] = self.right
        self.board = []
        self.placing = False
        self.win = True
        self.working = [] #Used for recusion
        self.generateBoard()
        self.turn = 1
        self.score = [0,0]
        self.sel = [10,10]
        game.text(60,2,"Controlls")
        game.text(2,14,"1 - Pointer left")
        game.text(2,26,"2 - Pointer up")
        game.text(2,38,"3 - Place (x2 to quit)")
        game.text(2,50,"4 - Pointer down")
        game.text(2,62,"5 - Pointer right")
        game.text(2,80,"Press 3 to start")
        game.update()
    def fillBox(self,x,y,pl):
        self.working.append([x,y])
        c = self.board[x][y]
        if x>0 and y>0 and "u" in c and "l" in c:
            if not [x-1,y-1] in self.working and not "1" in self.board[x-1][y-1] and not "2" in self.board[x-1][y-1]:
                c2 = self.board[x-1][y-1]
                if "d" in c2 and not "r" in c2:
                    self.board[x-1][y-1]+="r"+str(pl)
                    self.score[pl-1]+=1
                elif "r" in c2 and not "d" in c2:
                    self.board[x-1][y-1]+="d"+str(pl)
                    self.score[pl-1]+=1
        if x>0 and y<29 and "d" in c and "l" in c:
            if not [x-1,y+1] in self.working and not "1" in self.board[x-1][y] and not "2" in self.board[x-1][y]:
                c2 = self.board[x-1][y+1]
                if "u" in c2 and not "r" in c2:
                    self.board[x-1][y+1]+="r"
                    self.board[x-1][y]+=str(pl)
                    self.score[pl-1]+=1
                elif "r" in c2 and not "u" in c2:
                    self.board[x-1][y+1]+="u"
                    self.board[x-1][y]+=str(pl)
                    self.score[pl-1]+=1
        if x<29 and y>0 and "u" in c and "r" in c:
            if not [x+1,y-1] in self.working and not "1" in self.board[x][y-1] and not "2" in self.board[x][y-1]:
                c2 = self.board[x+1][y-1]
                if "d" in c2 and not "l" in c2:
                    self.board[x+1][y-1]+="l"
                    self.board[x][y-1]+=str(pl)
                    self.score[pl-1]+=1
                elif "l" in c2 and not "d" in c2:
                    self.board[x+1][y-1]+="d"
                    self.board[x][y-1]+=str(pl)
                    self.score[pl-1]+=1
        if x<29 and y<29 and "d" in c and "r" in c:
            if not [x+1,y+1] in self.working and not "1" in self.board[x][y] and not "2" in self.board[x][y]:
                c2 = self.board[x+1][y+1]
                if "l" in c2 and not "u" in c2:
                    self.board[x+1][y+1]+="u"
                    self.board[x][y]+=str(pl)
                    self.score[pl-1]+=1
                elif "u" in c2 and not "l" in c2:
                    self.board[x+1][y+1]+="l"
                    self.board[x][y]+=str(pl)
                    self.score[pl-1]+=1
    
        if x>0 and y>0:
            if not [x-1,y-1] in self.working:
                self.fillBox(x-1,y-1,pl)
        if x>0 and y<29:
            if not [x-1,y+1] in self.working:
                self.fillBox(x-1,y+1,pl)
        if x<29 and y<0:
            if not [x+1,y-1] in self.working:
                self.fillBox(x+1,y-1,pl)
        if x<29 and y<29:
            if not [x+1,y+1] in self.working:
                self.fillBox(x+1,y+1,pl)

        if x>0:
            if not [x-1,y] in self.working:
                self.fillBox(x-1,y,pl)
        if x<29:
            if not [x+1,y] in self.working:
                self.fillBox(x+1,y,pl)
        if y>0:
            if not [x,y-1] in self.working:
                self.fillBox(x,y-1,pl)
        if y<29:
            if not [x,y+1] in self.working:
                self.fillBox(x,y+1,pl)
    def moved(self): #A turn has finished
        self.placing = False
        s = self.score[self.turn-1]-1
        while s!=self.score[self.turn-1]:
            self.working = []
            s = self.score[self.turn-1]+0
            self.fillBox(self.sel[0],self.sel[1],self.turn)
        if self.score[0]+self.score[1]>=840:
            self.win = True
        else:
            self.turn = int(self.turn==1)+1
    def left(self):
        if self.win:
            return 0
        if self.placing:
            if not "l" in self.board[self.sel[0]][self.sel[1]]:
                self.board[self.sel[0]][self.sel[1]]+="l"
                if self.sel[0]>0:
                    self.board[self.sel[0]-1][self.sel[1]]+="r"
                self.moved()
        else:
            self.sel[0]-=1
            if self.sel[0]<0:
                self.sel[0]=29
        self.render()
    def right(self):
        if self.win:
            return 0
        if self.placing:
            if not "r" in self.board[self.sel[0]][self.sel[1]]:
                self.board[self.sel[0]][self.sel[1]]+="r"
                if self.sel[0]<29:
                    self.board[self.sel[0]+1][self.sel[1]]+="l"
                self.moved()
        else:
            self.sel[0]+=1
            if self.sel[0]>29:
                self.sel[0]=0
        self.render()
    def up(self):
        if self.win:
            return 0
        if self.placing:
            if not "u" in self.board[self.sel[0]][self.sel[1]]:
                self.board[self.sel[0]][self.sel[1]]+="u"
                if self.sel[1]>0:
                    self.board[self.sel[0]][self.sel[1]-1]+="d"
                self.moved()
        else:
            self.sel[1]-=1
            if self.sel[1]<0:
                self.sel[1]=29
        self.render()
    def down(self):
        if self.win:
            return 0
        if self.placing:
            if not "d" in self.board[self.sel[0]][self.sel[1]]:
                self.board[self.sel[0]][self.sel[1]]+="d"
                if self.sel[1]<29:
                    self.board[self.sel[0]][self.sel[1]+1]+="u"
                self.moved()
        else:
            self.sel[1]+=1
            if self.sel[1]>29:
                self.sel[1]=0
        self.render()
    def place(self):
        if self.win:
            self.generateBoard()
            self.win = False
            self.sel = [10,10]
            self.score = [0,0]
            self.render()
        elif self.placing:
            self.exitGame()
        else:
            t = "l" in self.board[self.sel[0]][self.sel[1]] and "r" in self.board[self.sel[0]][self.sel[1]] and "u" in self.board[self.sel[0]][self.sel[1]] and "d" in self.board[self.sel[0]][self.sel[1]]
            if not t:
                self.placing = True
                self.render()
    
    def generateBoard(self): #Makes a new board
        self.board = []
        for y in range(30):
            self.board.append([])
            for x in range(30):
                self.board[y].append("")
    def render(self): #Draws all the blocks
        self.scr.clear()
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                self.scr.circle((x*3)+2,(y*3)+2,1,True)
                if "u" in b:
                    self.scr.line((x*3)+2,(y*3)+2,(x*3)+2,(y*3)-1)
                if "d" in b:
                    self.scr.line((x*3)+2,(y*3)+2,(x*3)+2,(y*3)+5)
                if "l" in b:
                    self.scr.line((x*3)+2,(y*3)+2,(x*3)-1,(y*3)+2)
                if "r" in b:
                    self.scr.line((x*3)+2,(y*3)+2,(x*3)+5,(y*3)+2)
                if "1" in b:
                    self.scr.line((x*3)+2,(y*3)+2,(x*3)+5,(y*3)+5)
                elif "2" in b:
                    self.scr.line((x*3)+5,(y*3)+2,(x*3)+2,(y*3)+5)
        self.scr.text(90,2,"Player 1: "+str(self.score[0]))
        self.scr.text(90,14,"Player 2: "+str(self.score[1]))
        if self.turn==1:
            self.scr.text(90,26,"Player 1's turn")
        else:
            self.scr.text(90,26,"Player 2's turn")
        if self.win:
            self.scr.text(90,62,"Press 3 to restart")
            if self.turn==1:
                self.scr.text(90,50,"Player 1 wins!")
            else:
                self.scr.text(90,50,"Player 2 wins!")
        if self.placing:
            self.scr.rectangle((self.sel[0]*3)+1,(self.sel[1]*3)+1,(self.sel[0]*3)+3,(self.sel[1]*3)+3,True)
        else:
            self.scr.circle((self.sel[0]*3)+2,(self.sel[1]*3)+2,8,False)
        self.scr.update()
    def loop(self):
        pass
