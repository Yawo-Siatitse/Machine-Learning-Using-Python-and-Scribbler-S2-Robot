'''
The code that runs the first robot starts form here.
'''


from Myro import *
init('COM4')
setForwardness("fluke-forward")
setIRPower(135)
TurnList = []

def CallerMSolver1():
    while True:
        print(getMicrophone())
        if getMicrophone()>500000:
            Robot1_Solving()
        else:
            continue

#BEGIN: Obstacle Avoider
def Robot1_Solving():
    global a
    a = 6400
    global TurnList
    while True: 
        left = getObstacle(0)
        center = getObstacle(1)
        right = getObstacle(2)
        print(getObstacle())
        if (left < a and center < a and right < a):
            translate(1)
            
            TurnList.append('forward')
        else:
            
            turnLeft(0.5,1.3)
            TurnList.append('left')
            continue
#END: Obstacle Avoider


#BEGIN: Map Correction Code
def MapCorrector():
    global TurnList
    x=0
    while x < len(TurnList)-1:
        if ( TurnList[x] == 'forward' and TurnList[x] == TurnList[x+1]):
            TurnList.pop(x)
        else:
            x+=1
    print(TurnList)
    i=0
    while i < len(TurnList)-4:
        if (TurnList[i] == 'left' and TurnList[i+1] == 'forward' and TurnList[i+2] == 'left' and TurnList[i+3] == 'left'):
            TurnList.insert(i,"right")
            del TurnList[i+1:i+6]
        else:
            i+=1
    print(TurnList)
    t=0  
    while t < len(TurnList):
        if (TurnList[t] == 'forward'):
            TurnList.pop(t)
        else:
            t+=1
    print(TurnList)
#END: Map Correction Code
       

#BEGIN: Transmission code
def Map_Transmission():
    global TurnList
    x=0
    
    while x < (len(TurnList)):
        if TurnList[x]=="left":
            if x == 0:
                backward(1,0.15)
            elif TurnList[x - 1] == "left":
                pass
            elif TurnList[x-1]=="right":
                backward(1,0.3)
        elif TurnList[x] == "right":
            if x==0:
                forward(1,0.15)
            elif TurnList[x - 1] == "left":
                forward(1,0.3)
            elif TurnList[x-1]=="right":
                pass
        x+=1
        wait(1)
    setVolume('on')
    setS2Volume(100)
    beep(0.1,850)        
    print("Transmission done...")
#END: Transmission code

'''
The code that runs the first robot ends here.
'''



'''
The code that runs the second robot starts form here.
'''

from Myro import *
init('COM3')

setForwardness("fluke-forward")
setIRPower(135)

def CallerReciever():
    while True:
        print(getMicrophone())
        if getMicrophone()>500000:
            ReceiveInst()
        else:
            continue

def CallerMSolver2():
    while True:
        print(getMicrophone())
        if getMicrophone()>500000:
            Robot2_Solving()
        else:
            continue


TurnList2 = []
#BEGIN: Reception code
def ReceiveInst():
    global TurnList2
   
    while True:
        if (getLight(0) < getLight(2)):
            TurnList2 = TurnList2 + ['right']
        elif (getLight(2)< getLight(0)):
            TurnList2 = TurnList2 + ['left']
        print(TurnList2)
        wait(1)
#END: Reception code



#BEGIN: Maze Solving Code 2
 
def Robot2_Solving():
    global TurnList2    
    while len(TurnList2) > 0:
        left = getObstacle(0)
        center = getObstacle(1)
        right = getObstacle(2)
        print(getObstacle())
        a=6400
        if (left < a and center < a and right < a):
            translate(1)
        else:
            if TurnList2[0]=="left":
                turnLeft(0.5,1.3)
                TurnList2.pop(0)
                continue
         
            elif TurnList2[0]=="right":
                turnRight(0.5,1.3)
                TurnList2.pop(0)
                continue
    if len(TurnList2) == 0:
        forward(1,3)
        ScribbySong()
#END: MazeSolving Code 2

#BEGIN: Maze Completion Song
def ScribbySong():
    setVolume("on")

    c = 261.6256
    ch = 277.18
    d = 293.6648
    dh = 311.13
    e = 329.6276
    f = 349.2282
    fh = 369.99
    g = 391.9954
    gh = 415.30
    a = 440
    ah = 466.16
    b = 493.8833

    scorelist = [e,e,f,g,g,f,e,d,c,c,d,e,e,d,d]
    scorelist2 = [e,e,f,g,g,f,e,d,c,c,d,e,d,c,c]
    for i in scorelist:
        rotate(0.5)
        beep(0.5,2.7*i)
        beep(.01,0)
    for x in scorelist2:
        rotate(-0.5)
        beep(0.5,2.7*x)
        beep(.01,0)
    stop()
    setVolume("off")
#END: Maze Completion Song

'''
The code that runs the second robot ends here.
'''
