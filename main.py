#This is the file to be executed by the Pi
#Its used as a main menu for the games
import screenTester as scr
import time, os

def addZero(num):
    if num<10:
        return "0"+str(num)
    return str(num)

for i in range(0,30):
    scr.clear()
    scr.image(0,0,"intro/00"+addZero(i+1)+".png")
    scr.update()
    time.sleep(0.05)
time.sleep(0.5)
scr.clear()
scr.text(0,0,"Please select a game to play...")

games = os.listdir("games")
ind = 0
scr.rectangle(6,15,194,30,False)
scr.text(10,15,games[0][:len(games[0])-3])
scr.line(0,75,200,75)
scr.text(15,80,"<")
scr.text(175,80,">")

def nextGame():
    global ind
    ind+=1
    scr.clear()
    if ind>=len(games):
        ind=0
    scr.text(0,0,"Please select a game to play...")
    scr.rectangle(6,15,194,30,False)
    scr.text(10,15,games[ind][:len(games[ind])-3])
    scr.line(0,75,200,75)
    scr.text(15,80,"<")
    scr.text(175,80,">")
    scr.update()
def beforeGame():
    global ind
    ind-=1
    scr.clear()
    if ind<0:
        ind=len(games)-1
    scr.text(0,0,"Please select a game to play...")
    scr.rectangle(6,15,194,30,False)
    scr.text(10,15,games[ind][:len(games[ind])-3])
    scr.line(0,75,200,75)
    scr.text(15,80,"<")
    scr.text(175,80,">")
    scr.update()

scr.downBind[0] = beforeGame
scr.downBind[4] = nextGame

scr.update()
run = True
while run:
    scr.updateLoop()
