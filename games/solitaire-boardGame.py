#Solitare board game, not the card one!

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        game.downBind[0] = self.lastMove
        game.downBind[1] = self.nextMove
        game.downBind[2] = self.putMove
        game.downBind[3] = self.quitGame
        game.downBind[4] = exitGame
        self.holes = []
        for y in range(7):
            self.holes.append([])
            for x in range(7):
                self.holes[y].append(True)
        self.holes[3][3]=False
        self.sel = [3,1,3]
        self.selInd = 0
        self.win = False
        self.moves = [] #A list containing all the possbile moves
        #Directions
        #0: Down
        #1: Up
        #2: Left
        #3: Right
        self.getAllMoves()
        self.sel = [self.moves[0][0]+0,self.moves[0][1]+0,self.moves[0][2]+0]
        game.text(70,0,"Controlls")
        game.text(3,20,"1 - Select backwards")
        game.text(3,30,"2 - Select forwards")
        game.text(3,40,"3 - Place")
        game.text(3,50,"4 - Quit game")
        game.text(3,70,"Press 1 or 2 to play")
        game.update()
    def quitGame(self):
        if self.win:
            self.holes = []
            for y in range(7):
                self.holes.append([])
                for x in range(7):
                    self.holes[y].append(True)
            self.holes[3][3]=False
            self.selInd = 0
            self.getAllMoves()
            self.sel = [self.moves[0][0]+0,self.moves[0][1]+0,self.moves[0][2]+0]
            self.win = False
            self.render()
    def nextMove(self): #Button 2
        if self.win:
            return 0
        self.selInd+=1
        if self.selInd>=len(self.moves):
            self.selInd = 0
        self.sel = [self.moves[self.selInd][0]+0,self.moves[self.selInd][1]+0,self.moves[self.selInd][2]+0]
        self.render()
    def putMove(self): #Button 3
        if self.win:
            return 0
        if self.sel[2]==0:
            self.holes[self.sel[0]][self.sel[1]]=False
            self.holes[self.sel[0]][self.sel[1]+1]=False
            self.holes[self.sel[0]][self.sel[1]+2]=True
        elif self.sel[2]==1:
            self.holes[self.sel[0]][self.sel[1]]=False
            self.holes[self.sel[0]][self.sel[1]-1]=False
            self.holes[self.sel[0]][self.sel[1]-2]=True
        elif self.sel[2]==2:
            self.holes[self.sel[0]][self.sel[1]]=False
            self.holes[self.sel[0]-1][self.sel[1]]=False
            self.holes[self.sel[0]-2][self.sel[1]]=True
        elif self.sel[2]==3:
            self.holes[self.sel[0]][self.sel[1]]=False
            self.holes[self.sel[0]+1][self.sel[1]]=False
            self.holes[self.sel[0]+2][self.sel[1]]=True
        self.getAllMoves()
        
        self.selInd-=1
        if self.selInd<0:
            self.selInd=0
        if len(self.moves)==0:
            self.win = True
            self.sel[2]=4
        else:
            self.sel = [self.moves[self.selInd][0]+0,self.moves[self.selInd][1]+0,self.moves[self.selInd][2]+0]
        self.render()
    def lastMove(self): #Button 1
        if self.win:
            return 0
        self.selInd-=1
        if self.selInd<0:
            self.selInd = len(self.moves)-1
        self.sel = [self.moves[self.selInd][0]+0,self.moves[self.selInd][1]+0,self.moves[self.selInd][2]+0]
        self.render()
    def getPoint(self,x,y): #Returns if a point is filled, -1 if not on the board
        if (x>1 and x<5) or (y>1 and y<5):
            if x<0 or x>6 or y<0 or y>6:
                return -1
            return int(self.holes[x][y])
        return -1
    def getAllMoves(self): #Gets all the possible moves for the board
        self.moves = []
        for x,a in enumerate(self.holes):
            for y,b in enumerate(a):
                if ((x>1 and x<5) or (y>1 and y<5)) and b:
                    if self.getPoint(x,y+1)==1 and self.getPoint(x,y+2)==0:
                        self.moves.append([x+0,y+0,0])
                    if self.getPoint(x,y-1)==1 and self.getPoint(x,y-2)==0:
                        self.moves.append([x+0,y+0,1])
                    if self.getPoint(x-1,y)==1 and self.getPoint(x-2,y)==0:
                        self.moves.append([x+0,y+0,2])
                    if self.getPoint(x+1,y)==1 and self.getPoint(x+2,y)==0:
                        self.moves.append([x+0,y+0,3])
    def render(self): #Draw the board
        self.scr.clear()
        self.scr.line(82,1,120,1)
        self.scr.line(82,95,120,95)
        self.scr.line(55,28,82,28)
        self.scr.line(55,66,82,66)
        self.scr.line(120,28,147,28)
        self.scr.line(120,66,147,66)

        self.scr.line(82,1,82,28)
        self.scr.line(120,1,120,28)
        self.scr.line(82,66,82,95)
        self.scr.line(120,66,120,95)
        self.scr.line(55,28,55,66)
        self.scr.line(147,28,147,66)
        scr = 0
        for x,a in enumerate(self.holes):
            for y,b in enumerate(a):
                if ((x>1 and x<5) or (y>1 and y<5)) and b:
                    if x==self.sel[0] and y==self.sel[1]:
                        self.scr.circle(62+int(x*13),8+int(y*13),8,False)
                    else:
                        self.scr.circle(62+int(x*13),8+int(y*13),8,True)
                    scr+=1
        
        if self.sel[2]==0:
            self.scr.line(58+int(self.sel[0]*13),8+int(self.sel[1]*13),62+int(self.sel[0]*13),8+int((self.sel[1]+1)*13))
            self.scr.line(66+int(self.sel[0]*13),8+int(self.sel[1]*13),62+int(self.sel[0]*13),8+int((self.sel[1]+1)*13))
        elif self.sel[2]==1:
            self.scr.line(58+int(self.sel[0]*13),8+int(self.sel[1]*13),62+int(self.sel[0]*13),8+int((self.sel[1]-1)*13))
            self.scr.line(66+int(self.sel[0]*13),8+int(self.sel[1]*13),62+int(self.sel[0]*13),8+int((self.sel[1]-1)*13))
        elif self.sel[2]==2:
            self.scr.line(62+int(self.sel[0]*13),4+int(self.sel[1]*13),62+int((self.sel[0]-1)*13),8+int(self.sel[1]*13))
            self.scr.line(62+int(self.sel[0]*13),12+int(self.sel[1]*13),62+int((self.sel[0]-1)*13),8+int(self.sel[1]*13))
        elif self.sel[2]==3:
            self.scr.line(62+int(self.sel[0]*13),4+int(self.sel[1]*13),62+int((self.sel[0]+1)*13),8+int(self.sel[1]*13))
            self.scr.line(62+int(self.sel[0]*13),12+int(self.sel[1]*13),62+int((self.sel[0]+1)*13),8+int(self.sel[1]*13))

        if self.win:
            self.scr.text(10,0,"Score: "+str(scr))
            self.scr.text(162,0,"Press")
            self.scr.text(162,10,"4 to")
            self.scr.text(162,20,"play")
            self.scr.text(162,30,"again")
        
        self.scr.update()
    def loop(self):
        pass
