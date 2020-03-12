from phaneron import phaneron

class lidar():
    
    def findLineVal(self,x1,y1,x2,y2,x,y):
        returnVal = -1
        tempVal = (y-y1)*(x1-x2)+(x-x1)*(y2-y1)
        if tempVal>0:
            returnVal = 1
        return returnVal
        
    
    def findSubVal(self, xd,yd, phaneron, i):
        returnSub = 1
        subCenter = phaneron.nearestChunkCentres[i]
        subType = phaneron.nearestChunkTypes[i]
        subOmits = phaneron.nearestChunkOmits[i]
        xt = self.refTes.posX
        xf = xt + xd
        yt = self.refTes.posY
        yf = yt + yd
        xc = subCenter[0]
        yc = subCenter[1]
        if (subType == "UD"):
            side = phaneron.side
            x1  = xc
            x2 = xc
            y1 = yc - side/2
            y2 = yc + side/2
            tesVal = self.findLineVal(x1,y1,x2,y2,xt,yt)
            dotVal = self.findLineVal(x1,y1,x2,y2,xf,yf)
            if((tesVal!=dotVal)):
                returnSub = 0
        if (subType == "LR"):
            side = phaneron.side
            x1  = xc - side/2
            x2 = xc + side/2
            y1 = yc - side/2
            y2 = yc + side/2
            tesValMid = self.findLineVal(x1,yc,x2,yc,xt,yt)
            dotValMid = self.findLineVal(x1,yc,x2,yc,xf,yf)
            tesValLeft = self.findLineVal(x1,y1,x2,y1,xt,yt)
            dotValLeft = self.findLineVal(x1,y1,x2,y1,xf,yf)
            if((tesValMid!=dotValMid) or (tesValLeft!=dotValLeft)):
                returnSub = 0
        return returnSub
    
    def checkVal(self,xd, yd, phaneron):
        returnVal = 1
        for i in range(phaneron.nearestChunks):
            phanVal = self.findSubVal(xd, yd, phaneron, i)
            if (phanVal == 0):
                returnVal = 0
        return returnVal
    
    def getDots(self, phaneron):
        dots = []
        angle = self.refTes.angle
        for spokes in range(self.count):
            spokeDots = []
            for dotIndex in range(self.limiting):
                r = dotIndex*self.spread 
                xd = -r*sin(angle)
                yd = r*cos(angle)
                dotVal = self.checkVal(xd,yd,phaneron)
                spokeDots.append(dotVal)
            angle = angle + self.rotation
            dots.append(spokeDots)
        return dots
    
    def __init__(self, phaneron, refTes, count, spread, limiting):
        self.refTes = refTes
        self.phaneron = phaneron
        self.posX = self.phaneron.posX + self.phaneron.side/2
        self.posY = self.phaneron.posY + self.phaneron.side/2
        self.count = count
        self.spread = spread
        self.limiting = limiting
        self.rotation = 2*PI/self.count
        self.dotMatrix = self.getDots(self.phaneron)
    
    def update(self):
        self.dotMatrix = self.getDots(self.phaneron)
        
    def show(self):
        translate(self.posX, self.posY)
        pushMatrix()
        for spokes in range(self.count):
            for dots in range(self.limiting):
                if(self.dotMatrix[spokes][dots] == 1):
                    stroke(250)
                else:
                    stroke(200,0,0)
                ellipse(0,self.spread*dots,1,1)
            rotate(self.rotation)
        popMatrix()
        
        
