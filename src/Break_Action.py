

from Weapons import Weapon
from Ammunitions import Cardridge



class Shotgun(Weapon):

    name = None

    is_hammer_cocked = [False, False]
    
    is_action_open = False

    # Complex action container object. Just a list.
    barrels = [None, None]
    
    doables = { #"," : lambda self : self.action_fire(0),
                #"." : lambda self : self.action_fire(1),
                "j" : lambda self : self.action_fire(),
                #"h" : lambda self : self.action_fire('b'),            Fun idea, but maybe not practical
                #"h" : lambda self : self.action_cock_hammer(0),
                #"j" : lambda self : self.action_cock_hammer(1),
                "k" : lambda self : self.action_cock_hammer('b'),
                "u" : lambda self : self.action_extract(0),
                "i" : lambda self : self.action_extract(1),
                "y" : lambda self : self.action_extract('b'),
                "n" : lambda self : self.action_load(0),
                "m" : lambda self : self.action_load(1),
                "r" : lambda self : self.action_open_action(),
                "v" : lambda self : self.action_close_action(),
                "s" : lambda self : self.action_lookat_action()
                }

    def __init__( self, name = "Default", is_doubleAction = False, barrel_count = 1 ):
        
        self.name = name
        self.is_doubleAction = is_doubleAction
        
        self.barrels = [None]*barrel_count
        
        print("Made a Break Action type weapon \"" +self.name+"\"" )

    def __repr__(self):
        return self.name

    def action_fire(self, barrel = 'n'):
        
        if barrel == 'b':
            self.action_fire(0)
            self.action_fire(1)
        elif barrel == 1 or barrel == 0:
            print("Firing", self.name,"barrel", barrel+1)
            if self.is_hammer_cocked[barrel] == True:
                self.is_hammer_cocked[barrel] = False
                
                if self.is_action_open == False:
                    
                    if type(self.barrels[barrel]) == type(Cardridge()):
                        if self.barrels[barrel].bullet:
                            print("Firing round")
                            self.barrels[barrel].fire()
                                
                        else:
                            print("The cartridge wasn't armed")
                    else:
                        print("There was no cartridge" )
                else:
                    print("The hammer struck, but the cylinder was open")
            else:
                print("The hammer wasn't cocked")
                
        
        else:
            #Fire a barrel that isn't cocked
            if self.is_hammer_cocked[0] == True:
                self.action_fire(0)
                return
            elif self.is_hammer_cocked[1] == True:
                self.action_fire(1)
                return

    def action_cock_hammer(self, barrel = 'b'):
        
        if barrel == 'b':
            self.action_cock_hammer(0)
            self.action_cock_hammer(1)
        else:
            if self.is_hammer_cocked[barrel] == False:
                print("Cocking hammer")
                self.is_hammer_cocked[barrel] = True
            else:
                print("Hammer was already cocked")
            
    def action_open_action(self):
        if self.is_action_open == False:
            self.is_action_open = True
            print("Opened action")
        else:
            print("Action was already open")
    
    def action_close_action(self):
        if self.is_action_open == True:
            self.is_action_open = False
            self.action_cock_hammer('b')
            print("Closed action")
        else:
            print("Action was already closed")
    
    def action_lookat_action(self):
        if self.is_action_open == True:
            print(self.barrels)
        else:
            print("The action is closed. Not much to look at.")
            
    def action_extract(self, barrel = 'b'):
        
        if self.is_action_open == True:
            if barrel == 'b':
                print("ejecting all cardriges")
                self.action_extract(0)
                self.action_extract(1)
            else:
                print("ejecting cardridge from barrel", barrel+1)
                self.barrels[barrel] = None
        else:
            print("Can't extract cardridges if the action is closed")
    
    def action_load(self, barrel):
        
        #Replace with a normalised function that just loads all the barrels with None in them.
        if self.is_action_open == True:
            if self.barrels[barrel] == None:
                
                print("Loading cartridge")
                self.barrels[barrel] = Cardridge()
            else:
                print("There is something in this spot")
        else:
            print("Can't load cartridges if the action is closed")
            
            '''
            if None in self.barrels:
                print("Loading cartridge in an empty spot")
                self.barrels[self.barrels.index(None)] = Cardridge()
            else:
                print("The barrel is full")
            '''
            
            