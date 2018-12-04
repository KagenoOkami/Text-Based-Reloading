
from Weapons import Weapon
from Weapons import enum_bolt_position
from Weapons import enum_bolt_rotation

from Ammunitions import Cardridge



class Bolt_Action_Rifle(Weapon):

    name = None

    

    # Complex action container object. Just a list.
    magazine = []
    magazine_size = 0
    
    chamber = [None]
    
    bolt_position = enum_bolt_position.locked
    
    doables = { "j" : lambda self : self.action_fire(),
                "i" : lambda self : self.action_load_chamber(),
                "k" : lambda self : self.action_load_round(),
                "," : lambda self : self.action_load_clip([Cardridge(),Cardridge(),Cardridge(),Cardridge(),Cardridge()]),
                "v" : lambda self : self.action_move_bolt(enum_bolt_position.open),
                "f" : lambda self : self.action_move_bolt(enum_bolt_position.half),
                "r" : lambda self : self.action_move_bolt(enum_bolt_position.closed),
                "t" : lambda self : self.action_move_bolt(enum_bolt_position.locked),
                "s" : lambda self : self.action_look()
                }

    def __init__( self, name = "Default", magazine_size = 5 ):
        
        self.name = name
        
        self.chamber = [None]
        
        self.magazine_size = magazine_size
        
        print("Made a bolt action type weapon \"" +self.name+"\"" )

    def __repr__(self):
        return "Captured rerp function, but didn't implement it yet"

    def action_fire(self):
        
        if self.bolt_position == enum_bolt_position.locked:
            if self.is_hammer_cocked == True:
                self.is_hammer_cocked = False

                if type(self.chamber) == type(Cardridge()):
                    if self.chamber.bullet:
                        print("Firing round")
                        self.chamber.fire()
                        
                    else:
                        print("Cartridge wasn't armed")
                else:
                    print("There was no cartridge" )
            else:
                print("Hammer wasn't cocked")
        else:
            print("Bolt isn't locked")

    def action_cock_hammer(self):
        
        if self.is_hammer_cocked == False:
            print("Hammer cocked")
            self.is_hammer_cocked = True
        else:
            print("Hammer was already cocked")
            
    def action_move_bolt(self, toPosition):
        
        #------------------------------------------------------------------
        if toPosition == enum_bolt_position.closed:
            if self.bolt_position != toPosition:
                if self.bolt_position == enum_bolt_position.locked:
                    self.bolt_position = enum_bolt_position.closed
                    self.action_cock_hammer()
                    print("Bolt unlocked")
                elif self.bolt_position != enum_bolt_position.locked:
                    self.bolt_position = enum_bolt_position.closed
                    self.chamber_from_magazine()
                    print("Bolt closed")
            else:
                print("Bolt is already closed")
        
        #------------------------------------------------------------------
        elif toPosition == enum_bolt_position.half:
            if self.bolt_position != toPosition:
                if self.bolt_position != enum_bolt_position.locked:
                    self.bolt_position = enum_bolt_position.half
                    print("Bolt partially opened")
                else:
                    print("Bolt is locked")
            else:
                print("Bolt is already partially open")
        
        #------------------------------------------------------------------
        elif toPosition == enum_bolt_position.open:
            if self.bolt_position != toPosition:
                if self.bolt_position != enum_bolt_position.locked:
                    self.bolt_position= enum_bolt_position.open
                    print("Bolt opened")
                    
                    # When the bolt is returned fully, anything in the chamber is ejected regardless
                    self.action_eject_chamber()
                else:
                    print("Bolt is locked")
            else:
                print("Bolt is already open")
                
        #------------------------------------------------------------------        
        elif toPosition == enum_bolt_position.locked:
            if self.bolt_position != toPosition:
                if self.bolt_position == enum_bolt_position.closed:
                    self.bolt_position = enum_bolt_position.locked
                    print("Bolt locked")
                else:
                    print("Bolt isn't closed")
            else:
                print("Bolt is already locked")
    
    def action_look(self):
        if self.bolt_position[0] != enum_bolt_position.closed:
            print("Chamber:",self.chamber)
            print("debug: Magazine:", self.magazine)
            if self.magazine:
                print("Magazine:",self.magazine)
            else:
                print("Magazine is empty")
        else:
            print("The action is closed. Not much to look at.")
            
            
            
    def chamber_from_magazine(self):
        if len(self.magazine):
            if self.chamber == None:
                self.chamber = self.magazine.pop()
                print("Loaded round to chamber from magazine")
            else:
                print("Couldn't load round into chamber")
        else:
            print("magazine is empty")
    
    def action_load_round(self):
        
        
        if self.bolt_position == enum_bolt_position.open:
            if len(self.magazine) < self.magazine_size:
                
                print("Loading cartridge into magazine")
                self.magazine.append(Cardridge())
                
            else:
                print("The magazine is full")
        else:
            print("Can't load cartridges if the action is closed.")
            
    def action_load_chamber(self):
        if self.bolt_position == enum_bolt_position.open:
            if self.chamber == None:
                self.chamber = Cardridge()
                print("Loading cartridge into magazine")
            else:
                print("The chamber is full")
        else:
            print("Can't load cartridges if the action is closed.")
    
    def action_load_clip(self, clip = []):
        
        if self.bolt_position[0] == enum_bolt_position.open:
            if len(self.magazine) < self.magazine_size:
                
                print("Loading cartridge into magazine")
                while len(self.magazine) < self.magazine_size:
                    self.magazine.append(clip.pop())
                
            else:
                print("The magazine is full")
        else:
            print("Can't load cartridges if the action is closed.")
            
    def action_eject_chamber(self):
        
        # This check shouldn't be nessasery, but safety first
        if self.bolt_position == enum_bolt_position.open:
            
            if self.chamber != None:
                print("ejecting cardridge")
                self.chamber = None
        else:
            print("Can't extract cardridges if the action is closed")
            