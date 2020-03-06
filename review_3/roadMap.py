from chunks import chunk
from chunks import createChunk

class roadMap():
    
    def __init__(self):
        self.chunkSide = 140
        self.chunks = [
                       createChunk(70, 70, self.chunkSide, "DR"),
                       createChunk(210, 70, self.chunkSide, "LR"),
                       createChunk(350, 70, self.chunkSide, "DL"),
                       createChunk(70, 210, self.chunkSide, "UD"),
                       createChunk(70, 350, self.chunkSide, "UR"),
                       createChunk(350, 210, self.chunkSide, "UD"),
                       createChunk(210, 350, self.chunkSide, "LR"),
                       createChunk(490, 350, self.chunkSide, "LR"),
                       createChunk(350, 490, self.chunkSide, "UD"),
                       createChunk(630, 350, self.chunkSide, "DL"),
                       createChunk(350, 630, self.chunkSide, "UR"),
                       createChunk(630, 490, self.chunkSide, "UD"),
                       createChunk(490, 630, self.chunkSide, "LR"),
                       createChunk(630, 630, self.chunkSide, "UL"),
                       createChunk(350, 350, self.chunkSide, "Central")
                       ]
        
    def show(self):
        for each_chunk in self.chunks:
            each_chunk.show()
