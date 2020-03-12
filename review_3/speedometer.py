class speedometer():
    
    def __init__(self):
        self.posX = 1120
        self.posY = 490
        self.steeringTilt = 0
        #self.keyLogger = keyLogger()
        self.dispImage = loadImage("../assets/steering_wheel.png")
        self.font = createFont("../assets/digital-7.ttf",32);
                
    def show(self, distance, speed):
        self.speed = speed
        self.distance = distance
        fill(50)
        rectMode(CORNER)
        rect(self.posX,self.posY,210,210)
        pushMatrix()
        textFont(self.font)
        text("Speed: " + str('%.2f' % float(self.speed*10)) + " mPH", self.posX+10, self.posY-5)
        popMatrix()
        imageMode(CENTER)
        pushMatrix()
        translate(self.posX + 105 , self.posY + 105 )
        rotate(self.steeringTilt)
        image(self.dispImage, 0, 0, 150, 150)
        popMatrix()
