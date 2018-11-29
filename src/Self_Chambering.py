
from Weapons import Weapon
from Weapons import enum_bolt_position
from Weapons import enum_action_type

from Ammunitions import Cardridge


class Self_Chambering_Pistol(Weapon):
    
    bolt_position =  enum_bolt_position.closed
    
    is_bolt_locked = False
    
    action_type = None
    
    # Complex action container object. Just a list.
    magazine = None
    magazine_size = 0
    
    chamber = [None]
    
    doables = { "fire" : lambda self : self.action_fire(),
                "open" : lambda self : self.action_open_bolt(),
                "close" : lambda self : self.action_close_bolt(),
                "look" : lambda self : self.action_look(),
                "actions" : lambda self : self.get_actions(),
                "load" : lambda self : self.action_load_magazine([Cardridge(),Cardridge(),Cardridge(),Cardridge()]),
                "eject" : lambda self : self.action_eject_magazine()
                }

    def __init__( self, name = "Default", magazine_size = 5, action_type = enum_action_type.DAR ):
        
        self.name = name
        
        self.chamber = [None]
        
        self.magazine_size = magazine_size
        
        self.action_type =  action_type
        
        if self.action_type == enum_action_type.DAR:
            self.doables["cock"] = lambda self : self.action_cock_hammer()
        
        print("Made a self chambering type weapon \"" +self.name+"\"" )

    def __repr__(self):
        return "Captured rerp function, but didn't implement it yet"

    def action_fire(self):
        
        print("Firing rifle")
            
        if self.bolt_position == enum_bolt_position.closed:
            if self.action_type==enum_action_type.DAT:
                self.action_cock_hammer()
            
            if self.is_hammer_cocked == True:
                self.is_hammer_cocked = False
                
                if type(self.chamber) == type(Cardridge()):
                    if self.chamber.bullet:
                        print("Firing round")
                        self.chamber.fire()
                        self.action_open_bolt()
                        if len(self.magazine):
                            self.action_close_bolt()
                        else:
                            print("Magazine is empty, locked bolt open")
                        
                    else:
                        print("The cartridge wasn't armed")
                else:
                    print("There was no cartridge" )
                    
                    
                if self.chamber == 1:
                    print("Firing round")
                    self.chamber.fire()
                else:
                    print("There was no armed cartridge")
            else:
                print("The hammer wasn't cocked")
        else:
            print("The chamber isn't closed")

    def action_cock_hammer(self):
        
        if self.is_hammer_cocked == False:
            print("Cocking hammer")
            self.is_hammer_cocked = True
        else:
            print("Hammer was already cocked")
            
    def action_open_bolt(self, toPosition = enum_bolt_position.open, stay_open = False):
        
        if self.bolt_position != toPosition:
            self.bolt_position = enum_bolt_position.open
            print("Opened bolt")
            
            if self.action_type == enum_action_type.DAR:
                self.action_cock_hammer()
            
            # When the bolt is drawn fully, anything in the chamber is ejected regardless
            self.action_eject_chamber()
        else:
            print("The bolt is already open")
    
    
    def action_open_bolt_half(self, toPosition = enum_bolt_position.half):
        
        if self.bolt_position != toPosition:
            self.bolt_position = enum_bolt_position.half
            print("Half opened bolt")
        else:
            print("The bolt is already half open")
    
    def action_close_bolt(self, toPosition = enum_bolt_position.closed):
        if self.bolt_position != toPosition:
            self.bolt_position = enum_bolt_position.closed
            self.chamber_from_magazine()
            print("Closed bolt")
        else:
            print("The bolt is already closed")
            
    
    def action_look(self):
        
        # The self_chambering weapon doesn't need to open the bolt manually, because the bolt isn't locked and slides forward on it's own.
        print("Chamber:",self.chamber)
        print("debug: Magazine:", self.magazine)
        if self.magazine:
            print("Magazine:",self.magazine)
        else:
            print("Magazine is empty")
            
            
            
    def chamber_from_magazine(self):
        if len(self.magazine):
            if self.chamber == None:
                self.chamber = self.magazine.pop()
                print("Loaded round to chamber from magazine")
                return True
            else:
                print("Couldn't load round into chamber")
                return False
        else:
            print("magazine is empty")
    
    def action_load_magazine(self, new_magazine):
        
        if self.magazine == None:
            
            print("Loading magazine into gun", new_magazine)
            self.magazine = new_magazine
        else:
            print("Magazine slot is occupied")
            
    def action_eject_magazine(self):
        
        if self.magazine != None:
            print("Ejecting magazine")
            temp = self.magazine
            self.magazine = None
            return temp
        else:
            print("Magazine slot was already empty")
            
    def action_eject_chamber(self):
        
        # This check shouldn't be nessasery, but safety first
        if self.bolt_position == enum_bolt_position.open:
            
            if self.chamber != None:
                print("ejecting cardridge")
                self.chamber = None
        else:
            print("Can't extract cardridges if the action is closed")
            