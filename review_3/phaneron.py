from roadMap import roadMap

def chunkCentres(roadMap):
    centres = []
    types = []
    omits = []
    for each_chunk in roadMap.chunks:
        vect = [each_chunk.posX, each_chunk.posY]
        centres.append(vect)
        types.append(each_chunk.chunkType)
        omits.append(each_chunk.omit)
    return [centres, types, omits]

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
        final_list = []
        for i in range(self.nearestChunks):
            temp = sorted(s)[i]
            temp1 = distances.index(temp)
            final_list.append(temp1)
        return final_list
        
        
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
        self.chunkOmits = temp[2]
        self.refTes = refTes
        self.nearestChunks = 4
        self.minIndices = self.getminIndices()
        self.dispImage = loadImage("../assets/teslaTopView.png")
        self.chunkType = "generic"
        self.chunkCentre = [0,0]
        self.nearestChunkTypes = [self.chunkTypes[p] for p in self.minIndices]
        self.nearestChunkCentres = [self.chunkCentres[q] for q in self.minIndices]
        self.nearestChunkOmits = [self.chunkOmits[r] for r in self.minIndices]
        
        
    def dispPhaneron(self,chunkCentre,chunkType,chunkOmit):
        X = chunkCentre[0]
        Y = chunkCentre[1]
        pushMatrix()
        #printing chunk boundary on to the phaneron
        noFill()
        stroke(255,240,0)
        gap = [X-self.refTes.posX,Y-self.refTes.posY]
        rotate(-self.refTes.angle)
        translate(gap[0],gap[1])
        #rect(0,0,self.chunkSide, self.chunkSide)
        if (chunkType == "UD"):
            line(0,-self.chunkSide/2,0, self.chunkSide/2)
            if (chunkOmit!="left"):
                line(-self.chunkSide/2,-self.chunkSide/2,-self.chunkSide/2, self.chunkSide/2)
            if (chunkOmit!="right"):
                line(self.chunkSide/2,-self.chunkSide/2,self.chunkSide/2, self.chunkSide/2)
        elif (chunkType == "LR"):
            line(-self.chunkSide/2,0, self.chunkSide/2,0)
            if (chunkOmit!="top"):
                line(-self.chunkSide/2,-self.chunkSide/2, self.chunkSide/2,-self.chunkSide/2)
            if (chunkOmit!="bottom"):
                line(-self.chunkSide/2,self.chunkSide/2, self.chunkSide/2,self.chunkSide/2)
        if (chunkType == "DL"):
            arc(-self.chunkSide/2, self.chunkSide/2, self.chunkSide, self.chunkSide, -PI/2, 0)
            arc(0, 0, self.chunkSide, self.chunkSide, -PI/2, 0)
            arc(-self.chunkSide,self.chunkSide, self.chunkSide, self.chunkSide, -PI/2, 0)
            line(self.chunkSide/2,self.chunkSide/2, self.chunkSide/2,0)
            line(-self.chunkSide/2,-self.chunkSide/2, 0,-self.chunkSide/2)
        if (chunkType == "UR"):
            arc(self.chunkSide/2, -self.chunkSide/2, self.chunkSide, self.chunkSide, PI/2, PI)
            arc(0, 0, self.chunkSide, self.chunkSide, PI/2, PI)
            arc(self.chunkSide,-self.chunkSide, self.chunkSide, self.chunkSide, PI/2, PI)
            line(-self.chunkSide/2,-self.chunkSide/2, -self.chunkSide/2,0)
            line(0,self.chunkSide/2, self.chunkSide/2,self.chunkSide/2)
        if (chunkType == "DR"):
            arc(self.chunkSide/2, self.chunkSide/2, self.chunkSide, self.chunkSide, -PI, -PI/2)
            arc(0, 0, self.chunkSide, self.chunkSide, -PI, -PI/2)
            arc(self.chunkSide,self.chunkSide, self.chunkSide, self.chunkSide, -PI, -PI/2)
            line(-self.chunkSide/2,self.chunkSide/2, -self.chunkSide/2,0)
            line(0,-self.chunkSide/2, self.chunkSide/2,-self.chunkSide/2)
        if (chunkType == "UL"):
            arc(-self.chunkSide/2, -self.chunkSide/2, self.chunkSide, self.chunkSide, 0,PI/2)
            arc(0, 0, self.chunkSide, self.chunkSide, 0, PI/2)
            arc(-self.chunkSide,-self.chunkSide, self.chunkSide, self.chunkSide, 0, PI/2)
            line(-self.chunkSide/2,self.chunkSide/2, 0,self.chunkSide/2)
            line(self.chunkSide/2,-self.chunkSide/2, self.chunkSide/2,0)
        if (chunkType == "Central"):
            arc(-self.chunkSide, self.chunkSide, self.chunkSide, self.chunkSide, -PI/2,0)
            arc(self.chunkSide, self.chunkSide, self.chunkSide, self.chunkSide, -PI,-PI/2)
            arc(self.chunkSide, -self.chunkSide, self.chunkSide, self.chunkSide, PI/2,PI)
            arc(-self.chunkSide, -self.chunkSide, self.chunkSide, self.chunkSide, 0,PI/2)
            #arc(0, 0, self.chunkSide, self.chunkSide, 0, PI/2)
            #arc(-self.chunkSide,-self.chunkSide, self.chunkSide, self.chunkSide, 0, PI/2)
        popMatrix()

    def update(self):
        self.minIndices = self.getminIndices()
        self.nearestChunkTypes = [self.chunkTypes[p] for p in self.minIndices]
        self.nearestChunkCentres = [self.chunkCentres[q] for q in self.minIndices]
        self.nearestChunkOmits = [self.chunkOmits[r] for r in self.minIndices]
        
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
        for i in range(self.nearestChunks):
            a = self.nearestChunkCentres[i]
            b = self.nearestChunkTypes[i]
            c = self.nearestChunkOmits[i]
            self.dispPhaneron(a,b,c)
        popMatrix()
            
        
       
            
            
    
