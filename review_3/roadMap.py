from chunks import chunk
from chunks import createChunk

class roadMap():
    
    def __init__(self):
        self.chunkSide = 140
        self.chunks = [
                       createChunk(70, 70, self.chunkSide, "DR","none"),
                       createChunk(210, 70, self.chunkSide, "LR","none"),
                       createChunk(350, 70, self.chunkSide, "LR","none"),
                       createChunk(490, 70, self.chunkSide, "LR","none"),
                       createChunk(630, 70, self.chunkSide, "LR","none"),
                       createChunk(770, 70, self.chunkSide, "LR","none"),
                       createChunk(910, 70, self.chunkSide, "LR","none"),
                       createChunk(1050, 70, self.chunkSide, "DL","none"),
                       createChunk(1050, 210, self.chunkSide, "UD","none"),
                       createChunk(1050, 490, self.chunkSide, "UD","none"),
                       createChunk(1050, 630, self.chunkSide, "UL","none"),
                       createChunk(210, 630, self.chunkSide, "LR","none"),
                       createChunk(350, 630, self.chunkSide, "LR","none"),
                       createChunk(490, 630, self.chunkSide, "LR","none"),
                       createChunk(630, 630, self.chunkSide, "LR","none"),
                       createChunk(770, 630, self.chunkSide, "LR","none"),
                       createChunk(910, 630, self.chunkSide, "LR","none"),
                       createChunk(1050, 350, self.chunkSide, "UD","none"),
                       createChunk(70, 630, self.chunkSide, "UR","none"),
                       createChunk(70, 210, self.chunkSide, "UD","none"),
                       createChunk(70, 350, self.chunkSide, "UD","none"),
                       createChunk(70, 490, self.chunkSide, "UD","none"),
                       createChunk(70, 630, self.chunkSide, "UR","none")
                       ]
        
    def show(self):
        for each_chunk in self.chunks:
            each_chunk.show()
