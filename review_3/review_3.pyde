from tesla import tesla
from keylogger import keyLogger
from roadMap import roadMap
from phaneron import phaneron
from lidar import lidar

def setup():
    size(1330,700)
    global Tesla
    global Klogger
    global Road
    global Phaneron
    global Lidar
    Tesla = tesla()
    Klogger = keyLogger()
    Road = roadMap()
    Phaneron = phaneron(Road, Tesla)
    Lidar = lidar(Phaneron, Tesla, 32, 2, 50)
    
def draw():
    frameRate(50)
    background(20,200,20)
    Phaneron.update()
    Phaneron.show()
    Road.show()
    Tesla.show()
    Lidar.update()
    Lidar.show()

def keyPressed():
    user_input = Klogger.logKey(key)
    if (user_input == 0):
        Tesla.shift('left')
    elif (user_input == 1):
        Tesla.shift('right')
    elif (user_input == 2):
        Tesla.shift('up')
    elif (user_input == 3):
        Tesla.shift('down')    
