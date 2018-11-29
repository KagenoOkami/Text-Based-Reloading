from test.support import temp_cwd



class Magazine():
    def __init(self):
        pass
    
class Clip():
    def __init(self):
        pass

class Cardridge():
    
    primer = True
    bullet = True
    diameter = 0
    length = 0
    
    
    def __init__(self,primer=True,bullet=True,diameter=0,length=0):
        self.primer = primer
        self.bullet = bullet
        self.diameter = diameter
        self.length = length 
    
    def fire(self):
        if self.primer == True:
            self.primer = False
            if self.bullet == True:
                self.bullet = None
                return True
        
        return False
    
    def __repr__(self):
        temp = ""
        '''
        if self.primer == True:
            temp += "|"
        else:
            temp += ">"
        temp += "="
        if self.bullet != None:
            temp += "o"
        '''
        if self.bullet == True:
            temp += "O"
        else:
            temp += "X"
            
        return temp
    
    


