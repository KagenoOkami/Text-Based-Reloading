from inventoryitem import Item


class Magazine(Item):
    magazine = []
    name = "Magazine"
    
    def __init__(self):
        self.magazine = [Cardridge() for x in range(4)]
        '''
        if contents == None:
            for dummy in range(magazine_size):
                self.magazine.append(Cardridge(True))
        else:
            self.magazine = contents
        '''
    
    def __repr__(self):
        return self.name
    
    def do(self):
        pass
    
    def look(self):
        return self.magazine
    
    def data(self):
        return self.magazine
        
    
class Clip(Item):
    clip = []
    name = "Clip"
    def __init__(self):
        self.clip = [Cardridge() for x in range(5)]
        pass
    
    def __repr__(self):
        return self.name
    
    def look(self):
        return self.clip
    
    def data(self):
        return self.clip

class Cardridge(Item):
    
    primer = True
    
    name = "bullet"
    
    
    def __init__(self, primer=True):
        self.primer = primer
    
    def fire(self):
        if self.primer == True:
            self.primer = False
            return True
        
        return False
    
    def __repr__(self):
        if self.primer == True:
            return "O"
        else:
            return "X"
    
    


