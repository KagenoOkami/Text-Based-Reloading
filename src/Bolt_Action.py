
from Weapons import Weapon
from Weapons import enum_bolt_position
from Weapons import enum_bolt_rotation

from Ammunitions import Cardridge



class Bolt_Action_Rifle(Weapon):

    name = None

    
    bolt_position =  [enum_bolt_position.closed, enum_bolt_rotation.down]

    # Complex action container object. Just a list.
    magazine = []
    magazine_size = 0
    
    chamber = [None]
    
    doables = { "fire" : lambda self : self.action_fire(),
                "load round" : lambda self : self.action_load_round(),
                "load round chamber" : lambda self : self.action_load_chamber(),
                "load clip" : lambda self : self.action_load_clip([Cardridge(),Cardridge(),Cardridge(),Cardridge(),Cardridge()]),
                "open bolt" : lambda self : self.action_open_bolt(),
                "open bolt half" : lambda self : self.action_open_bolt_half(),
                "close bolt" : lambda self : self.action_close_bolt(),
                "look" : lambda self : self.action_look(),
                "rotate up" : lambda self : self.action_rotate_bolt(enum_bolt_rotation.up),
                "rotate down" : lambda self : self.action_rotate_bolt(enum_bolt_rotation.down)
                }

    def __init__( self, name = "Default", magazine_size = 5 ):
        
        self.name = name
        
        self.chamber = [None]
        
        self.magazine_size = magazine_size
        
        print("Made a bolt action type weapon \"" +self.name+"\"" )

    def __repr__(self):
        return "Captured rerp function, but didn't implement it yet"

    def action_fire(self):
        
        print("Firing rifle")
        if self.bolt_position == [enum_bolt_position.closed, enum_bolt_rotation.down]:
            if self.is_hammer_cocked == True:
                self.is_hammer_cocked = False

                if type(self.chamber) == type(Cardridge()):
                    if self.chamber.bullet:
                        print("Firing round")
                        self.chamber.fire()
                        
                    else:
                        print("The cartridge wasn't armed")
                else:
                    print("There was no cartridge" )
            else:
                print("The hammer wasn't cocked")
        else:
            print("The bolt isn't closed")

    def action_cock_hammer(self):
        
        if self.is_hammer_cocked == False:
            print("Cocking hammer")
            self.is_hammer_cocked = True
        else:
            print("Hammer was already cocked")
            
    def action_open_bolt(self, toPosition = enum_bolt_position.open):
        
        if self.bolt_position[0] != toPosition:
            if self.bolt_position[1] == enum_bolt_rotation.up:
                self.bolt_position[0] = enum_bolt_position.open
                print("Opened bolt")
                
                # When the bolt is returned fully, anything in the chamber is ejected regardless
                self.action_eject_chamber()
            else:
                print("Can't pull, bolt is down")
        else:
            print("The bolt is already open")
    
    
    def action_open_bolt_half(self, toPosition = enum_bolt_position.half):
        
        if self.bolt_position[0] != toPosition:
            if self.bolt_position[1] == enum_bolt_rotation.up:
                self.bolt_position[0] = enum_bolt_position.half
                print("Half opened bolt")
            else:
                print("Can't pull, bolt is down")
        else:
            print("The bolt is already half open")
    
    def action_close_bolt(self, toPosition = enum_bolt_position.closed):
        if self.bolt_position[0] != toPosition:
            self.bolt_position[0] = enum_bolt_position.closed
            self.chamber_from_magazine()
            print("Closed bolt")
        else:
            print("The bolt is already closed")
    
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
    
    def action_rotate_bolt(self, direction ):
        if self.bolt_position[0] == enum_bolt_position.closed:
            if direction == enum_bolt_rotation.up:
                if self.bolt_position[1] == enum_bolt_rotation.down:
                    self.bolt_position[1] = enum_bolt_rotation.up
                    print("Rotate bolt up")
                    self.action_cock_hammer()
            elif direction == enum_bolt_rotation.down:
                if self.bolt_position[1] == enum_bolt_rotation.up:
                    self.bolt_position[1] = enum_bolt_rotation.down
                    print("Rotate bolt down")
        else:
            print("Bolt can only be rotated in clsoed position")
            
            
            
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
        
        
        if self.bolt_position[0] == enum_bolt_position.open:
            if len(self.magazine) < self.magazine_size:
                
                print("Loading cartridge into magazine")
                self.magazine.append(Cardridge())
                
            else:
                print("The magazine is full")
        else:
            print("Can't load cartridges if the action is closed.")
            
    def action_load_chamber(self):
        if self.bolt_position[0] == enum_bolt_position.open:
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
        if self.bolt_position[0] == enum_bolt_position.open:
            
            if self.chamber != None:
                print("ejecting cardridge")
                self.chamber = None
        else:
            print("Can't extract cardridges if the action is closed")
            