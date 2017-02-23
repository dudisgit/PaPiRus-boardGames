#Idk the name of this game
from random import randint

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.exitGame = exitGame
        game.downBind[0] = self.nextIn
        game.downBind[1] = self.nextOut
        game.downBind[2] = self.increment
        self.ind = 0
        self.board = []
        #Syntax for each cell in board
        #0: The number
        #1: Is perminant
        for y in range(9):
            self.board.append([])
            for x in range(9):
                rn = randint(1,16)
                if rn>=10:
                    rn = 10
                self.board[y].append([rn,rn<10])
        self.generateBoard()
        self.render()
    def checkUp(self,lis): #Returns true if the list contains numbers 1-9
        ref = []
        for a in lis:
            if a[0] in lis:
                return False
            lis.append(a[0])
        if len(ref)==9 and not 10 in ref:
            return True
        return False
    def generateBoard(self): #Generates a new board to play
        #This algorithm works by making a solved board and then removing some numbers
        self.board = []
        numList = []
        #Generate 32 lists of numbers 1-9 in randomly order
        for i in range(32):
            add = []
            gen = [i+1 for i in range(9)] #A list from 1-9 (ordered)
            for i in range(9):
                add.append(gen.pop(randint(0,len(gen)-1)))
            numList.append(add)
        #Make the board (solved)
        for x in range(9):
            self.board.append([])
            for y in range(9):
                self.board[x].append([0,True])
        #Make each squere contain numbers up to 10
        for x in range(3):
            for y in range(3):
                nums = numList.pop()
                for cx in range(3): #Squere
                    for cy in range(3): #Squere
                        self.board[(x*3)+cx][(y*3)+cy][0] = nums.pop()
        for x in range(9): #Start sorting each column
            pass
        
        while self.board[self.ind%9][int(self.ind/9)][1]: #Make sure the selecter box isn't on a number
            self.nextIn(0)
            break
    def checkWin(self): #Returns true if the game has been won
        for i in range(0,9):
            ref = []
            for y in range(0,9):
                if self.board[i][y][0] in ref:
                    return False
                ref.append(self.board[i][y][0])
            if len(ref)!=9 or 10 in ref:
                return False
            ref = []
            for x in range(0,9):
                if self.board[x][i][0] in ref:
                    return False
                ref.append(self.board[x][i][0])
            if len(ref)!=9 or 10 in ref:
                return False
        return True
    def increment(self): #Increment the box the person is currently on
        if not self.board[self.ind%9][int(self.ind/9)][1]:
            self.board[self.ind%9][int(self.ind/9)][0]+=1
            if self.board[self.ind%9][int(self.ind/9)][0]>9:
                self.board[self.ind%9][int(self.ind/9)][0]=1
            self.render()
    def nextIn(self,*ev): #Moves the selection box inside the 9 boxes on the screen
        self.ind+=1
        if self.ind%3==0: #Went over the limits of the box
            if ((int(self.ind/9)+1)%3==0 and not self.ind%9==0) or (int(self.ind/9)%3==0 and self.ind%9==0): #Start at the first item of the box
                self.ind-=21
            else: #Simply go to anouther row in the box
                self.ind+=6
        if len(ev)==0:
            while self.board[self.ind%9][int(self.ind/9)][1]:
                self.nextIn(0)
            self.render()
    def nextOut(self): #Switch between each 9 boxes on the screen
        bf = int(self.ind/9)%3
        self.ind+=3
        if int(self.ind/9)%3!=bf: #If the line has changed because it is on a new row then go to the box below
            self.ind+=18
        if self.ind>=81: #At the end of the boxes, start from begining
            self.ind-=81
        while self.board[self.ind%9][int(self.ind/9)][1]:
            self.nextIn(0)
        self.render()
    def render(self): #Draws the game
        self.scr.clear()
        self.scr.rectangle(40,1,160,95,False)
        #Draw lines
        for i in range(1,9):
            self.scr.line(40+int(i*13.2),0,40+int(i*13.2),95)
            if i%3==0:
                self.scr.line(39+int(i*13.2),0,39+int(i*13.2),95)
        for i in range(1,9):
            self.scr.line(40,1+int(i*10.5),160,1+int(i*10.5))
            if i%3==0:
                self.scr.line(40,int(i*10.5),160,int(i*10.5))
        #Draw numbers
        for x,a in enumerate(self.board):
            for y,b in enumerate(a):
                if b[0]<10:
                    self.scr.text(45+int(x*13.2),1+int(y*10.5),str(b[0]))
                    if not b[1]:
                        self.scr.rectangle(41+int(x*13.2),2+int(y*10.5),39+int((x+1)*13.2),int((y+1)*10.5),False)

        self.scr.circle(int(46.6+((self.ind%9)*13.2)),int(6.25+(int(self.ind/9)*10.5)),10,False)
        #self.scr.rectangle(41+int((self.ind%9)*13.2),2+int(int(self.ind/9)*10.5),
        #                   53+int((self.ind%9)*13.2),10+int(int(self.ind/9)*10.5),
        #                   False)
        self.scr.update()
    def loop(self):
        pass
