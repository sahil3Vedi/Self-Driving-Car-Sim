from roadMap import roadMap

def chunkCentres(roadMap):
    centres = []
    types = []
    for each_chunk in roadMap.chunks:
        vect = [each_chunk.posX, each_chunk.posY]
        centres.append(vect)
        types.append(each_chunk.chunkType)
    return [centres, types]

class phaneron():
    
    def getminIndices(self):
        x1 = self.refTes.posX
        y1 = self.refTes.posY
        distances = []
        for each_centre in self.chunkCentres:
            x2 = each_centre[0]
            y2 = each_centre[1]
            distance = dist(x1,y1,x2,y2)
            distances.append(distance)
        s = set(distances)
        min1 = sorted(s)[0]
        min2 = sorted(s)[1]
        min3 = sorted(s)[2]
        min4 = sorted(s)[3]
        min_index1 = distances.index(min1)
        min_index2 = distances.index(min2)
        min_index3 = distances.index(min3)
        min_index4 = distances.index(min4)
        return [min_index1,min_index2,min_index3,min_index4]
        
        
    def __init__(self, roadMap, refTes):
        self.posX = 490
        self.posY = 0
        self.subsize = 70
        self.subcount = 3
        self.side = self.subsize*self.subcount
        self.chunkSide = 140
        temp = chunkCentres(roadMap)
        self.chunkCentres = temp[0]
        self.chunkTypes = temp[1]
        self.refTes = refTes
        self.minIndices = self.getminIndices()
        self.dispImage = loadImage("../assets/teslaTopView.png")
        self.chunkType = "generic"
        self.chunkCentre = [0,0]
        self.nearestChunkTypes = [self.chunkTypes[q] for q in self.minIndices]
        self.nearestChunkCentres = [self.chunkCentres[r] for r in self.minIndices]
        
    def dispPhaneron(self,chunkCentre,chunkType):
        X = chunkCentre[0]
        Y = chunkCentre[1]
        pushMatrix()
        if (chunkType == "UD"):
            #printing chunk boundary on to the phaneron
            noFill()
            stroke(255,240,0)
            gap = [X-self.refTes.posX,Y-self.refTes.posY]
            rotate(-self.refTes.angle)
            translate(gap[0],gap[1])
            #rect(0,0,self.chunkSide, self.chunkSide)
            line(0,-self.chunkSide/2,0, self.chunkSide/2)
            line(-self.chunkSide/2,-self.chunkSide/2,-self.chunkSide/2, self.chunkSide/2)
            line(self.chunkSide/2,-self.chunkSide/2,self.chunkSide/2, self.chunkSide/2)
        elif (chunkType == "LR"):
            #printing chunk boundary on to the phaneron
            noFill()
            stroke(255,240,0)
            gap = [X-self.refTes.posX,Y-self.refTes.posY]
            rotate(-self.refTes.angle)
            translate(gap[0],gap[1])
            #rect(0,0,self.chunkSide, self.chunkSide)
            line(-self.chunkSide/2,0, self.chunkSide/2,0)
            line(-self.chunkSide/2,-self.chunkSide/2, self.chunkSide/2,-self.chunkSide/2)
            line(-self.chunkSide/2,self.chunkSide/2, self.chunkSide/2,self.chunkSide/2)
        if (chunkType == "DL"):
            #printing chunk boundary on to the phaneron
            noFill()
            stroke(255,240,0)
            gap = [X-self.refTes.posX,Y-self.refTes.posY]
            rotate(-self.refTes.angle)
            translate(gap[0],gap[1])
            #rect(0,0,self.chunkSide, self.chunkSide)
            arc(-self.chunkSide/2, self.chunkSide/2, self.chunkSide, self.chunkSide, -PI/2, 0)
            arc(0, 0, self.chunkSide, self.chunkSide, -PI/2, 0)
            arc(-self.chunkSide,self.chunkSide, self.chunkSide, self.chunkSide, -PI/2, 0)
            line(self.chunkSide/2,self.chunkSide/2, self.chunkSide/2,0)
            line(-self.chunkSide/2,-self.chunkSide/2, 0,-self.chunkSide/2)
        if (chunkType == "UR"):
            #printing chunk boundary on to the phaneron
            noFill()
            stroke(255,240,0)
            gap = [X-self.refTes.posX,Y-self.refTes.posY]
            rotate(-self.refTes.angle)
            translate(gap[0],gap[1])
            #rect(0,0,self.chunkSide, self.chunkSide)
            arc(self.chunkSide/2, -self.chunkSide/2, self.chunkSide, self.chunkSide, PI/2, PI)
            arc(0, 0, self.chunkSide, self.chunkSide, PI/2, PI)
            arc(self.chunkSide,-self.chunkSide, self.chunkSide, self.chunkSide, PI/2, PI)
            line(-self.chunkSide/2,-self.chunkSide/2, -self.chunkSide/2,0)
            line(0,self.chunkSide/2, self.chunkSide/2,self.chunkSide/2)
        if (chunkType == "DR"):
            #printing chunk boundary on to the phaneron
            noFill()
            stroke(255,240,0)
            gap = [X-self.refTes.posX,Y-self.refTes.posY]
            rotate(-self.refTes.angle)
            translate(gap[0],gap[1])
            #rect(0,0,self.chunkSide, self.chunkSide)
            arc(self.chunkSide/2, self.chunkSide/2, self.chunkSide, self.chunkSide, -PI, -PI/2)
            arc(0, 0, self.chunkSide, self.chunkSide, -PI, -PI/2)
            arc(self.chunkSide,self.chunkSide, self.chunkSide, self.chunkSide, -PI, -PI/2)
            line(-self.chunkSide/2,self.chunkSide/2, -self.chunkSide/2,0)
            line(0,-self.chunkSide/2, self.chunkSide/2,-self.chunkSide/2)
        if (chunkType == "UL"):
            #printing chunk boundary on to the phaneron
            noFill()
            stroke(255,240,0)
            gap = [X-self.refTes.posX,Y-self.refTes.posY]
            rotate(-self.refTes.angle)
            translate(gap[0],gap[1])
            #rect(0,0,self.chunkSide, self.chunkSide)
            arc(-self.chunkSide/2, -self.chunkSide/2, self.chunkSide, self.chunkSide, 0,PI/2)
            arc(0, 0, self.chunkSide, self.chunkSide, 0, PI/2)
            arc(-self.chunkSide,-self.chunkSide, self.chunkSide, self.chunkSide, 0, PI/2)
            line(-self.chunkSide/2,self.chunkSide/2, 0,self.chunkSide/2)
            line(self.chunkSide/2,-self.chunkSide/2, self.chunkSide/2,0)
        if (chunkType == "Central"):
            #printing chunk boundary on to the phaneron
            noFill()
            stroke(255,240,0)
            gap = [X-self.refTes.posX,Y-self.refTes.posY]
            rotate(-self.refTes.angle)
            translate(gap[0],gap[1])
            #rect(0,0,self.chunkSide, self.chunkSide)
            arc(-self.chunkSide, self.chunkSide, self.chunkSide, self.chunkSide, -PI/2,0)
            arc(self.chunkSide, self.chunkSide, self.chunkSide, self.chunkSide, -PI,-PI/2)
            arc(self.chunkSide, -self.chunkSide, self.chunkSide, self.chunkSide, PI/2,PI)
            arc(-self.chunkSide, -self.chunkSide, self.chunkSide, self.chunkSide, 0,PI/2)
            #arc(0, 0, self.chunkSide, self.chunkSide, 0, PI/2)
            #arc(-self.chunkSide,-self.chunkSide, self.chunkSide, self.chunkSide, 0, PI/2)
        popMatrix()

    def update(self):
        self.minIndices = self.getminIndices()
        self.nearestChunkTypes = [self.chunkTypes[q] for q in self.minIndices]
        self.nearestChunkCentres = [self.chunkCentres[r] for r in self.minIndices]
        
    def show(self):
        rectMode(CORNER)
        fill(25)
        stroke(0)
        rect(self.posX, self.posY, self.side, self.side)
        stroke(255)
        fill(255)
        imageMode(CENTER)
        #text(str(self.minIndex), self.posX + self.side/2, self.posY+ self.side/2)
        pushMatrix()
        translate(self.posX + self.side/2, self.posY + self.side/2)
        rectMode(CENTER)
        image(self.dispImage, 0, 0, 42, 87) #70% reduction in size
        for i in range(4):
            a = self.nearestChunkCentres[i]
            b = self.nearestChunkTypes[i]
            self.dispPhaneron(a,b)
        popMatrix()
            
        
       
            
            
    
