
from Weapons import Weapon
from Weapons import enum_bolt_position
from Weapons import enum_action_type

from Ammunitions import Cardridge
from Ammunitions import Magazine


class Self_Chambering_Pistol(Weapon):
    
    bolt_position =  enum_bolt_position.closed
    
    is_bolt_locked = False
    
    action_type = None
    
    # Complex action container object. Just a list.
    magazine = None
    magazine_size = 0
    
    chamber = [None]
    
    doables = { "j" : lambda self : self.action_fire(),
                "v" : lambda self : self.action_move_bolt(enum_bolt_position.open),
                "f" : lambda self : self.action_move_bolt(enum_bolt_position.half),
                "r" : lambda self : self.action_move_bolt(enum_bolt_position.closed),
                "s" : lambda self : self.action_look(),
                "k" : lambda self : self.action_load_magazine(),
                "," : lambda self : self.action_eject_magazine()
                }

    def __init__( self, theplayer, name = "Default", magazine_size = 5, action_type = enum_action_type.DAR ):
        self.theplayer = theplayer
        
        self.name = name
        
        self.chamber = [None]
        
        self.magazine_size = magazine_size
        
        self.action_type =  action_type
        
        if self.action_type == enum_action_type.DAR:
            self.doables["cock"] = lambda self : self.action_cock_hammer()
        
        print("Made a self chambering type weapon \"" +self.name+"\"" )

    def __repr__(self):
        return self.name

    def action_fire(self):
        
        print("Firing", self.name)
            
        if self.bolt_position == enum_bolt_position.closed:
            if self.action_type==enum_action_type.DAT:
                self.action_cock_hammer()
            
            if self.is_hammer_cocked == True:
                self.is_hammer_cocked = False
                
                if type(self.chamber) == type(Cardridge()):
                    if self.chamber.primer:
                        print("Firing round")
                        self.chamber.fire()
                        
                        if len(self.magazine.magazine):
                            self.action_move_bolt(enum_bolt_position.open)
                        else:
                            self.action_move_bolt(enum_bolt_position.locked)
                            print("Magazine is empty, locked bolt open")
                        
                        
                        
                    else:
                        print("The cartridge wasn't armed")
                else:
                    print("There was no cartridge" )
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
    
    def action_move_bolt(self, toPosition):
        
        #------------------------------------------------------------------
        if toPosition == enum_bolt_position.closed:
            if self.bolt_position != toPosition:
                if self.bolt_position != enum_bolt_position.half:
                    self.chamber_from_magazine()
                    
                self.bolt_position = enum_bolt_position.closed
                print("Closed bolt")
            else:
                print("Bolt is already closed")
        
        #------------------------------------------------------------------
        if toPosition == enum_bolt_position.half:
            if self.bolt_position != toPosition:
                self.bolt_position = enum_bolt_position.half
                print("Bolt opened partially")
            else:
                print("Bolt is already partially open")
                
        #------------------------------------------------------------------
        # Special case
        # Doesn't lock open and returns to closed immidiatly.
        # Effectivly racks the slide
        if toPosition == enum_bolt_position.open:
            if self.bolt_position != toPosition:
                self.bolt_position = enum_bolt_position.open
                print("Bolt opened")
                
                if self.action_type == enum_action_type.DAR:
                    self.action_cock_hammer()
                    
                # When the bolt is drawn fully, anything in the chamber is ejected regardless
                self.action_eject_chamber()
                
                self.action_move_bolt(enum_bolt_position.closed)
            else:
                print("Bolt is already open")
                
        #------------------------------------------------------------------
        if toPosition == enum_bolt_position.locked:
            if self.bolt_position != toPosition:
                self.bolt_position = enum_bolt_position.locked
                print("Bolt opened")
                
                if self.action_type == enum_action_type.DAR:
                    self.action_cock_hammer()
                    
                # When the bolt is drawn fully, anything in the chamber is ejected regardless
                self.action_eject_chamber()
            else:
                print("Odd state; bolt can't be locked if it was already locked!")
            
    
    def action_look(self):
        
        # The self_chambering weapon doesn't need to open the bolt manually, because the bolt isn't locked and slides forward on it's own.
        print("Chamber:",self.chamber)
        print("debug: Magazine:", self.magazine.look())
        if self.magazine:
            print("Magazine:",self.magazine.look())
        else:
            print("Magazine is empty")
            
            
            
    def chamber_from_magazine(self):
        if self.magazine != None and len(self.magazine.data()):
            if self.chamber == None:
                self.chamber = self.magazine.magazine.pop()
                print("Loaded round to chamber from magazine")
                return True
            else:
                print("Couldn't load round into chamber")
                return False
        else:
            print("magazine is empty")
    
    def action_load_magazine(self):
        global theplayer
        
        if self.magazine == None:
            if self.theplayer.secondhand != None:
                print("Loading magazine into gun", self.theplayer.secondhand.data())
                self.magazine = self.theplayer.secondhand
                self.theplayer.secondhand = None
            else:
                print("Left hand is empty")
        else:
            print("Magazine slot is occupied")
            
    def action_eject_magazine(self):
        
        if self.magazine != None:
            if self.theplayer.secondhand == None:
                print("Ejecting magazine")
                self.theplayer.secondhand = self.magazine
                self.magazine = None
            else:
                print("Left hand is not empty")
        else:
            print("Magazine slot was already empty")
            
    def action_eject_chamber(self):
        
        # This check shouldn't be nessasery, but safety first
        if self.bolt_position == enum_bolt_position.open or self.bolt_position == enum_bolt_position.locked:
            
            if self.chamber != None:
                print("ejecting cardridge")
                self.chamber = None
        else:
            print("Can't extract cardridges if the action is closed")
            
            
            
            
            
            
            
            