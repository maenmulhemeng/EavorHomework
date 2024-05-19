# In this file we build our state machine. This machine can answer our question about what we should do to move 
# from state A to state B.
# The transition function: [state1,state2]=>commands and by executing these commands we'll move from state1 to state2
# Each command basically holds two attributes: the name of the command and the action of the command (Callback functions)

# The required actions (Callback functions) to solve the problem

# Move action: it takes the next position and returns it as it is. If we need to modify the meaning of the move action
# we can chagne this specific function.
def move(nextPoition):
    return nextPoition

# This funciton returns the value the represent heading north
def changeDirectionToNorth():
    return 'NORTH'

# This funciton returns the value the represent heading west
def changeDirectionToWest():
    return 'WEST'

# This funciton returns the value the represent heading east
def changeDirectionToEast():
    return 'EAST'

# This funciton returns the value the represent heading south
def changeDirectionToSouth():
    return 'SOUTH'

# This funciton accepts a list as a parameter and reverse it
def reversePriorities(priorities):
    priorities.reverse()
    return priorities

# This funciton toggle the boost value
def toggleBoost(boost):
    return not boost

# This function finds the other teleporters and returns it
def teleport(teleportPosition, teleports):
    for t in teleports:
        if t != teleportPosition:
            return t

# With respect to the prioritized dicrections, this function finds to which direction
# we should look at to escape from blockers like @ or x without boost power
def lookAround(priorities,getNextPistion, position, stateMap, isBoost,visited,L,C ):
    # No direction until we find one
    foundDirection = False
    # Let's check our priorities
    for possibleDirection in priorities:
        # Let's look toward the position of the suggested direction
        positionOfPossibleState = getNextPistion(position,possibleDirection,L,C)
        # And then let's get its state
        possibleState = stateMap[positionOfPossibleState[0]][positionOfPossibleState[1]]
        # if the next state is not a blocker @ and now an x without boost and the next position has not beed visited and we haven't seen
        # a good direction to look at  
        if (not ((possibleState == '#') or (possibleState == 'x' and not isBoost) or (foundDirection) or (positionOfPossibleState in visited))):
            # We'll consider this direction a good potential to look at
            direction = possibleDirection
            # And we'll take its state
            nextPoition = positionOfPossibleState
            # Direction found
            foundDirection = True
            # Let's return them
            return direction, nextPoition,foundDirection
    return '', [], foundDirection

# This action remove change the state into blank
def deleteBlocker(position,stateMap):
    stateMap[position[0]][position[1]] = 'blank'

# Transition Funcion is (state1,state2)=>commands and by executing these commands we'll move from state1 to state2
def transition (currentState, nextState,isBoost):
    # For the special case of facing a blocker x when we have the boost power
    # We'd return the command immediately
    if (nextState == 'x' and isBoost):
        return [commandMove, commandDeleteBlocker]
    # But for the other cases we'll ask the state machine table
    return stateMachine[currentState][nextState]

# Commands
# Each command has a name and an action (callback fundtion)
commandMove = {"name":"move", "action":move}
commandLookAround = {"name":"lookAround", "action":lookAround}
commandImpossible = {"name":"impossible"}
commandDone = {"name":"done"}
commandChangeDirectionToNorth = {"name": "changeDirection", "action":changeDirectionToNorth }
commandChangeDirectionToWest =  {"name": "changeDirection", "action":changeDirectionToWest}
commandChangeDirectionToSouth = {"name": "changeDirection", "action":changeDirectionToSouth}
commandChangeDirectionToEast =  {"name": "changeDirection", "action":changeDirectionToEast}
commandReverse = {"name":"reverse", "action":reversePriorities}
commandBoost = {"name": "boost", "action": toggleBoost}
commandTeleporters = {"name": "teleporters", "action":teleport}
commandLoop = {"name":"loop"}
commandDeleteBlocker = {"name":"deleteBlocker", "action":deleteBlocker}

# The state machine table simplifies how we work with the states (tokens) and 
# what we need to move from a state to another 
# For example: To move from a state 'blank' to state 'N' we'll apply two commands
#              1- Move to the state
#              2- Change direction to north
# Example 2: What we should do if tried to go from state 'N' to '#' is to apply the command Look Around

# Why is it important to consider a state machine table? Now, if you want to add a new state and scale your 
# game with a new feature, you can come here and map your new state with the other states and use the commands
# to tell what the transition from and to this new state needs without changing the code of the function of getInstructions
# For Example: You can add a new state 'NE' that tranfers you a step north then step east by using the available commands 
stateMachine = {
    "blank":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x":[commandLookAround],
        "$":[commandMove],
        "@":[commandMove],
        "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove,commandTeleporters],
    },
    "#":{
        "blank": [commandImpossible],
        "#": [commandImpossible],
        "x": [commandImpossible],
        "$": [commandImpossible],
        "@": [commandImpossible],
        "N": [commandImpossible],
        "W": [commandImpossible],
        "E": [commandImpossible],
        "S": [commandImpossible],
        "I": [commandImpossible],
        "B": [commandImpossible],
        "T": [commandImpossible],
    },
    "x":{
        "blank": [commandMove],
        "#": [commandImpossible],
        "x" : [commandImpossible],
        "$" :  [commandMove],
        "@": [commandMove],
        "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "$":{
        "blank": [commandDone],
        "#": [commandDone],
        "x" :[commandDone],
        "$": [commandDone],
        "@": [commandDone],
        "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "@":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x" : [commandLookAround],
        "$":  [commandMove],
        "@": [commandImpossible],
        "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "N":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x" : [commandLookAround],
        "$":  [commandMove],
        "@": [commandMove],
        "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "W":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x" : [commandLookAround],
        "$":  [commandMove],
        "@": [commandMove],
        "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "E":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x" : [commandLookAround],
        "$":  [commandMove],
        "@": [commandMove],
         "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "S":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x" : [commandLookAround],
        "$":  [commandMove],
        "@": [commandMove],
         "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "I":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x" : [commandLookAround],
        "$":  [commandMove],
        "@": [commandMove],
         "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "B":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x" : [commandLookAround],
        "$":  [commandMove],
        "@": [commandMove],
         "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandMove, commandTeleporters],
    },
    "T":{
        "blank": [commandMove],
        "#": [commandLookAround],
        "x" : [commandLookAround],
        "$":  [commandMove],
        "@": [commandMove],
         "N": [commandMove, commandChangeDirectionToNorth],
        "W": [commandMove, commandChangeDirectionToWest],
        "E": [commandMove, commandChangeDirectionToEast],
        "S": [commandMove, commandChangeDirectionToSouth],
        "I": [commandMove, commandReverse],
        "B": [commandMove, commandBoost],
        "T": [commandLoop]
    }
}