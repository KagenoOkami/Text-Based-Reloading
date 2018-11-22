import math
import random

from enum import Enum

import Ammunitions


class Shotgun():

    name = None

    is_hammer_cocked = [False, False]
    
    is_action_open = False

    # Complex action container object. Just a list.
    barrels = [None, None]
    
    doables = { "firel" : lambda self : self.action_fire(0),
                "firer" : lambda self : self.action_fire(1),
                "fire" : lambda self : self.action_fire('b'),
                "cockl" : lambda self : self.action_cock_hammer(0),
                "cockr" : lambda self : self.action_cock_hammer(1),
                "cock" : lambda self : self.action_cock_hammer('b'),
                "extractl" : lambda self : self.action_extract(0),
                "extractr" : lambda self : self.action_extract(1),
                "extract" : lambda self : self.action_extract('b'),
                "loadl" : lambda self : self.action_load(0),
                "loadr" : lambda self : self.action_load(1),
                "open" : lambda self : self.action_open_action(),
                "close" : lambda self : self.action_close_action(),
                "look" : lambda self : self.action_lookat_action(),
                "actions" : lambda self : self.get_actions()
                }

    def __init__( self, name = "Default", is_doubleAction = False, barrel_count = 1 ):
        
        self.name = name
        self.is_doubleAction = is_doubleAction
        
        self.barrels = [None]*barrel_count
        
        print("Made the revolver type weapon \"" +self.name+"\"" )

    def __repr__(self):
        return "Captured rerp function, but didn't implement it yet"

    def action_fire(self, barrel = 'b'):
        
        if barrel == 'b':
            self.action_fire(0)
            self.action_fire(1)
        else:
            print("Firing", self.name,"barrel", barrel+1)
            if self.is_hammer_cocked[barrel] == True:
                self.is_hammer_cocked[barrel] = False
                
                if self.is_action_open == False:
                    
                    if self.barrels[barrel] == 1:
                        print("Firing round")
                        self.barrels[barrel] = 0
                        if self.is_doubleAction:
                            # If the action is Double Action Trigger, cock the hammer
                            self.action_cock_hammer(barrel)
                    else:
                        print("There was no armed cartridge")
                else:
                    print("The hammer struck, but the cylinder was open")
            else:
                print("The hammer wasn't cocked")

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
                self.barrels[barrel] = None
        else:
            print("Can't extract cardridges if the action is closed")
    
    def action_load(self, barrel):
        
        if self.is_action_open == True:
            if self.barrels[barrel] == None:
                
                print("Loading cartridge")
                self.barrels[barrel] = 1
            else:
                print("There is something in this spot")
        else:
            print("Can't load cartridges if the action is closed")
            
    def get_actions(self):
        for i in sorted(self.doables.keys()):
            print(i)
    
    
    
    def do(self, var):
        self.doables.get(var,lambda self : self.get_actions() )(self)
        
            
            