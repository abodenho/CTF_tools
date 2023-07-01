HORIZONTALDECAL = 2
VERTICALDECAL = 1

class mazeSolver:
    def __init__(self,fileName):
        self.cheminPris = []
        self.isAlreadyFind = False
        self.createMaze(fileName)
        self.solve()

    def solve(self):
        initialPos = (2,1)
        self.cheminPris.append(initialPos)
        self.findPath(self.possiblePos(initialPos),initialPos)


    def createMaze(self,filename):
        file = open(filename, 'r')
        myMaze = []
        for line in file:
            myMaze.append(self.clearLine(line))
        self.maze = myMaze

    @staticmethod
    def clearLine(line):
        return line[:-1]

    def findPath(self,lstChoix,newPos):
        if self.getBlock(newPos[0],newPos[1]) == "F" and not self.isAlreadyFind:
            self.printSolution()
            self.isAlreadyFind = True
        else:
            for choix in lstChoix:
                self.cheminPris.append(choix)
                self.findPath(self.possiblePos(choix),choix)
                try:
                    self.cheminPris.pop()
                except:
                    pass



    def printSolution(self):

        try:
            for i in range(1, len(self.cheminPris)):
                endroitToPrint = self.cheminPris[i]
                lastElem = self.cheminPris[i]
                newPos = self.cheminPris[i +1]
                self.setBlock(endroitToPrint, self.getSymbole(lastElem, newPos))
        except:
            pass

        self.prettyPrint()

    def prettyPrint(self):
        for line in self.maze:
            print(line)

    def getSymbole(self,lastPos,newPos):
        newX = newPos[0]
        newY = newPos[1]
        oldX = lastPos[0]
        oldY = lastPos[1]
        if (newX - oldX) > 0:
            symbole = '>'

        elif (newX - oldX) < 0:
            symbole = '<'

        elif (newY - oldY) > 0:
            symbole = 'v'

        else: #(newY - oldY) < 0
            symbole = "^"

        return symbole

    def setBlock(self,pos,symbole):
        x = pos[0]#TODO check yx
        y = pos[1]
        self.maze[y] =self.maze[y][0:x] + symbole + self.maze[y][x+ 1:]


    def getBlock(self,x,y):
        return self.maze[y][x] #TODO check yx


    def possiblePos(self, pos):
        lstPos = []
        actualPosX = pos[0]
        actualPosY = pos[1]
        down = (actualPosX, actualPosY + VERTICALDECAL)
        left = (actualPosX + HORIZONTALDECAL, actualPosY)
        up = (actualPosX, actualPosY - VERTICALDECAL)
        right = (actualPosX - HORIZONTALDECAL, actualPosY)
        if (self.isFreeToPass((actualPosX, actualPosY), "d") and not down in self.cheminPris):
            lstPos.append(down)

        if (self.isFreeToPass((actualPosX, actualPosY), "l") and not left in self.cheminPris):
            lstPos.append(left)

        if (self.isFreeToPass((actualPosX, actualPosY), "u") and not up in self.cheminPris):
            lstPos.append(up)

        if (self.isFreeToPass((actualPosX, actualPosY), "r") and not right in self.cheminPris):
            lstPos.append(right)

        return lstPos


    def isFreeToPass(self, actualPos,direction):
        value = False
        x = actualPos[0]
        y = actualPos[1]

        if direction == "u":
            if (self.testZone(x,y-1)):
                value = True

        elif direction == "d":
            if (self.testZone(x, y+1)):
                value = True
        elif direction == "l":
            if (self.testZone(x+2, y)):
                value = True
        else: #r
            if (self.testZone(x-2, y)):
                value = True

        return value

    def testZone(self,x,y):
        bloc = self.getBlock(x,y)
        if (bloc == " " or bloc == "F" ):
            return True
        return False

mazeSolver("maze.txt")
