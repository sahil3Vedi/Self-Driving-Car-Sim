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
    
    def getminIndex(self):
        x1 = self.refTes.posX
        y1 = self.refTes.posY
        distances = []
        for each_centre in self.chunkCentres:
            x2 = each_centre[0]
            y2 = each_centre[1]
            distance = dist(x1,y1,x2,y2)
            distances.append(distance)
        min_dist = min(distances)
        min_index = distances.index(min_dist)
        return min_index
        
        
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
        self.minIndex = self.getminIndex()
        self.dispImage = loadImage("../assets/teslaTopView.png")
        
    def update(self):
        self.minIndex = self.getminIndex()
        
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
        image(self.dispImage, 0, 0, 55, 110) #70% reduction in size
        popMatrix()
    
