#noughts and crosses game

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.board = [0,0,0,0,0,0,0,0,0]
        self.ind = 0
        game.downBind[0] = self.slideSmall
        game.downBind[1] = self.slideBig
        self.render()
    def drawItem(self,ind): #Draw an object in cell index <ind>
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
        self.scr.rectangle(ps[0],ps[1],ps[2],ps[3],True)
    def render(self):
        self.scr.clear()
        self.scr.line(52,29,148,29)
        self.scr.line(52,67,148,67)
        self.scr.line(81,0,81,96)
        self.scr.line(119,0,119,96)
        self.drawItem(self.ind)
        
        self.scr.update()
    def slideBig(self):
        self.ind+=3
        if self.ind>=9:
            self.ind-=9
        self.render()
    def slideSmall(self):
        self.ind+=1
        if self.ind%3==0:
            self.ind-=3
        self.render()
    def loop(self):
        pass
