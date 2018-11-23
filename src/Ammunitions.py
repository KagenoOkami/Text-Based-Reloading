




class Cardrigdge():
    
    bullet = None
    diameter = 0
    length = 0
    
    
    def __init__(self,bullet=1,diameter=0,length=0):
        pass
    
    def fire(self):
        
        if self.bullet == 1:
            self.bullet = None
            return True
        
        return False
    
    def __repr__(self):
        if self.bullet == 1:
            return "=0"
        elif self.buller == None:
            return "="