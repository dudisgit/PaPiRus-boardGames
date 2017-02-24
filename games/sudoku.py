#Idk the name of this game
from random import randint
import pickle

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        self.exitGame = exitGame
        game.downBind[0] = self.nextIn
        game.downBind[1] = self.nextOut
        game.downBind[2] = self.increment
        game.downBind[3] = self.reset
        game.downBind[4] = self.quitGame
        self.exitGame = exitGame
        self.ind = 0
        self.board = []
        self.win = False
        self.startup = True
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
        game.text(30,14,"Load from last game?")
        game.text(5,3,"Yes")
        game.text(175,3,"No")
        game.text(60,40,"Controlls")
        game.text(5,50,"1 - Next hole")
        game.text(5,60,"2 - Next squere")
        game.text(5,70,"3 - Increment hole")
        game.text(5,80,"5 - Exit game")
        game.update()
    def quitGame(self): #Quits the game
        if self.startup:
            self.startup = False
            self.generateBoard()
            self.render()
            self.scr.updateFull()
            return 0
        if not self.win:
            file = open("sudoku.save","wb")
            file.write(pickle.dumps([self.board,self.ind]))
            file.close()
        self.exitGame()
    def checkUp(self,lis): #Returns true if the list contains numbers 1-9
        ref = []
        for a in lis:
            if a[0] in lis:
                return False
            lis.append(a[0])
        if len(ref)==9 and not 10 in ref:
            return True
        return False
    def box(self,x,y,trim): #Returns a list of numbers for the square at x,y
        lis = {}
        for ix in range(trim[0],3):
            for iy in range(trim[1],3):
                lis[self.board[(int(x/3)*3)+ix][(int(y/3)*3)+iy][0]]=[(int(x/3)*3)+ix,(int(y/3)*3)+iy]
        return lis
    def reset(self): #Reset the board ones the player has won
        if self.win:
            self.win = False
            self.ind = 0
            self.generateBoard()
            self.render()
            self.scr.updateFull()
    def generateBoard(self): #Generates a new board to play
        #This algorithm works by making a solved board and then removing some numbers
        self.board = []
        numList = []
        #Generate 32 lists of numbers 1-9 in randomly order
        for i in range(42):
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

        #Allredey existing board
        self.board[0][0][0]=6
        self.board[1][0][0]=8
        self.board[2][0][0]=2
        self.board[3][0][0]=9
        self.board[4][0][0]=4
        self.board[5][0][0]=7
        self.board[6][0][0]=5
        self.board[7][0][0]=1
        self.board[8][0][0]=3

        self.board[0][1][0]=3
        self.board[1][1][0]=1
        self.board[2][1][0]=4
        self.board[3][1][0]=6
        self.board[4][1][0]=2
        self.board[5][1][0]=5
        self.board[6][1][0]=7
        self.board[7][1][0]=9
        self.board[8][1][0]=8

        self.board[0][2][0]=9
        self.board[1][2][0]=7
        self.board[2][2][0]=5
        self.board[3][2][0]=8
        self.board[4][2][0]=3
        self.board[5][2][0]=1
        self.board[6][2][0]=4
        self.board[7][2][0]=6
        self.board[8][2][0]=2

        self.board[0][3][0]=2
        self.board[1][3][0]=5
        self.board[2][3][0]=7
        self.board[3][3][0]=3
        self.board[4][3][0]=8
        self.board[5][3][0]=6
        self.board[6][3][0]=9
        self.board[7][3][0]=4
        self.board[8][3][0]=1

        self.board[0][4][0]=1
        self.board[1][4][0]=4
        self.board[2][4][0]=6
        self.board[3][4][0]=7
        self.board[4][4][0]=9
        self.board[5][4][0]=2
        self.board[6][4][0]=3
        self.board[7][4][0]=8
        self.board[8][4][0]=5

        self.board[0][5][0]=8
        self.board[1][5][0]=9
        self.board[2][5][0]=3
        self.board[3][5][0]=1
        self.board[4][5][0]=5
        self.board[5][5][0]=4
        self.board[6][5][0]=6
        self.board[7][5][0]=2
        self.board[8][5][0]=7

        self.board[0][6][0]=7
        self.board[1][6][0]=6
        self.board[2][6][0]=9
        self.board[3][6][0]=2
        self.board[4][6][0]=1
        self.board[5][6][0]=3
        self.board[6][6][0]=8
        self.board[7][6][0]=5
        self.board[8][6][0]=4

        self.board[0][7][0]=4
        self.board[1][7][0]=2
        self.board[2][7][0]=8
        self.board[3][7][0]=5
        self.board[4][7][0]=7
        self.board[5][7][0]=9
        self.board[6][7][0]=1
        self.board[7][7][0]=3
        self.board[8][7][0]=6

        self.board[0][8][0]=5
        self.board[1][8][0]=3
        self.board[2][8][0]=1
        self.board[3][8][0]=4
        self.board[4][8][0]=6
        self.board[5][8][0]=8
        self.board[6][8][0]=2
        self.board[7][8][0]=7
        self.board[8][8][0]=9
        
        for i in range(0,128): #Randomly shuffle the pre-made board
            r1 = randint(0,2) #squere x
            r2 = randint(0,2) #squere y
            r3 = randint(0,2) #shift x
            r4 = randint(0,2) #shift y
            self.board[r1*3],self.board[(r1*3)+r3]=self.board[(r1*3)+r3],self.board[r1*3]
            for i in range(9):
                self.board[i][r2*3],self.board[i][(r2*3)+r4]=self.board[i][(r2*3)+r4],self.board[i][r2*3]
       #This is the old algorithm that might be used in the future since the one obove in my opiniun is cheating!
        """
        #Make each squere contain numbers 1-9
        for x in range(3):
            for y in range(3):
                nums = numList.pop()
                for cx in range(3): #Squere
                    for cy in range(3): #Squere
                        self.board[(x*3)+cx][(y*3)+cy][0] = nums.pop()
        self.render()
        for x in range(9): #Start sorting each column
            nums = numList.pop()
            reps = [0,0,0]
            for i,a in enumerate(nums):
                if (x+1)%3==1: #At the start of the box
                    nuz = self.box(x,i,[0,0])
                    reps = [0,0,0]
                    self.board[x][i],self.board[nuz[a][0]][nuz[a][1]]=self.board[nuz[a][0]][nuz[a][1]],self.board[x][i]
                elif (x+1)%3==2: #At the middle of the box
                    for b in range(3):
                        if reps[b]<3:
                            nuz = self.box(x,b*3,[1,0])
                            if a in nuz:
                                self.board[x][(b*3)+reps[b]],self.board[nuz[a][0]][nuz[a][1]] = self.board[nuz[a][0]][nuz[a][1]],self.board[x][(b*3)+reps[b]]
                                reps[b]+=1
                                break
        for y in range(9): #Start sorting each row
            #This side of things is broken and was why i went to the algorithm obove
            nums = numList.pop()
            print("new",nums)
            reps = [[],[],[]]
            for i,a in enumerate(nums):
                if (y+1)%3==1: #At the start of the box
                    for b in range(3):
                        if len(reps[b])<3:
                            nuz = self.box(b*3,y,[0,0])
                            if not nuz[a][0] in reps[b]:
                                self.board[nuz[a][0]][y],self.board[nuz[a][0]][nuz[a][1]]=self.board[nuz[a][0]][nuz[a][1]],self.board[nuz[a][0]][y]
                                reps[b].append(nuz[a][0]+0)
                                print("swap",self.board[nuz[a][0]][y],self.board[nuz[a][0]][nuz[a][1]])
                                break
                elif (y+1)%3==2 and False: #At the middle of the box
                    for b in range(3):
                        if reps[b]<3:
                            nuz = self.box(x,b*3,[1,0])
                            if a in nuz:
                                self.board[x][(b*3)+reps[b]],self.board[nuz[a][0]][nuz[a][1]] = self.board[nuz[a][0]][nuz[a][1]],self.board[x][(b*3)+reps[b]]
                                reps[b]+=1
                                break"""
        for x in range(3):
            for y in range(3):
                sq = self.box(x*3,y*3,[0,0])
                sql = list(sq)
                for i in range(6):
                    vl = sq[sql.pop(randint(0,len(sql)-1))]
                    self.board[vl[0]][vl[1]] = [10,False]
        
        while self.board[self.ind%9][int(self.ind/9)][1]: #Make sure the selecter box isn't on a number
            self.nextIn(0)
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
        if not self.board[self.ind%9][int(self.ind/9)][1] and not self.win and not self.startup:
            self.board[self.ind%9][int(self.ind/9)][0]+=1
            if self.board[self.ind%9][int(self.ind/9)][0]>9:
                self.board[self.ind%9][int(self.ind/9)][0]=1
            if self.checkWin():
                self.win = True
            self.render()
    def nextIn(self,*ev): #Moves the selection box inside the 9 boxes on the screen
        if self.win:
            return 0
        if self.startup:
            file = open("sudoku.save","rb")
            d = pickle.loads(file.read())
            file.close()
            self.board = d[0]
            self.ind = d[1]
            self.render()
            self.scr.updateFull()
            self.startup = False
            return 0
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
        if self.win or self.startup:
            return 0
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
        if self.win:
            self.scr.text(10,0,"YOU")
            self.scr.text(10,10,"WIN")
            self.scr.text(162,0,"Press")
            self.scr.text(162,10,"4 to")
            self.scr.text(162,20,"play")
            self.scr.text(162,30,"again")
        else:
            self.scr.circle(int(46.6+((self.ind%9)*13.2)),int(6.25+(int(self.ind/9)*10.5)),10,False)
        self.scr.update()
    def loop(self):
        pass
