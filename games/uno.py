from random import randint
import socket #This is for connecting it to a hub (anouther PI that displays the game)

def nothing(*ev):
    pass
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
            self.activeCards.append(randint(0,1)==1)
        self.active = active
        self.sel = 0
    def draw(self,scr):
        scr.rectangle(3,55,197,96,False)
        for i,a in enumerate(self.cards[int(self.sel/5)*5:(int(self.sel/5)*5)+5]):
            scr.image((i*40)+1,55,"games/UNO images/"+a+".png")
            if self.active and self.activeCards[i]:
                scr.rectangle((i*40)+2,56,(i*40)+39,95,False)
                scr.rectangle((i*40)+3,57,(i*40)+38,94,False)
                scr.rectangle((i*40)+4,58,(i*40)+37,93,False)
    def upClick(self):
        self.sel+=1
        if self.sel>=len(self.cards):
            self.sel = self.sel-(self.sel%5)
        if self.sel%5==0:
            self.sel-=5
        if self.active:
            while self.activeCards[self.sel]:
                self.sel+=1
                if self.sel>=len(self.cards):
                    self.sel = 0
    def downClick(self):
        self.sel+=5
        self.sel = self.sel-(self.sel%5)
        if self.sel>=len(self.cards):
            self.sel-=len(self.cards)
        if self.active:
            while self.activeCards[self.sel]:
                self.sel+=1
                if self.sel>=len(self.cards):
                    self.sel = 0
    def drawSelect(self,scr):
        scr.rectangle(1,53,199,96,False)
        scr.rectangle(((self.sel%5)*40),54,((self.sel%5)*40)+40,95,False)


class Player():
    def __init__(self,name,numCards):
        self.name = name
        self.cards = []
        for i in range(numCards):
            self.cards.append(randomCard())

class Main():
    def __init__(self,game,exitGame):
        self.scr = game
        game.downBind[0] = self.button_1
        game.downBind[1] = self.button_2
        game.downBind[2] = self.button_3
        game.downBind[3] = self.button_4
        game.downBind[4] = self.button_5
        
        self.exitGame = exitGame
        self.screen = 4
        
        self.focus = 0
        self.hubIp = ""
        self.info = {}
        self.info["cards"] = 0
        self.info["players"] = 0
        self.info["bots"] = False
        self.info["hub"] = False

        self.game = {}
        self.game["dir"] = -1 #Direction of the game
        self.game["player"] = 0 #Current player
        self.game["players"] = [Player("Testing player",12)]
        self.game["card"] = "0blue"
        self.game["color"] = "blue"
        self.game["stack"] = 0
        self.widg = []
        
        self.widg.append(Slider("Players",10,3,2,12))
        self.widg.append(Slider("Cards per player",10,34,3,24))
        self.widg.append(CheckButton("Play againsed bots",10,64))
        self.widg.append(CheckButton("Connect to hub",10,80))
        self.widg.append(Button("Next",160,80,self.setupNext))
        self.loadGame()
        self.render()
        game.update()
    def setupNext(self): #Next button on the setup screen was pressed
        self.info["players"] = self.widg[0].value
        self.info["cards"] = self.widg[1].value
        self.info["bots"] = self.widg[2].value == True
        self.info["hub"] = self.widg[3].value == True
        self.game["players"] = []
        self.game["player"] = 0
        self.game["dir"] = 0
        for pl in range(self.info["players"]):
            self.game["players"].append(Player("Player: "+str(pl),self.info["cards"]))
        loadNext()
        self.render()
    
    #Main game playing/card selecting area
    def loadGame(self):
        self.widg = []
        self.widg.append(Button("Players ",3,3))
        self.widg.append(Button("Say UNO ",3,19))
        self.widg.append(Button("End turn",3,36))
        self.widg.append(CardList(self.game["players"][self.game["player"]].cards,True))
    
    
    #Player switch screen
    def loadNext(self):
        self.widg = []
        self.widg.append(Text(self.game["players"][0].name+" turn",5,5))
        self.focus = 2
        if self.game["dir"]==0:
            self.focus = 1
        elif self.game["dir"]==1:
            self.widg.append(Image("games/UNO images/arrowRight.png",130,15))
        elif self.game["dir"]==-1:
            self.widg.append(Image("games/UNO images/arrowLeft.png",5,15))
        self.widg.append(Button("Take turn",50,80))
    
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
        else:
            self.widg[-1].text = "Invalid IP"
            self.render()
    def loadHubJoin(self):
        self.widg = []
        self.widg.append(Text("Enter IP of hub",2,0))
        self.widg.append(Text("",2,20))
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
        if len(self.widg)!=0:
            self.focus-=1
            if self.focus<0:
                self.focus = 0
            self.render()
    def button_2(self):
        if len(self.widg)!=0:
            self.focus+=1
            if self.focus>=len(self.widg):
                self.focus = len(self.widg)-1
            self.render()
    def button_3(self):
        pass
    def button_4(self):
        if len(self.widg)!=0:
            self.widg[self.focus].downClick()
            self.render()
    def button_5(self):
        if len(self.widg)!=0:
            self.widg[self.focus].upClick()
            self.render()
    def render(self):
        self.scr.clear()
        if self.screen==4: #Main game screen
            self.scr.image(70,0,"games/UNO images/"+self.game["card"]+".png")
            self.scr.text(112,2,"Colour: "+self.game["color"])
            self.scr.text(112,12,"Stack: "+str(self.game["stack"]))
            typ = "NONE"
            crd = self.game["card"]
            if crd[0].isnumeric():
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
            self.scr.text(112,22,"Type: "+typ)
            self.scr.text(112,32,"Select: "+str(self.widg[-1].sel+1)+"/"+str(len(self.widg[-1].cards)))
        self.drawWidgets()
        self.scr.update()
    def drawWidgets(self): #Draws all the widgets
        for i,a in enumerate(self.widg):
            if i==self.focus:
                a.drawSelect(self.scr)
            a.draw(self.scr)
    def loop(self):
        pass
