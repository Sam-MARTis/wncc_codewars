panav
SATURDAY
How did the competition go?
03:06
Panav ya' been?
How did the competition go?
4/10
18:57
Our thing barely flew
18:57
It glided at max
18:57
But I had so much fun
18:57
And we're planning to build so many more
18:57
We have the design of the next one in production already
18:58
Hey has the link of the code wars thing come out
21:38
Could you send it please
21:38
You
But I had so much fun
That’s what matters afterall
23:10
You
We have the design of the next one in production already
Amazing
23:10
YESTERDAY
You
Hey has the link of the code wars thing come out
I have no idea what’s on about that
01:32
Are you back?
11:14
Yup
13:54
Came back at 9 am
13:55
Ooo nice
14:38
You
Hey has the link of the code wars thing come out
did you get all the resources?
17:51
Yup
18:02
TODAY
import random
import math

name = "scriptblue"


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

dir = [1 for i in range(40)]


def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]
    current = pirate.investigate_current()[0]

    # print(type(pirate.getID()))
    id = 0
    try:
        # print(type(int(pirate.getID())))
        id = int(pirate.getID())
    except:
        id = 0
    
    
    

    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()

    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(s)


    if id > 0 and id <= 40:
        x, y = pirate.getPosition()
        print(id, x, y)
        if y==39:
            dir[id-1] = 1
            return moveTo(id, 0, pirate)
        elif y==0:
            dir[id-1] = 3
            return moveTo(id, 39, pirate)
        else:
            if dir[id-1] == 3:
                return moveTo(id, 39, pirate)
            elif dir[id-1] == 1:
                return moveTo(id, 0, pirate)
    
    elif pirate.getTeamSignal() != "" and id!=0 and id%4==0:
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
    
        return moveTo(x, y, pirate)

    else:
        return random.randint(1, 4)

        
    


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    # for i in range(0, team.getTotalPirates()):


    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
17:16


