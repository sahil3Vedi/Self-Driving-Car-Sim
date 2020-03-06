class chunk():
    
    def __init__(self,posX,posY,side,chunk_type):
        self.posX = posX
        self.posY = posY
        self.side = side
        self.chunkType = chunk_type
        
    def show(self):
        rectMode(CENTER)
        fill(100)
        noStroke()
        rect(self.posX, self.posY, self.side, self.side)
        stroke(255) #displaying midlanes on the chunk
        if (self.chunkType=="LR"):
            line(self.posX-(self.side/2),self.posY,self.posX+(self.side/2),self.posY)
        if (self.chunkType=="UD"):
            line(self.posX,self.posY-(self.side/2),self.posX,self.posY+(self.side/2))
        if (self.chunkType=="DL"):
            arc(self.posX-(self.side/2), self.posY+(self.side/2), self.side, self.side, -PI/2, 0)
            noStroke()
            rect(self.posX-3*(self.side/4),self.posY+3*(self.side/4),self.side/2,self.side/2)
            fill(20,200,20)
            rect(self.posX+(self.side/4),self.posY-(self.side/4),self.side/2,self.side/2)
            arc(self.posX-self.side, self.posY+self.side, self.side, self.side, -PI/2, 0)
            fill(100)
            stroke(100)
            arc(self.posX, self.posY, self.side, self.side, -PI/2, 0)
        if (self.chunkType=="UR"):
            arc(self.posX+(self.side/2), self.posY-(self.side/2), self.side, self.side, PI/2, PI)
            noStroke()
            rect(self.posX+3*(self.side/4),self.posY-3*(self.side/4),self.side/2,self.side/2)
            fill(20,200,20)
            rect(self.posX-(self.side/4),self.posY+(self.side/4),self.side/2,self.side/2)
            arc(self.posX+self.side, self.posY-self.side, self.side, self.side, PI/2, PI)
            fill(100)
            stroke(100)
            arc(self.posX, self.posY, self.side, self.side, PI/2, PI)
        if (self.chunkType=="DR"):
            arc(self.posX+(self.side/2), self.posY+(self.side/2), self.side, self.side, -PI, -PI/2)
            noStroke()
            rect(self.posX+3*(self.side/4),self.posY+3*(self.side/4),self.side/2,self.side/2)
            fill(20,200,20)
            rect(self.posX-(self.side/4),self.posY-(self.side/4),self.side/2,self.side/2)
            arc(self.posX+self.side, self.posY+self.side, self.side, self.side, -PI, -PI/2)
            fill(100)
            stroke(15)
            arc(self.posX, self.posY, self.side, self.side, -PI, -PI/2)
        if (self.chunkType=="UL"):
            arc(self.posX-(self.side/2), self.posY-(self.side/2), self.side, self.side, 0, PI/2)
            noStroke()
            rect(self.posX-3*(self.side/4),self.posY-3*(self.side/4),self.side/2,self.side/2)
            fill(20,200,20)
            rect(self.posX+(self.side/4),self.posY+(self.side/4),self.side/2,self.side/2)
            arc(self.posX-self.side, self.posY-self.side, self.side, self.side, 0, PI/2)
            fill(100)
            stroke(100)
            arc(self.posX, self.posY, self.side, self.side, 0, PI/2)
        if (self.chunkType=="Central"):
            #line(self.posX-(self.side/2),self.posY,self.posX+(self.side/2),self.posY)
            #line(self.posX,self.posY-(self.side/2),self.posX,self.posY+(self.side/2))
            #arc(self.posX-3*(self.side/4), self.posY+3*(self.side/4), self.side, self.side, -3*PI/8, -PI/8)
            #arc(self.posX+3*(self.side/4), self.posY-3*(self.side/4), self.side, self.side, 5*PI/8, 7*PI/8)
            #arc(self.posX+3*(self.side/4), self.posY+3*(self.side/4), self.side, self.side, -7*PI/8, -5*PI/8)
            #arc(self.posX-3*(self.side/4), self.posY-3*(self.side/4), self.side, self.side, PI/8, 3*PI/8)
            noStroke()
            rect(self.posX-3*(self.side/4),self.posY-3*(self.side/4),self.side/2,self.side/2)
            rect(self.posX-3*(self.side/4),self.posY+3*(self.side/4),self.side/2,self.side/2)
            rect(self.posX+3*(self.side/4),self.posY-3*(self.side/4),self.side/2,self.side/2)
            rect(self.posX+3*(self.side/4),self.posY+3*(self.side/4),self.side/2,self.side/2)
            fill(20,200,20)
            #rect(self.posX+(self.side/4),self.posY+(self.side/4),self.side/2,self.side/2)
            stroke(100)
            arc(self.posX-self.side, self.posY-self.side, self.side, self.side, 0, PI/2)
            arc(self.posX+self.side, self.posY+self.side, self.side, self.side, -PI, -PI/2)
            arc(self.posX+self.side, self.posY-self.side, self.side, self.side, PI/2, PI)
            arc(self.posX-self.side, self.posY+self.side, self.side, self.side, -PI/2, 0)
            stroke(255)
            line(self.posX-(self.side/4),self.posY-(self.side/2),self.posX+(self.side/4),self.posY-(self.side/2))
            line(self.posX-(self.side/4),self.posY+(self.side/2),self.posX+(self.side/4),self.posY+(self.side/2))
            line(self.posX+(self.side/2),self.posY-(self.side/4),self.posX+(self.side/2),self.posY+(self.side/4))
            line(self.posX-(self.side/2),self.posY-(self.side/4),self.posX-(self.side/2),self.posY+(self.side/4))
            
def createChunk(posX, posY, side, chunk_type):
    newChunk = chunk(posX, posY, side, chunk_type)
    return newChunk
