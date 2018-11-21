import math
import random

from enum import Enum

import Ammunitions

# Each weapon has its own class because they generally work uniquely. When weapons are very similiar, they probably also work identically internally/simplified.


class Hammer_action(Enum):
    # Single Action (SA); doesn't cock hammer after firing
    SA = 1
    
    # Double Action Recoil [operated] (DAR); cocks hammer after firing
    DAR = 2
    
    # Double Action Trigger [operated] (DAT); cocks hammer when pulling trigger
    DAT = 3

class Loading_action(Enum):
    
    # Break; barrel hinges forward
    Break = 1


class Break_Action():

    name = None

    hammer_action_is = None

    loading_action_is = None

    is_hammer_cocked = False
    
    is_action_open = False
    
    can_selfextract = False
    
    cartridge = None

    # Complex barrel container object. Just a list of all the barrels it has.
    barrels = []

    def __init__( self, name = "Default", barrel_count = 1, action_type = Hammer_action.DAT, loading_action = Loading_action.Swing, can_selfextract = False ):
        
        self.name = name

        self.barrels = [None]*barrel_count

        self.hammer_action_is = action_type
        self.loading_action_is = loading_action
        
        self.can_selfextract = can_selfextract

        print("Made the revolver type weapon \"" +self.name+"\"" )
        print("\t Action:",self.hammer_action_is)
        print("\t Loading:",self.loading_action_is)
        print("\t barrels:",len(self.barrels),"barrels")
        print("\t can selfextract:",self.can_selfextract)

    def __repr__(self):
        return "Captured rerp function, but didn't implement it yet"

    def action_fire(self, barrel = 0):
        print("Firing", self.name)

        if self.is_hammer_cocked == True:
            self.is_hammer_cocked = False
            if self.is_action_open == False:
                if self.cylinder[self.cylinder_top] == 1:
                    print("Firing round")
                    self.cylinder[self.cylinder_top] = 0
                    
                    # If the action is Double Action Recoil, cock the hammer
                    if self.hammer_action_is == Hammer_action.DAR:
                        self.action_cock_hammer()

                else:
                    print("There was no armed cartridge")
            else:
                print("The hammer struck, but the cylinder was open")
        else:
            print("The hammer wasn't cocked")

    def action_cock_hammer(self):
        if self.is_hammer_cocked == False:
            print("Cocking hammer")
            self.is_hammer_cocked = True

        else:
            print("Hammer was already cocked")

            
            
    def action_open_action(self, using_selfextraction = False):
        if self.is_action_open == False:
            self.is_action_open = True
            print("Opened cylinder")
            if using_selfextraction == True:
                print("Ejecting all barrels")
                for i in range(len(barrels)):
                    barrels[i] = None
        else:
            print("Cylinder was already open")
    
    def action_close_action(self):
        if self.is_action_open == True:
            self.is_action_open = False
            print("Closed cylinder")
        else:
            print("Cylinder was already closed")
    
    def action_lookat_action(self):
        if self.is_action_open == True:
            
            print(self.barrels)
        else:
            print("The cylinder is closed. Not much to look at.")
            
    def action_extract(self, barrel = 0):
        if self.is_action_open == True:
            self.barrels[barrel] = None
        
    
    def action_load(self, barrel = 0, cartridge = 1):
        if self.is_action_open == True:
            if self.barrels[barrel] != None:
                self.barrels[barrel] = cartridge
            else:
                print("There is something in this spot")
        else:
            print("Can't load cartridges if the cylinder is closed")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            