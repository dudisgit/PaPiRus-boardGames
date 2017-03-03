
#0: Empty
#1: Pawn
#2: Rook
#3: Bishop
#4: Knite
#5: Queen
#6: King

#Positive it white
#Negative is black

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.board = []
        self.sel = [4,4]
        self.newBoard()
        self.render()
    def newBoard(self):
        self.board = []
        for x in range(8):
            self.board.append([])
            for y in range(8):
                self.board[x].append(0)
        for i in range(8):
            self.board[i][1]=1
            self.board[i][6]=-1
        self.board[0][0]=2
        self.board[7][0]=2
        self.board[1][0]=4
        self.board[6][0]=4
        self.board[2][0]=3
        self.board[5][0]=3
        self.board[3][0]=5
        self.board[4][0]=6
        
        self.board[0][7]=-2
        self.board[7][7]=-2
        self.board[1][7]=-4
        self.board[6][7]=-4
        self.board[2][7]=-3
        self.board[5][7]=-3
        self.board[3][7]=-5
        self.board[4][7]=-6
        
    def render(self):
        self.scr.clear()
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                self.scr.rectangle((x*10)+60,(y*10)+8,(x*10)+70,(y*10)+18,False)
                if b!=0:
                    self.scr.image((x*10)+60,(y*10)+8,"games/Chess pieces/"+str(b)+".png")
        self.scr.circle((self.sel[0]*10)+65,(self.sel[1]*10)+13,8,False)
        self.scr.update()
    def loop(self):
        pass
