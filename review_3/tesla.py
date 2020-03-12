from speedometer import speedometer

class tesla():
    
    def __init__(self):
        self.posX = 315
        self.posY = 595
        self.dispImage = loadImage("../assets/teslaTopView.png")
        self.speed = 0
        self.distance = 0
        self.angle = PI/2
        self.speedometer = speedometer()
        self.friction = 0.001

    def update(self):
        self.posX = self.posX + self.speed*sin(self.angle)
        self.posY = self.posY - self.speed*cos(self.angle)
        if(self.speedometer.steeringTilt>0):
            self.speedometer.steeringTilt = self.speedometer.steeringTilt - PI/640
        else:
            self.speedometer.steeringTilt = self.speedometer.steeringTilt + PI/640
        if(self.speed>0):
            self.speed = self.speed - self.friction
        if(self.speed<0):
            self.speed = self.speed + self.friction
        
    def shift(self, argument):
        if (argument == "right"):
            if ((self.speed>0.01) or (self.speed<-0.01)):
                self.angle  = self.angle + PI/30
                self.speedometer.steeringTilt = self.speedometer.steeringTilt + PI/20
        elif (argument == "left"):
            if ((self.speed>0.01) or (self.speed<-0.01)):
                self.angle = self.angle - PI/30
                self.speedometer.steeringTilt = self.speedometer.steeringTilt - PI/20
        elif (argument == "up"):
            self.speed += 0.05
        elif (argument == "down"):
            self.speed -= 0.05
            
    def show(self):
        self.update()
        imageMode(CENTER)
        pushMatrix()
        translate(self.posX, self.posY)
        rotate(self.angle)
        #image(self.dispImage, 0, 0, 60, 125)
        image(self.dispImage, 0, 0, 42, 87) #70% reduction in size
        popMatrix()
        self.speedometer.show(self.distance, self.speed)
        #self.speedometer.steeringTilt = 0
