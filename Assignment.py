def main():
    #***Gets the upper-right Co-ordinates of the plateau
    upperRightCoordinates=input().split()
    upperRightX=int(upperRightCoordinates[0])
    upperRightY=int(upperRightCoordinates[1])

    #***Gets the Co-ordinates and the Movements of the first rover
    roverOneCoordinates=input().split()
    roverOneMovement=input()
    roverOneX=int(roverOneCoordinates[0])
    roverOneY=int(roverOneCoordinates[1])
    roverOneDir=roverOneCoordinates[2]
    

    #Gets the Co-ordinates and the Movements of the second rover
    roverTwoCoordinates=input().split()
    roverTwoMovement=input()
    roverTwoX=int(roverTwoCoordinates[0])
    roverTwoY=int(roverTwoCoordinates[1])
    roverTwoDir=roverTwoCoordinates[2]

    #***Function for the rover one starts here***
    def roverOne():
        global roverOneX
        global roverOneY
        global roverOneDir
        roverOneX=int(roverOneCoordinates[0])
        roverOneY=int(roverOneCoordinates[1])
        roverOneDir=roverOneCoordinates[2]
        for dir in roverOneMovement:
            
            #*** code for movement of the rover starts herer***
            if dir == "M" and roverOneDir=='N':
                roverOneY=roverOneY+1
            elif dir== "M" and roverOneDir=='W':
                roverOneX=roverOneX-1
            elif dir== "M" and roverOneDir=='E':
                roverOneX=roverOneX+1
            elif dir== "M" and roverOneDir=='S':
                roverOneY=roverOneY-1
            #***code for movement of the rover ends here***
            
            #***code for the direction of the rover starts here***
            elif dir=="L" and roverOneDir=='N':
                roverOneDir='W'
            elif dir=="R" and roverOneDir=='N':
                roverOneDir='E'
            elif dir=="L" and roverOneDir=='W':
                roverOneDir='S'
            elif dir=="R" and roverOneDir=='W':
                roverOneDir='N'
            elif dir=="L" and roverOneDir=='E':
                roverOneDir='N'
            elif dir=="R" and roverOneDir=='E':
                roverOneDir='S'
            elif dir=="L" and roverOneDir=='S':
                roverOneDir='E'
            elif dir=="R" and roverOneDir=='S':
                roverOneDir='W'
             #***code for the direction of the rover ends here***

        if (0 <= roverOneX <= upperRightX) and (0 <= roverOneY <= upperRightY):
            print(roverOneX, roverOneY, roverOneDir)
        else:
            print("Rover One is going out of bounds")
        #***Function for the rover one ends here***
    
    def roverTwo():
        global roverTwoX
        global roverTwoY
        global roverTwoDir
        roverTwoX=int(roverTwoCoordinates[0])
        roverTwoY=int(roverTwoCoordinates[1])
        roverTwoDir=roverTwoCoordinates[2]
        
        for dir in roverTwoMovement:
            
            #*** code for movement of the rover starts herer***
            if dir == "M" and roverTwoDir=='N':
                roverTwoY=roverTwoY+1
            elif dir== "M" and roverTwoDir=='W':
                roverTwoX=roverTwoX-1
            elif dir== "M" and roverTwoDir=='E':
                roverTwoX=roverTwoX+1
            elif dir== "M" and roverTwoDir=='S':
                roverTwoY=roverTwoY-1
            #***code for movement of the rover ends here***
            
            #***code for the direction of the rover starts here***
            elif dir=="L" and roverTwoDir=='N':
                roverTwoDir='W'
            elif dir=="R" and roverTwoDir=='N':
                roverTwoDir='E'
            elif dir=="L" and roverTwoDir=='W':
                roverTwoDir='S'
            elif dir=="R" and roverTwoDir=='W':
                roverTwoDir='N'
            elif dir=="L" and roverTwoDir=='E':
                roverTwoDir='N'
            elif dir=="R" and roverTwoDir=='E':
                roverTwoDir='S'
            elif dir=="L" and roverTwoDir=='S':
                roverTwoDir='E'
            elif dir=="R" and roverTwoDir=='S':
                roverTwoDir='W'
            #***code for the direction of the rover ends here***
        
        if  (0 <= roverTwoX <= upperRightX) and (0 <= roverTwoY <= upperRightY):
            print(roverTwoX, roverTwoY, roverTwoDir)
        else:
            print("Rover Two is going out of bounds")
    #***Function for the rover two ends here***
    
    if (0 <= roverOneX <= upperRightX) and (0 <= roverOneY <= upperRightY):
        roverOne()
    else:
        print("Rover One is out of bounds")

    if (0 <= roverTwoX <= upperRightX) and (0 <= roverTwoY <= upperRightY):
        roverTwo()
    else:
        print("Rover Two is out of bounds")
    
main()
    