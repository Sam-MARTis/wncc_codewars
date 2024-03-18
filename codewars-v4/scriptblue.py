import random
import math
# import threading

name = "scriptblue"
units = 10
islands = ["island1", "island2", "island3"]
game_clock = 0

def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1


def ActPirate(pirate):
    try:
        if pirate.randX == None:
            pirate.randX = 40//units * random.randint(0,units-1)
    except:
        pirate.randX = 40//units * random.randint(0,units-1)
    try:
        if pirate.randY == None:
            pirate.randY = 40//units * random.randint(0,units-1)
    except:
        pirate.randY = 40//units * random.randint(0,units-1)
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    try:
        if pirate.obey==0:
            return
    except:
        pirate.obey=1
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        # s = up[-1] + str(x) + "," + str(y - 1)
        # pirate.setTeamSignal(s)
        pirate.obey=0
        return moveTo(x, y-1, pirate)
        

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        # s = down[-1] + str(x) + "," + str(y + 1)
        # # pirate.setTeamSignal(s)
        # return moveTo
        pirate.obey=0
        return moveTo(x, y+1, pirate)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        # s = left[-1] + str(x - 1) + "," + str(y)
        # pirate.setTeamSignal(s)
        pirate.obey=0
        return moveTo(x-1, y, pirate)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        # s = right[-1] + str(x + 1) + "," + str(y)
        # pirate.setTeamSignal(s)
        pirate.obey=0
        return moveTo(x+1, y, pirate)
    pirate.obey=1
    global game_clock
    if game_clock%50 ==0:
        pirate.randX = 40//units * random.randint(0,units-1)
        pirate.randY = 40//units * random.randint(0,units-1)
    
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
    
        # return moveTo(x, y, pirate)
        return moveTo(pirate.randX + random.randint(0,4), pirate.randY+ random.randint(0,4), pirate)

    else:
        # return random.randint(1, 4)
        return moveTo(pirate.randX + random.randint(0,4), pirate.randY+ random.randint(0,4), pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    global game_clock

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    
    # print(f"Team signal is: {team.getTeamSignal()}\n")
    # print(f"Track players: {team.trackPlayers()}\n")
    game_clock+=1
    if game_clock%50==0:
        print("Changing team signal")
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
