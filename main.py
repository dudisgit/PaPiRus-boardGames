#This is the file to be executed by the Pi
#Its used as a main menu for the games
#You can either import 'screen' or 'screenTester'
#They have the same functions but one if for testing and the other is to work on the PI
import screen as scr
import time, os
import importlib as lib
import os,sys
cDir = os.getcwd()

def addZero(num):
    if num<10:
        return "0"+str(num)
    return str(num)

for i in range(0,15):
    scr.clear()
    scr.image(0,0,"intro/00"+addZero((i*2)+1)+".png")
    scr.update()
time.sleep(0.5)
scr.clear()
scr.text(0,20,"Please select a game to play...")

games = os.listdir("games")
rem = []
for a in games:
    if a[len(a)-3:]!=".py":
        rem.append(a)
for a in rem:
    games.remove(a)
ind = 0
scr.rectangle(6,35,194,50,False)
scr.text(10,35,games[0][:len(games[0])-3])
scr.image(0,52, "gameIcons/"+games[0][:len(games[0])-3]+".png")
scr.line(0,18,200,18)
scr.text(15,3,"<")
scr.text(175,3,">")
scr.text(90,3,"OK")
scr.text(45,3,"Exit")
scr.text(130,3,"Off")

def nextGame():
    global ind
    ind+=1
    scr.clear()
    if ind>=len(games):
        ind=0
    scr.text(0,20,"Please select a game to play...")
    scr.rectangle(6,35,194,50,False)
    scr.text(10,35,games[ind][:len(games[ind])-3])
    scr.image(0,52, "gameIcons/"+games[ind][:len(games[ind])-3]+".png")
    scr.line(0,18,200,18)
    scr.text(15,3,"<")
    scr.text(175,3,">")
    scr.text(90,3,"OK")
    scr.text(45,3,"Exit")
    scr.text(130,3,"Off")
    scr.update()
def beforeGame():
    global ind
    ind-=1
    scr.clear()
    if ind<0:
        ind=len(games)-1
    scr.text(0,20,"Please select a game to play...")
    scr.rectangle(6,35,194,50,False)
    scr.text(10,35,games[ind][:len(games[ind])-3])
    scr.image(0,52, "gameIcons/"+games[ind][:len(games[ind])-3]+".png")
    scr.line(0,18,200,18)
    scr.text(15,3,"<")
    scr.text(175,3,">")
    scr.text(90,3,"OK")
    scr.text(45,3,"Exit")
    scr.text(130,3,"Off")
    scr.update()
def ExitScript():
    global run,ind
    if ind>=len(games):
        return 0
    scr.clear()
    scr.text(0,20,"Please select a game to play...")
    scr.rectangle(6,35,194,50,False)
    scr.text(10,35,games[ind][:len(games[ind])-3])
    scr.image(0,52, "gameIcons/"+games[ind][:len(games[ind])-3]+".png")
    scr.line(0,18,200,18)
    scr.text(15,3,"No")
    scr.text(170,3,"Yes")
    scr.text(60,3,"Exit script?")
    scr.update()
    while not scr.button(0) and not scr.button(4):
        pass
    if scr.button(4):
        run = False
    else:
        ind+=1
def ShutdownScript():
    global run,ind
    if ind>=len(games):
        return 0
    scr.clear()
    scr.text(0,20,"Please select a game to play...")
    scr.rectangle(6,35,194,50,False)
    scr.text(10,35,games[ind][:len(games[ind])-3])
    scr.image(0,52, "gameIcons/"+games[ind][:len(games[ind])-3]+".png")
    scr.line(0,18,200,18)
    scr.text(15,3,"No")
    scr.text(170,3,"Yes")
    scr.text(70,3,"Shutdown?")
    scr.update()
    while not scr.button(0) and not scr.button(4):
        pass
    if scr.button(4):
        print("Shutdown")
        run = False
    else:
        ind+=1
def enterGame(): #Enter a game
    global inGame,ind,game
    sys.path.insert(0,cDir+"/games")
    libr = lib.import_module(games[ind][:len(games[ind])-3])
    scr.clear()
    scr.update()
    scr.updateFull()
    scr.downBind[0] = scr.nil
    scr.downBind[4] = scr.nil
    scr.downBind[1] = scr.nil
    scr.downBind[3] = scr.nil
    scr.downBind[2] = scr.nil
    game = libr.Main(scr,exitGame)
    inGame = True
def exitGame(): #Called by anouther library to stop playing the game
    global inGame
    inGame = False
    scr.downBind[0] = beforeGame
    scr.downBind[4] = nextGame
    scr.downBind[1] = ExitScript
    scr.downBind[3] = ShutdownScript
    scr.downBind[2] = enterGame
    sys.path.insert(0,cDir)
    scr.clear()
    scr.text(0,20,"Please select a game to play...")
    scr.rectangle(6,35,194,50,False)
    scr.text(10,35,games[ind][:len(games[ind])-3])
    scr.image(0,52, "gameIcons/"+games[ind][:len(games[ind])-3]+".png")
    scr.line(0,18,200,18)
    scr.text(15,3,"<")
    scr.text(175,3,">")
    scr.text(90,3,"OK")
    scr.text(45,3,"Exit")
    scr.text(130,3,"Off")
    scr.update()
    scr.updateFull()


scr.downBind[0] = beforeGame
scr.downBind[4] = nextGame
scr.downBind[1] = ExitScript
scr.downBind[3] = ShutdownScript
scr.downBind[2] = enterGame

inGame = False
game = None

scr.update()
run = True
while run:
    if inGame:
        game.loop()
    scr.updateLoop()

#Tempory
#scr.main.destroy()

