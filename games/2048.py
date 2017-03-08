from random import randint

class Main():
    def __init__(self,game,exitGame):
        game.downBind[0] = self.moveLeft
        game.downBind[1] = self.moveUp
        game.downBind[2] = self.button_3
        game.downBind[3] = self.moveDown
        game.downBind[4] = self.moveRight
        self.scr = game
        self.score = 0
        self.win = False
        self.lost = True
        self.quit = exitGame
        
        self.board = []
        for y in range(4):
            self.board.append([])
            for x in range(4):
                self.board[y].append(0)
        self.board[1][0]=2
        self.board[0][2]=4
        game.text(60,2,"Controlls")
        game.text(2,16,"1 - Shift left")
        game.text(2,28,"2 - Shift up")
        game.text(2,40,"3 - Quit game")
        game.text(2,52,"4 - Shift down")
        game.text(2,64,"5 - Shift right")
        game.text(2,78,"Press 3 to start")
        game.update()
    def button_3(self): #Button 3 was pressed
        if self.lost:
            self.board = []
            for y in range(4):
                self.board.append([])
                for x in range(4):
                    self.board[y].append(0)
            self.board[1][0]=2
            self.board[0][2]=4
            self.lost = False
            self.win = False
            self.render()
        else:
            self.quit()
    def checkLost(self): #Returns true if the game has been lost
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                if b==0:
                    return False
                if x>0:
                    if self.board[x-1][y]==b:
                        return False
                if x<3:
                    if self.board[x+1][y]==b:
                        return False
                if y>0:
                    if a[y-1]==b:
                        return False
                if y<3:
                    if a[y+1]==b:
                        return False
        return True
    def goStep(self): #A move has been done
        r = False
        for x in self.board:
            for y in x:
                if y==0:
                    r = True
                    break
            if r:
                break
        if r:
            xr = randint(0,3)
            yr = randint(0,3)
            while self.board[xr][yr]!=0:
                xr = randint(0,3)
                yr = randint(0,3)
            self.board[xr][yr]=2
        if self.checkLost():
            self.lost = True
        self.render()
    def makeWin(self): #Makes the player win
        self.win = True
        self.lost = True
    def moveUp(self): #Moves all the blocks up
        if self.lost:
            return 0
        has = 0
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                if b!=0 and y>0:
                    ind = y+0
                    for i in range(1,4):
                        if a[ind-i]!=0 or ind-i<=0:
                            ind = ind-i
                            break
                    if y!=ind+1:
                        has+=1
                    if a[ind]!=0:
                        if a[ind]==b:
                            self.score+=b
                            a[ind]*=2
                            if a[ind]==2048:
                                self.makeWin()
                            a[y]=0
                            has+=1
                        else:
                            s = b+0
                            a[y] = 0
                            a[ind+1]=s
                    else:
                        s = b+0
                        a[y] = 0
                        a[ind]=s
        if has!=0:
            self.goStep()
    def moveDown(self): #Moves all the blocks down
        if self.lost:
            return 0
        has = 0
        for x,a in enumerate(self.board):
            for y2 in range(4):
                y = 3-y2
                b = a[y]
                if b!=0 and y<3:
                    ind = y+0
                    for i in range(1,4):
                        if a[ind+i]!=0 or ind+i>=3:
                            ind = ind+i
                            break
                    if y!=ind-1:
                        has+=1
                    if a[ind]!=0:
                        if a[ind]==b:
                            self.score+=b
                            a[ind]*=2
                            if a[ind]==2048:
                                self.makeWin()
                            a[y]=0
                            has+=1
                        else:
                            s = b+0
                            a[y] = 0
                            a[ind-1]=s
                    else:
                        s = b+0
                        a[y] = 0
                        a[ind]=s
        if has!=0:
            self.goStep()
    def moveLeft(self): #Moves all the blocks left
        if self.lost:
            return 0
        has = 0
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                if b!=0 and x>0:
                    ind = x+0
                    for i in range(1,4):
                        if self.board[ind-i][y]!=0 or ind-i<=0:
                            ind = ind-i
                            break
                    if x!=ind+1:
                        has+=1
                    if self.board[ind][y]!=0:
                        if self.board[ind][y]==b:
                            self.score+=b
                            self.board[ind][y]*=2
                            if self.board[ind][y]==2048:
                                self.makeWin()
                            a[y]=0
                            has+=1
                        else:
                            s = b+0
                            a[y] = 0
                            self.board[ind+1][y] = s
                    else:
                        s = b+0
                        a[y] = 0
                        self.board[ind][y] = s
        if has!=0:
            self.goStep()
    def moveRight(self): #Moves all the blocks right
        if self.lost:
            return 0
        has = 0
        for x2 in range(4):
            x = 3-x2
            a = self.board[x]
            for y,b in enumerate(a):
                if b!=0 and x<3:
                    ind = x+0
                    for i in range(1,4):
                        if self.board[ind+i][y]!=0 or ind+i>=3:
                            ind = ind+i
                            break
                    if x!=ind-1:
                        has+=1
                    if self.board[ind][y]!=0:
                        if self.board[ind][y]==b:
                            self.score+=b
                            self.board[ind][y]*=2
                            if self.board[ind][y]==2048:
                                self.makeWin()
                            a[y]=0
                            has+=1
                        else:
                            s = b+0
                            a[y] = 0
                            self.board[ind-1][y] = s
                    else:
                        s = b+0
                        a[y] = 0
                        self.board[ind][y] = s
        if has!=0:
            self.goStep()
    def render(self): #Draws the board
        self.scr.clear()
        self.scr.rectangle(56,1,144,88,False)
        for i in range(4):
            self.scr.line(56+(i*22),1,56+(i*22),88)
            self.scr.line(56,1+(i*22),144,1+(i*22))
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                if b!=0:
                    if b>=1000:
                        self.scr.text(57+(x*22),1+(y*22),str(b)[:3])
                        self.scr.text(57+(x*22),11+(y*22),str(b)[3:])
                    else:
                        self.scr.text(57+(x*22),1+(y*22),str(b))
        self.scr.text(2,2,"Score")
        self.scr.text(2,12,str(self.score))
        if self.win:
            self.scr.text(150,2,"YOU")
            self.scr.text(150,12,"WON!")
            self.scr.text(0,32,"Press 3")
            self.scr.text(15,42,"to")
            self.scr.text(0,52,"restart")
        elif self.lost:
            self.scr.text(150,2,"GAME")
            self.scr.text(150,12,"OVER")
            self.scr.text(0,32,"Press 3")
            self.scr.text(15,42,"to")
            self.scr.text(0,52,"restart")
        self.scr.update()
    def loop(self):
        pass
