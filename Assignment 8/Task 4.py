#!/usr/bin/env python3
# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def move(state, direction):
    try:
        for line in state:
            if not len(line) >= 1 or not len(line) == len(state[0]) or not checkchr(line) or not playernum(state):
                raise Warning("Invalid State")
    except:
        raise Warning("Big Chungus")
    posmoves = iliketomoveitmoveit(state)
    if direction not in posmoves:
        raise Warning("wrong move, buddy")
    nstate = newworldthegame(state, direction)
    nposmoves = iliketomoveitmoveit(nstate)
    return nstate, nposmoves

def findpos(state):
    y = 0
    for line in state:
        y += 1                 # y (line)starts with one
        if "o" in line:
            x = line.find("o") # x (index)starts with zero
            break
    return(x, y)

def newworldthegame(state, direction):
    x, y = findpos(state)
    i = 0
    nstate = []
    for line in state:
        if "o" in line:
            nstate.append(line.replace("o"," "))
        else:
            nstate.append(line)
    
    if direction == "down":
        nstate[y] = nstate[y][:x] + "o" + nstate[y][x+1:]
    if direction == "right":
        nstate[y-1] = nstate[y-1][:x+1] + "o" + nstate[y-1][x+2:]
    if direction == "left":
        nstate[y-1] = nstate[y-1][:x-1] + "o" + nstate[y-1][x:]
    if direction == "up":
        nstate[y-2] = nstate[y-2][:x] + "o" + nstate[y][x+1:]
    
    return tuple(nstate)




def iliketomoveitmoveit(state):
    ty = len(state)
    tx = len(state[0])
    posmoves = []
    x, y = findpos(state)
                      
    #print(x, y, tx, ty)
    if ty - y > 0 and state[y][x] != "#":
        posmoves.append("down")
    if x > 0 and state[y-1][x-1] != "#":
        posmoves.append("left")
    if tx > x and state[y-1][x+1] != "#":
        posmoves.append("right")
    if y - 1 > 0 and state[y-2][x] != "#":
        posmoves.append("up")
    if len(posmoves) == 0:
        raise Warning("brazil")
    return tuple(posmoves)


def checkchr(line):
    allowedchr = set(" #o")
    return set(line) <= allowedchr

def playernum(state):
    o = 0
    for line in state:
        if "o" in line:
            o += 1
    return 2 > o

# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "       #"
)
s2 = move(s1, "up")

print("= New State =")
print("\n".join(s2[0]))
print(f"\nPossible Moves: {s2[1]}")
