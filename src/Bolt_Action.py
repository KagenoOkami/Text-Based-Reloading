
from enum import Enum

import Ammunitions


class enum_bolt_position(Enum):
    # Closed and ready for firing
    closed = 0
    # Half-open. Can't be fired nor loaded, but won't eject the cardridge
    half = 1
    # Opened and ready for loading
    open = 2



class Bolt_Action_Rifle():

    name = None

    is_hammer_cocked = False
    
    bolt_position =  enum_bolt_position.closed

    # Complex action container object. Just a list.
    magazine = []
    magazine_size = 0
    
    chamber = [None]
    
    doables = { "fire" : lambda self : self.action_fire(),
                "load" : lambda self : self.action_load(),
                "open" : lambda self : self.action_open_action(),
                "close" : lambda self : self.action_close_action(),
                "look" : lambda self : self.action_lookat_action(),
                "actions" : lambda self : self.get_actions()
                }

    def __init__( self, name = "Default", magazine_size = 5 ):
        
        self.name = name
        
        self.chamber = [None]
        
        self.magazine_size = magazine_size
        
        print("Made the bolt action type weapon \"" +self.name+"\"" )

    def __repr__(self):
        return "Captured rerp function, but didn't implement it yet"

    def action_fire(self):
        
        print("Firing rifle")
        if self.is_hammer_cocked == True:
            self.is_hammer_cocked = False
            
            if self.bolt_position == enum_bolt_position.closed:
                
                if self.chamber == 1:
                    print("Firing round")
                    self.chamber = 0
                else:
                    print("There was no armed cartridge")
            else:
                print("The chamber isn't closed")
        else:
            print("The hammer wasn't cocked")

    def action_cock_hammer(self):
        
        if self.is_hammer_cocked == False:
            print("Cocking hammer")
            self.is_hammer_cocked = True
        else:
            print("Hammer was already cocked")
            
    def action_open_bolt(self, toPosition):
        
        if self.bolt_position != toPosition:
            self.bolt_position = enum_bolt_position.open
            print("Opened bolt")
            
            # The hammer of a bolt action is cocked when rotated, but this isn't implemented yet.
            self.action_cock_hammer()
            # When the bolt is returned fully, anything in the chamber is ejected regardless
            self.action_eject_chamber()
        else:
            print("The bolt is already open")
            
    def action_half_open_bolt(self, toPosition):
        
        if self.bolt_position != toPosition:
            self.bolt_position = enum_bolt_position.half
            print("Half opened bolt")
            
            # The hammer of a bolt action is cocked when rotated, but this isn't implemented yet.
            self.action_cock_hammer()
        else:
            print("The bolt is already half open")
    
    def action_close_bolt(self):
        if self.bolt_position != toPosition:
            self.bolt_position = enum_bolt_position.closed
            self.chamber_from_magazine(self)
            print("Closed bolt")
        else:
            print("The bolt is already open")
    
    def action_lookat_chamber(self):
        if self.bolt_position != enum_bolt_position.closed:
            print(self.chamber)
        else:
            print("The action is closed. Not much to look at.")
            
    def action_eject_chamber(self):
        
        # This check shouldn't be nessasery, but safety first
        if self.bolt_position == enum_bolt_position.open:
            
            if self.chamber == 1:
                print("ejecting chamber")
        else:
            print("Can't extract cardridges if the action is closed")
            
    def chamber_from_magazine(self):
        if len(self.magazine):
            self.chamber = self.magazine.pop()
            print("Loaded round to chamber from magazine")
        else:
            print("magazine is empty")
    
    def action_load_round(self):
        
        # Use Pop() and Push() to the magazine list (HAH, I'm a genius
        # Just don't allow more pushing than the magazine is large!
        
        
        if self.bolt_position == enum_bolt_position.open:
            if len(self.magazine) < self.magazine_size:
                
                print("Loading cartridge into magazine")
                self.magazine.push(1)
            else:
                print("The magazine is full, loading into chamber.")
                if self.chamber == None:
                    self.chamber = (1)
                else:
                    print("chamber is full too.")
        else:
            print("Can't load cartridges if the action is closed.")
            
    def get_actions(self):
        for i in sorted(self.doables.keys()):
            print(i)
    
    
    
    def do(self, var):
        self.doables.get(var,lambda self : self.get_actions() )(self)
        
            
            