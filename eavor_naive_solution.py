from state_machine import transition


# Given the current position and the direction, this function return the next
# position with respect to the matrix boundaries 
def getNextPistion(position,direction,L,C):
    i = position[0]
    j = position[1]

    # heading south means moving down on rows
    if direction == 'SOUTH':
        return [i + 1, j] if i < L -1 else [i,j]
    # heading east means moving right on columns
    elif direction == 'EAST':
        return [i, j + 1] if j < C -1 else [i,j]
    # heading north means moving up on rows
    elif direction == 'NORTH':
        return [i - 1, j] if i > 0 else [i,j]
    # heading west means moving left on columns
    elif direction == 'WEST':
        return [i, j - 1] if j > 0 else [i,j]
    
def getInstructions(stateMap,L,C,priorities,isBoost,position,teleports,direction = 'SOUTH',):
    # we'll save the solution here e.g ['SOUTH', 'EAST', 'NORTH', 'EAST', 'EAST']
    instructions = [] 

    # We'll track the positions that we have visited e.g [[1,1], [1,2]] 
    # it means we have visited position [1,1] and then [1,2]
    visited = [] 

    # Let's keep moving while we haven't reached $ yet and we are not stacking in a loop
    # We'll consider revisiting the same position twice is a problem and it leads us to loop
    while(stateMap[position[0]][position[1]] != '$' and position not in visited):

        # Givem the current position and the direction we can know the what the next position is
        nextPoition = getNextPistion(position, direction, L,C)
        
        # Let's ask our state machine a simple quesiton
        # What should we do if we want to move from current state to the next state of the next position with respect to the boos value
        commands = transition(stateMap[position[0]][position[1]], stateMap[nextPoition[0]][nextPoition[1]],isBoost)

        # The answer is a list of commands
        for command in commands:
            match command["name"]:
                case 'move':
                    # Consider the current position is visited
                    visited.append(position)
                    # Add the direction (instuction) to the solution
                    instructions.append(direction)
                    #execute the command action (callback function)
                    position = command['action'](nextPoition)
                case 'deleteBlocker':
                    command['action'](nextPoition,stateMap)
                case 'teleporters':
                    # Consider the current position is visited
                    visited.append(position)
                    # Add the direction (instuction) to the solution
                    instructions.append(direction) 
                    #execute the command action (callback function)
                    position = command["action"](position, teleports)
                case 'changeDirection':
                    #execute the command action (callback function)
                    direction = command["action"]()
                case 'reverse':
                    #execute the command action (callback function)
                    priorities = command["action"](priorities)
                case 'boost':
                    #execute the command action (callback function)
                    isBoost = command["action"](isBoost)
                case 'impossible':
                    break
                case 'lookAround':
                    #execute the command action
                    direction, nextPoition,stop = command["action"](priorities,getNextPistion, position, stateMap, isBoost,visited,L,C)
                    # if we could not find a position to go to after looking around
                    # We'll consider ourselves stacking in a loop
                    if (not stop):
                        return ['LOOP']
    return instructions

# This funciton reads the user input
# For Example: The program is expecting an input of this shape
# 
# 5 6
# # # # # #
# @ E I $ #
# I N     #
# x       #
# # # # # #

# The function returns 
# L = 5
# C = 6
# stateMape : matrix represts the roads
# position = [1,1] The poistion of token @
# teleporters : a pair of teleporter poistions or an empty list
def readUserInput():
    # reading the first line L,C as integers
    L,C = map(int,input().split())
    stateMap = []
    teleports = []
   
    # Loop over the next L lines
    for i in range(L):
        # read the line
        inputRow = input()
        # start with an empty row
        row = []
        # track the actual column index after removing the white spaces
        counter = -1
        # loop over the row itself (the columns)
        for j in range(len(inputRow)):
            # Note: There is two types of spaces here, the token seperators and the space tokens
            #       We'll remove the token seperators and keep space tokens 
            #       space tokens have even indecies
            if (j % 2 == 0):
                # Since, we can't use white space as a value to access a dictionary
                # We'll convert the space token into the word 'blank' to use it 
                # in our state machine (dictionatry) later
                row.append(inputRow[j] if inputRow[j] != " " else "blank")

                # track the actual column index after removing the white spaces
                counter  = counter + 1
                
                # If we found the initial position @ we'd save its position
                if (inputRow[j] == '@'):
                    position = [i,counter]
                
                # If we found teleporter T, we'd save its position as well
                elif (inputRow[j] == 'T'):
                   teleports.append([i,counter])
        
        # Add the row to the matrix
        stateMap.append(row)

    return L, C, stateMap, position,teleports

# Starting Point
if __name__ == "__main__":
    # Let's read the user inputs
    L, C, stateMap, position,teleports = readUserInput()

    # For sake of discussion, let's check if the user did not insert the right number of teleporter
    # Note: This should not happen because it a problem constraint
    if (len(teleports) != 2 and len(teleports) != 0):
        print("Constraint 1: There should be two teleporters. ", len(teleports), " teleporters found")
    
    # A list of prioritized directions
    priorities = ['SOUTH','EAST','NORTH','WEST']

    # At the beginning there is no boost
    isBoost = False
    # As stated in the document, the inital direction is south
    direction = 'SOUTH'
    # Let's find out the instuctions (directions) to the cheese
    instructions = getInstructions(stateMap,L,C,priorities,isBoost,position,teleports,direction)
    # Let's pring the solution
    for i in instructions:
        print(i)
    
        