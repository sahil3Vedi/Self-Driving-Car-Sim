from chunks import chunk
from chunks import createChunk

class roadMap():
    
    def __init__(self):
        self.chunkSide = 140
        self.chunks = [
                       createChunk(70, 70, self.chunkSide, "DR","none"),
                       createChunk(210, 70, self.chunkSide, "LR","bottom"),
                       createChunk(350, 70, self.chunkSide, "DL","none"),
                       createChunk(70, 210, self.chunkSide, "UD","right"),
                       createChunk(70, 350, self.chunkSide, "UR","none"),
                       createChunk(350, 210, self.chunkSide, "UD","left"),
                       createChunk(210, 350, self.chunkSide, "LR","top"),
                       createChunk(490, 350, self.chunkSide, "LR","bottom"),
                       createChunk(350, 490, self.chunkSide, "UD","right"),
                       createChunk(630, 350, self.chunkSide, "DL","none"),
                       createChunk(350, 630, self.chunkSide, "UR","none"),
                       createChunk(630, 490, self.chunkSide, "UD","left"),
                       createChunk(490, 630, self.chunkSide, "LR","top"),
                       createChunk(630, 630, self.chunkSide, "UL","none"),
                       createChunk(350, 350, self.chunkSide, "Central","none")
                       ]
        
    def show(self):
        for each_chunk in self.chunks:
            each_chunk.show()
