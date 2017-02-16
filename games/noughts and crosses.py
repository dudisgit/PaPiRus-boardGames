#noughts and crosses game


class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.board = [0,0,0,0,0,0,0,0,0]
        self.ind = 0
        game.downBind[0] = self.slideSmall
        game.downBind[1] = self.slideBig
        game.downBind[3] = exitGame
        game.clear()
        game.text(60,0,"Controlls")
        game.text(5,10,"1 - Switch column")
        game.text(5,20,"2 - Switch row")
        game.text(5,30,"3 - Place spot")
        game.text(5,40,"4 - Exit game")
        game.text(40,70,"Play againsed AI?")
        game.text(5,80,"Yes")
        game.text(175,80,"No")
        self.starting = True
        game.update()
    def drawItem(self,ind,typ): #Draw an object in cell index <ind>
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
        self.drawItem(self.ind,"sel")
        self.scr.update()
    def slideBig(self):
        if self.starting:
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
        if self.starting:
            return 0
        self.ind+=1
        if self.ind%3==0:
            self.ind-=3
        while self.board[self.ind]!=0:
            self.ind+=1
            if self.ind>=9:
                self.ind = 0
        self.render()
    def loop(self):
        pass
