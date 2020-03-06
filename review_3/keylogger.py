from collections import defaultdict
from java.awt.event import KeyEvent
from java.lang.reflect import Modifier

class keyLogger():
    
    def __init__(self):
        self.key_names = defaultdict(lambda:'UNKNOWN')
        
        for f in KeyEvent.getDeclaredFields():
            if Modifier.isStatic(f.getModifiers()):
                self.name = f.getName()
                if self.name.startswith("VK_"):
                    self.key_names[f.getInt(None)] = self.name[3:]
                    
    def flash(self,anyString):
        fill(15)
        textSize(16)
        text(anyString, width-100, 20)

    def logKey(self,K):
        self.flash(K)
        if(K=='a'):
            return 0
        elif(K=='d'):
            return 1
        elif(K=='w'):
            return 2
        elif(K=='s'):
            return 3
        else:
            return 4
        
