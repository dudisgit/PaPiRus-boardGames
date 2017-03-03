from random import randint
import time
import socket #This is for connecting it to a hub (anouther PI that displays the game)

def nothing(*ev):
    pass
def isNumber(ch):
    return ch in ["0","1","2","3","4","5","6","7","8","9"]
def checkIp(ip): #Returns true if the ip is correct
    dot = 0
    for a in ip:
        if not a in ["0","1","2","3","4","5","6","7","8","9","."]:
            return False
        if a==".":
            dot+=1
    if dot!=3:
        return False
    sp = ip.split(".")
    for a in sp:
        if a=="":
            return False
        if int(a)>255:
            return False
    return True
def randomCard():
    num = randint(0,14)
    col = randint(1,4)
    if num<10:
        if col==1:
            return str(num)+"blue"
        elif col==2:
            return str(num)+"green"
        elif col==3:
            return str(num)+"orange"
        elif col==4:
            return str(num)+"red"
    elif num==10:
        return "all"
    elif num==11:
        if col==1:
            return "cblue"
        elif col==2:
            return "cgreen"
        elif col==3:
            return "corange"
        elif col==4:
            return "cred"
    elif num==12:
        if col==1:
            return "sblue"
        elif col==2:
            return "sgreen"
        elif col==3:
            return "sorange"
        elif col==4:
            return "sred"
    elif num==13:
        if col==1:
            return "x2blue"
        elif col==2:
            return "x2green"
        elif col==3:
            return "x2orange"
        elif col==4:
            return "x2red"
    elif num==14:
        return "x4"
    return "uno"
def possibleCards(cards,cur,col,lost): #Returns a list of possible cards for the currently placed card
    crds = []
    if cur=="x2" or cur=="x4" and not lost:
        force = False
        for a in cards:
            if (a[:2]=="x2" and cur[:2]=="x2") or (a[:2]=="x2" and cur=="x4" and a[2:]==col) or a=="x4":
                force = True
                crds.append(a)
        if force:
            return True,crds
    for a in cards:
        if isNumber(a[0]) or a[0] in ["s","c"]:
            if a[0]==cur or a[1:]==col:
                crds.append(a)
        elif a[:2]=="x2":
            if cur=="x2" or a[2:]==col:
                crds.append(a)
        elif a=="all" or a=="x4":
            crds.append(a)
    return False,crds
def calculateScore(cards):
    score = 0
    for a in cards:
        if isNumber(a[0]):
            score+=int(a[0])
        else:
            if a[:2]=="x2" or a[0]=="s" or a[0]=="c":
                score+=20
            elif a=="x4" or a=="all":
                score+=50
    return score

class Slider():
    def __init__(self,text,x,y,fro,to):
        self.value = fro+0
        self.min = fro
        self.max = to
        self.text = text
        self.pos = [x,y]
    def upClick(self):
        self.value+=1
        if self.value>self.max:
            self.value = self.max+0
    def downClick(self):
        self.value-=1
        if self.value<self.min:
            self.value = self.min+0
    def draw(self,scr):
        x,y = self.pos[0],self.pos[1]
        scr.text(x,y,self.text)
        scr.text(x+180-(len(str(self.value))*8),y,str(self.value))
        scr.rectangle(x,y+15,x+180,y+25,False)
        scr.rectangle(x+2,y+17,x+2+(((self.value-self.min)/(self.max-self.min))*176),y+23,True)
    def drawSelect(self,scr):
        scr.rectangle(self.pos[0]-2,self.pos[1]-2,self.pos[0]+182,self.pos[1]+27,False)

class CheckButton():
    def __init__(self,text,x,y):
        self.text = text
        self.pos = [x,y]
        self.value = False
    def upClick(self):
        self.value = not self.value
    def downClick(self):
        self.value = not self.value
    def draw(self,scr):
        scr.rectangle(self.pos[0],self.pos[1],self.pos[0]+13,self.pos[1]+13,False)
        if self.value:
            scr.rectangle(self.pos[0]+2,self.pos[1]+2,self.pos[0]+11,self.pos[1]+11,True)
        scr.text(self.pos[0]+17,self.pos[1],self.text)
    def drawSelect(self,scr):
        scr.rectangle(self.pos[0]-2,self.pos[1]-2,self.pos[0]+17+(len(self.text)*8),self.pos[1]+15,False)

class Button():
    def __init__(self,text,x,y,*ext):
        self.text = text
        self.pos = [x,y]
        self.bind = None
        if len(ext)!=0:
            self.bind = ext[0]
        self.upClick = self.doButton
        self.downClick = self.doButton
    def doButton(self):
        if self.bind!=None:
            self.bind()
    def draw(self,scr):
        scr.rectangle(self.pos[0],self.pos[1],self.pos[0]+(len(self.text)*8),self.pos[1]+12,False)
        scr.text(self.pos[0]+1,self.pos[1],self.text)
    def drawSelect(self,scr):
        scr.rectangle(self.pos[0]-2,self.pos[1]-2,self.pos[0]+(len(self.text)*8)+2,self.pos[1]+14,False)

class Text():
    def __init__(self,text,x,y):
        self.text = text
        self.pos = [x,y]
        self.upClick = nothing
        self.downClick = nothing
        self.drawSelect = nothing
    def draw(self,scr):
        scr.text(self.pos[0],self.pos[1],self.text)

class Image():
    def __init__(self,path,x,y):
        self.image = path
        self.pos = [x,y]
        self.upClick = nothing
        self.downClick = nothing
        self.drawSelect = nothing
    def draw(self,scr):
        scr.image(self.pos[0],self.pos[1],self.image)

class CardList():
    def __init__(self,cards,active):
        self.cards = cards
        self.activeCards = []
        for i in range(0,len(cards)):
            self.activeCards.append(False)
        self.active = active
        self.sel = 0
    def convert(self,alo):
        self.activeCards = []
        for a in self.cards:
            if a in alo:
                self.activeCards.append(False)
            else:
                self.activeCards.append(True)
    def draw(self,scr):
        scr.rectangle(3,55,197,96,False)
        for i,a in enumerate(self.cards[int(self.sel/5)*5:(int(self.sel/5)*5)+5]):
            scr.image((i*40)+1,55,"games/UNO images/"+a+".png")
            if self.active and self.activeCards[(int(self.sel/5)*5)+i]:
                for b in range(0,10):
                    scr.line((i*40)+2,56+(b*4),(i*40)+39,56+(b*4))#,95)
        scr.rectangle(((self.sel%5)*40),54,((self.sel%5)*40)+40,95,False)
    def upClick(self): #Jump a space
        self.sel+=1
        if self.sel%5==0:
            self.sel-=5
        if self.sel>=len(self.cards):
            if self.sel-(self.sel%5)==0:
                self.sel-=self.sel%5
            else:
                self.sel -= (self.sel%5)-1
        if self.sel>=len(self.cards):
            self.sel-=len(self.cards)
        if self.sel<0:
            self.sel=0
    def downClick(self): #Jump to next column
        self.sel+=5
        self.sel = self.sel-(self.sel%5)
        if self.sel>=len(self.cards):
            self.sel=self.sel%len(self.cards)
        if self.sel<0:
            self.sel=0
    def drawSelect(self,scr):
        scr.rectangle(1,53,199,96,False)


class Player():
    def __init__(self,name,numCards):
        self.name = name
        self.cards = []
        for i in range(numCards):
            self.cards.append(randomCard())
        self.uno = False
        self.unoCatch = ""

class Caller():
    def __init__(self,cal,*pars):
        self.bind = cal
        self.pars = pars
    def do(self):
        self.bind(*self.pars)

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        game.downBind[0] = self.button_1
        game.downBind[1] = self.button_2
        game.downBind[2] = self.loadQuit
        game.downBind[3] = self.button_4
        game.downBind[4] = self.button_5
        
        self.exitGame = exitGame
        self.exit = False
        self.screen = 0
        #Screens
        #0: Setup screen
        #1: Setup ip typing screen
        #2: Next turn screen
        #3: Given cards screen
        #4: Main screen
        #5: The player viewing screen
        #6: The colour selecting screen
        #7: Direction selecting screen
        #8: The winning screen
        
        self.focus = 0
        self.quit = False
        self.sock = None
        self.hubIp = "10.20.0.1"
        self.info = {}
        self.info["cards"] = 0
        self.info["players"] = 0
        self.info["hub"] = False

        self.game = {}
        self.game["dir"] = 0 #Direction of the game
        self.game["player"] = 0 #Current player
        self.game["players"] = [Player("Testing player",14)]
        for i in range(7):
            self.game["players"].append(Player("player-"+str(i),14))
        while True:
            self.game["card"] = randomCard()
            if self.game["card"]!="x4" and self.game["card"]!="all" and self.game["card"][:2]!="x2":
                break
        if isNumber(self.game["card"][0]) or self.game["card"][0] in ["s","c"]:
            self.game["color"] = self.game["card"][1:]
        elif self.game["card"][:2]=="x2":
            self.game["color"] = self.game["card"][2:]
        else:
            self.game["color"] = "Err"
        self.game["stack"] = 0
        self.game["stackers"] = []
        self.game["first"] = True
        self.widg = []
        
        self.widg.append(Slider("Players",10,3,2,12))
        self.widg.append(Slider("Cards per player",10,34,3,24))
        self.widg.append(CheckButton("Connect to hub",10,64))
        self.widg.append(Button("Next",80,80,self.setupNext))

        game.text(60,2,"Controlls")
        game.text(2,14,"1 - Before widget")
        game.text(2,26,"2 - After widget")
        game.text(2,38,"3 - Quit game (prompt)")
        game.text(2,50,"4 - 'back' widget fucntion")
        game.text(2,62,"5 - 'after' widget fucntion")
        game.text(2,76,"Press 1 or 2 to continue")
        
        game.update()
    def setupNext(self): #Next button on the setup screen was pressed
        self.info["players"] = self.widg[0].value
        self.info["cards"] = self.widg[1].value
        self.info["hub"] = self.widg[2].value == True
        self.game["players"] = []
        self.game["player"] = 0
        self.game["dir"] = 0
        for pl in range(self.info["players"]):
            self.game["players"].append(Player("Player "+str(pl),self.info["cards"]))
        if self.info["hub"]:
            self.loadHubJoin()
        else:
            self.loadNext()

    #Quitting screen
    def loadQuit(self):
        self.scr.text(0,0,"Yes")
        self.scr.text(180,0,"No")
        self.scr.text(0,20,"Are you sure you want to quit?")
        self.scr.update()
        self.quit = True
    
    
    #Wining screen
    def quitGameSafe(self): #Safely quit the game
        self.exit = True
        if self.sock!=None:
            self.sock.close()
        self.exitGame()
    def loadWin(self,pl):
        self.widg = []
        self.screen = 8
        self.widg.append(Text(pl+" wins!",2,2))
        for i,a in enumerate(self.game["players"]):
            self.widg.append(Text(a.name+" "+str(calculateScore(a.cards)),2+(int(i/4)*75),18+(i*18)-(int(i/4)*72)))
        self.widg.append(Button("QUIT",164,2,self.quitGameSafe))
        self.focus = len(self.widg)-1
    
    #Select direction screen
    def setDirection(self,d):
        self.game["dir"] = d
        if self.game["card"][0]=="c":
            self.game["player"]+=self.game["dir"]*2
        else:
            self.game["player"]+=self.game["dir"]
        if self.game["player"]<0:
            self.game["player"]+=len(self.game["players"])
        if self.game["player"]>=len(self.game["players"]):
            self.game["player"]-=len(self.game["players"])
        self.loadNext()
    def loadDirection(self):
        self.widg = []
        self.focus = 1
        self.screen = 7
        self.widg.append(Text("Which direction?",2,2))
        self.widg.append(Button("Left",2,40,lambda: self.setDirection(-1)))
        self.widg.append(Button("Right",160,40,lambda: self.setDirection(1)))
    
    #Select Colour screen
    def colourSelect(self,col):
        self.nextGo(self.widg[-1].dump,col)
    def loadColour(self,crd):
        self.widg = []
        self.screen = 6
        self.widg.append(Text("What colour is the card?",2,2))
        self.widg.append(Button("Red",30,20,lambda: self.colourSelect("red")))
        self.widg.append(Button("Green",80,20,lambda: self.colourSelect("green")))
        self.widg.append(Button("Orange",30,50,lambda: self.colourSelect("orange")))
        self.widg.append(Button("Blue",80,50,lambda: self.colourSelect("blue")))
        self.focus = 2
        self.widg[-1].dump = crd #Bad way but it works!
    
    
    #New cards screen
    def cardsNext(self):
        self.loadGame()
        typ = "NONE"
        col = self.game["color"]
        crd = self.game["card"]
        if isNumber(crd[0]):
            typ = str(crd[0])
        elif crd[0]=="s":
            typ="s"
        elif crd[0]=="c":
            typ="c"
        elif crd=="all":
            typ="all"
        elif crd=="x4":
            typ="x4"
        elif crd[0]=="x":
            typ="x2"
        self.game["players"][self.game["player"]].unoCatch = ""
        has,poss = possibleCards(self.game["players"][self.game["player"]].cards,typ,col,True)
        self.widg[-1].convert(poss)
    def loadCards(self,crds):
        self.widg = []
        self.screen = 3
        self.widg.append(Text("CARDS!",2,2))
        if self.game["players"][self.game["player"]].unoCatch!="":
            self.widg.append(Text(self.game["players"][self.game["player"]].unoCatch,2,20))
            self.widg.append(Text("Caught you for not saying UNO",2,30))
        elif len(self.game["stackers"])==1:
            self.widg.append(Text(self.game["stackers"][0]+" gave you cards",2,20))
        elif len(self.game["stackers"])==0:
            self.widg.append(Text("You got cards!",2,20))
        else:
            add = self.game["stackers"][0]
            for a in self.game["stackers"][1:]:
                add+=", "+a
            self.widg.append(Text(add,2,20))
            self.widg.append(Text("gave you cards",2,30))
        self.widg.append(CardList(crds,False))
        self.widg.append(Button("Ok",80,40,self.cardsNext))
        self.focus = len(self.widg)-1
    
    #Load the player viewer tab (used to catch people out for not clicking UNO)
    def playerViewBack(self):
        self.screen = 4
        get = self.widg[0].dump
        self.loadGame()
        self.widg[-1].activeCards = get
    def playerCatch(self,pl):
        if len(pl.cards)==1 and not pl.uno and pl.unoCatch=="":
            pl.unoCatch = str(self.game["players"][self.game["player"]].name)
    def playerCatchAll(self):
        for i,a in enumerate(self.game["players"]):
            if i!=self.game["player"]:
                self.playerCatch(a)
    def loadPlayerView(self):
        self.screen = 5
        get = self.widg[-1].activeCards
        self.widg = []
        self.widg.append(Button("Back",2,2,self.playerViewBack))
        self.widg[0].dump = get #Very bad way of storing stuff but yeah
        self.widg.append(Button("Call out UNO for all",40,2,self.playerCatchAll))
        adz = []
        for i,a in enumerate(self.game["players"]):
            adz.append(Caller(self.playerCatch,self.game["players"][i+0]))
            self.widg.append(Button(a.name+" "+str(len(a.cards)),2+(int(i/4)*75),18+(i*18)-(int(i/4)*72),adz[i+0].do))
        self.focus = 0
    
    #Main game playing/card selecting area
    def nextGo(self,crd,col): #Put down a card and do the next go
        if crd!="none":
            self.game["card"] = crd
            if crd!="x4" and crd!="all":
                self.game["card"]+=col
                if self.sock!=None:
                    self.sock.sendall(("new,card,"+crd+col+","+self.game["players"][self.game["player"]].name).encode('ascii'))
                    time.sleep(0.1)
            elif self.sock!=None:
                self.sock.sendall(("new,card,"+crd+","+col+","+self.game["players"][self.game["player"]].name).encode('ascii'))
                time.sleep(0.1)
            self.game["color"] = col
        if crd=="x2":
            self.game["stack"]+=2
            if self.sock!=None:
                self.sock.sendall(("change,stack,"+str(self.game["stack"])).encode('ascii'))
            self.game["stackers"].append(self.game["players"][self.game["player"]].name)
        elif crd=="x4":
            self.game["stack"]+=4
            if self.sock!=None:
                self.sock.sendall(("change,stack,"+str(self.game["stack"])).encode('ascii'))
            self.game["stackers"].append(self.game["players"][self.game["player"]].name)
        if crd=="s":
            self.game["dir"]=self.game["dir"]*-1
        if crd=="c":
            self.game["player"]+=self.game["dir"]*2
        else:
            self.game["player"]+=self.game["dir"]
        if self.game["player"]<0:
            self.game["player"]+=len(self.game["players"])
        if self.game["player"]>=len(self.game["players"]):
            self.game["player"]-=len(self.game["players"])
        if self.game["first"]:
            self.loadDirection()
            self.game["first"] = False
        else:
            self.loadNext()
        
    def gameEndTurn(self): #Ending the turn button
        sel = self.widg[-1]
        acts = 0
        for a in sel.activeCards:
            if a:
                acts+=1
        if acts==len(sel.cards): #Player cannot go
            self.nextGo("none","")
            return 0
        elif sel.activeCards[sel.sel]:
            return 0
        typ = "NONE"
        col = "None"
        c = sel.cards.pop(sel.sel)
        if isNumber(c[0]) or c[0] in ["s","c"]:
            typ = c[0]
            col = c[1:]
        elif c[:2]=="x2":
            typ="x2"
            col = c[2:]
        if len(sel.cards)==0:
            if self.sock!=None:
                self.sock.sendall(("win,"+self.game["players"][self.game["player"]].name).encode('ascii'))
            self.loadWin(self.game["players"][self.game["player"]].name)
        elif c=="x4" or c=="all":
            self.loadColour(c)
        else:
            self.nextGo(typ,col)
    def gameSayUno(self):
        p = self.game["players"][self.game["player"]]
        acts = 0
        for a in self.widg[-1].activeCards:
            if a:
                acts+=1
        if (len(p.cards)==2 and acts!=len(self.widg[-1].cards)) and not p.uno:
            p.uno = True
    def loadGame(self):
        self.screen = 4
        self.focus = 2
        self.widg = []
        self.widg.append(Button("Players ",3,3,self.loadPlayerView))
        self.widg.append(Button("Say UNO ",3,19,self.gameSayUno))
        self.widg.append(Button("End turn",3,36,self.gameEndTurn))
        self.widg.append(CardList(self.game["players"][self.game["player"]].cards,True))
    
    #Player switch screen
    def loadNextTurn(self): #Loads the next turn for the player
        pl = self.game["players"][self.game["player"]]
        typ = "NONE"
        col = self.game["color"]
        crd = self.game["card"]
        if isNumber(crd[0]):
            typ = str(crd[0])
        elif crd[0]=="s":
            typ="s"
        elif crd[0]=="c":
            typ="c"
        elif crd=="all":
            typ="all"
        elif crd=="x4":
            typ="x4"
        elif crd[0]=="x":
            typ="x2"
        must,poss = possibleCards(pl.cards,typ,col,False)
        if len(poss)==0 or ((typ=="x2" or typ=="x4") and not must) or pl.unoCatch!="":
            pl.uno = False
            crd = []
            if len(self.game["stackers"])!=0:
                for i in range(self.game["stack"]):
                    crd.append(randomCard())
            else:
                crd.append(randomCard())
            if self.sock!=None:
                self.sock.sendall(("new,pickup,"+str(len(crd))+","+pl.name).encode('ascii'))
                time.sleep(0.1)
            self.loadCards(crd)
            if self.game["stack"]!=0:
                self.game["stackers"] = []
                self.game["stack"] = 0
                if self.sock!=None:
                    self.sock.sendall(("change,stack,0").encode('ascii'))
                    time.sleep(0.1)
            for a in crd:
                pl.cards.append(a)
        else:
            self.loadGame()
            self.widg[-1].convert(poss)
    def loadNext(self):
        self.widg = []
        self.screen = 2
        self.widg.append(Text(self.game["players"][self.game["player"]].name+" turn",5,5))
        self.focus = 2
        if self.game["dir"]==0:
            self.focus = 1
        elif self.game["dir"]==1:
            self.widg.append(Image("games/UNO images/arrowRight.png",130,15))
        elif self.game["dir"]==-1:
            self.widg.append(Image("games/UNO images/arrowLeft.png",5,15))
        self.widg.append(Button("Take turn",50,80,self.loadNextTurn))
    
    #Hub screen
    def hubAddText(self,char):
        if char=="<":
            self.hubIp = self.hubIp[:len(self.hubIp)-1]
        else:
            self.hubIp+=char
        self.widg[1].text = self.hubIp
        self.widg[-1].text = ""
        self.render()
    def hubOk(self):
        if checkIp(self.hubIp):
            self.widg[-1].text = "Atempting to connect..."
            self.render()
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.settimeout(8)
            try:
                print("Connecting to ",self.hubIp)
                self.sock.connect((self.hubIp,2634))
            except:
                self.widg[-1].text = "Failed to connect!"
                self.render()
            else:
                self.widg[-1].text = "Connected, sending info..."
                self.render()
                self.sock.sendall(("new,card,"+self.game["card"]+","+self.game["color"]).encode('ascii'))
                time.sleep(0.1)
                for a in self.game["players"]:
                    self.sock.sendall(("new,player,"+a.name+","+str(self.info["cards"])).encode('ascii'))
                    time.sleep(0.1)
                self.loadNext()
        else:
            self.widg[-1].text = "Invalid IP"
            self.render()
    def loadHubJoin(self):
        self.screen = 1
        self.widg = []
        self.widg.append(Text("Enter IP of hub",2,0))
        self.widg.append(Text(self.hubIp,2,20))
        self.focus = 2
        self.widg.append(Button("0",2,40,lambda: self.hubAddText("0")))
        self.widg.append(Button("1",17,40,lambda: self.hubAddText("1")))
        self.widg.append(Button("2",32,40,lambda: self.hubAddText("2")))
        self.widg.append(Button("3",47,40,lambda: self.hubAddText("3")))
        self.widg.append(Button("4",62,40,lambda: self.hubAddText("4")))
        self.widg.append(Button("5",77,40,lambda: self.hubAddText("5")))
        self.widg.append(Button("6",92,40,lambda: self.hubAddText("6")))
        self.widg.append(Button("7",107,40,lambda: self.hubAddText("7")))
        self.widg.append(Button("8",122,40,lambda: self.hubAddText("8")))
        self.widg.append(Button("9",137,40,lambda: self.hubAddText("9")))
        self.widg.append(Button(".",152,40,lambda: self.hubAddText(".")))
        self.widg.append(Button("<<",177,40,lambda: self.hubAddText("<")))
        self.widg.append(Button("Ok",60,80,self.hubOk))
        self.widg.append(Text("",5,60))
        
    def button_1(self):
        if self.quit:
            self.quitGameSafe()
        elif len(self.widg)!=0:
            self.focus-=1
            if self.focus<0:
                self.focus = 0
            if not self.exit:
                self.render()
    def button_2(self):
        if len(self.widg)!=0:
            self.focus+=1
            if self.focus>=len(self.widg):
                self.focus = len(self.widg)-1
            if not self.exit:
                self.render()
    def button_4(self):
        if len(self.widg)!=0:
            self.widg[self.focus].downClick()
            if not self.exit:
                self.render()
    def button_5(self):
        if self.quit:
            self.quit = False
            self.render()
        elif len(self.widg)!=0:
            self.widg[self.focus].upClick()
            if not self.exit:
                self.render()
    def render(self):
        self.scr.clear()
        if self.screen==4: #Main game screen
            self.scr.text(112,14,"Stack: "+str(self.game["stack"]))
            typ = "NONE"
            if self.focus==len(self.widg)-1:
                crd = self.widg[-1].cards[self.widg[-1].sel]
                col = "None!"
                if isNumber(crd[0]) or crd[0] in ["s","c"]:
                    col = crd[1:]
                elif crd[:2]=="x2":
                    col = crd[2:]
            else:
                col = self.game["color"]
                crd = self.game["card"]
            if isNumber(crd[0]):
                typ = str(crd[0])
            elif crd[0]=="s":
                typ="Reverse"
            elif crd[0]=="c":
                typ="Skip"
            elif crd=="all":
                typ="Wild"
            elif crd=="x4":
                typ="Wild x4"
            elif crd[0]=="x":
                typ="x2"
            self.scr.image(70,0,"games/UNO images/"+self.game["card"]+".png")
            self.scr.text(112,2,"Colour: "+col)
            self.scr.text(112,26,"Type: "+typ)
            self.scr.text(112,38,"Select: "+str(self.widg[-1].sel+1)+"/"+str(len(self.widg[-1].cards)))
        self.drawWidgets()
        self.scr.update()
    def drawWidgets(self): #Draws all the widgets
        for i,a in enumerate(self.widg):
            if i==self.focus:
                a.drawSelect(self.scr)
            a.draw(self.scr)
    def loop(self):
        pass
