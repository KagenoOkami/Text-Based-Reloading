
from Weapons import Weapon
from Weapons import enum_bolt_position

from Ammunitions import Cardridge




class Pump_Action(Weapon):

    name = None

    
    bolt_position =  enum_bolt_position.closed

    # Complex action container object. Just a list.
    magazine = []
    magazine_size = 0
    
    chamber = [None]
    
    doables = { "j" : lambda self : self.action_fire(),
                "k" : lambda self : self.action_load_round(),
                "i" : lambda self : self.action_load_chamber(),
                "v" : lambda self : self.action_move_bolt(enum_bolt_position.open),
                "f" : lambda self : self.action_move_bolt(enum_bolt_position.half),
                "r" : lambda self : self.action_move_bolt(enum_bolt_position.closed),
                "s" : lambda self : self.action_look()
                }

    def __init__( self, theplayer, name = "Default", magazine_size = 5 ):
        self.theplayer = theplayer
        
        self.name = name
        
        self.chamber = [None]
        
        self.magazine_size = magazine_size
        
        print("Made a Pump Action type weapon \"" +self.name+"\"" )

    def __repr__(self):
        return self.name

    def action_fire(self):
        
        print("Firing rifle")
        if self.bolt_position == enum_bolt_position.closed:
            if self.is_hammer_cocked == True:
                self.is_hammer_cocked = False
            
                

                if type(self.chamber) == type(Cardridge()):
                    if self.chamber.primer:
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
        if toPosition == enum_bolt_position.open:
            if self.bolt_position != toPosition:
                self.bolt_position = enum_bolt_position.open
                print("Bolt opened")
                self.action_cock_hammer()
                # When the bolt is drawn fully, anything in the chamber is ejected regardless
                self.action_eject_chamber()
            else:
                print("Bolt is already open")
    
    def action_look(self):
        if self.bolt_position != enum_bolt_position.closed:
            print("Chamber:",self.chamber)
            print("debug: Magazine:", self.magazine)
            if self.magazine:
                print("Magazine:",self.magazine)
            else:
                print("Magazine is empty")
        else:
            print("Bolt is closed. Not much to look at.")
            
            
            
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
        
        # Use Pop() and Push() to the magazine list (HAH, I'm a genius
        # Just don't allow more pushing than the magazine is large!
        
        if self.bolt_position == enum_bolt_position.open:
            if len(self.magazine) < self.magazine_size:
                
                print("Loading cartridge into magazine")
                self.magazine.append(theplayer.getCartridge())
                
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
            
    def action_eject_chamber(self):
        
        # This check shouldn't be nessasery, but safety first
        if self.bolt_position == enum_bolt_position.open:
            
            if self.chamber != None:
                print("ejecting cardridge")
                self.chamber = None
        else:
            print("Can't extract cardridges if the action is closed")