class grid():
    
    def __init__(self,l,w,res):
        self.l = l
        self.w = w
        self.res = res
        
    def show(self):
        stroke(15)
        i = self.res
        while(i<self.l):
            line(i,0,i,self.w)
            i+=self.res
        j = self.res
        while(j<self.w):
            line(0,j,self.l,j)
            j+=self.res
