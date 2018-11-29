



from enum import Enum
from enum import auto

    
class enum_action_type(Enum):
    # Hammer is cocked on pulling the trigger
    DAT = auto()
    # Hammer is cocked using the recoil of a fired round
    DAR = auto()
    # The weapon has to be manually recocked and rechambered
    SA = auto()

class enum_bolt_position(Enum):
    # Closed and ready for firing
    closed = auto()
    # Half-open. Can't be fired nor loaded, but won't eject the cardridge
    half = auto()
    # Opened and ready for loading
    open = auto()

class enum_bolt_rotation(Enum):
    up = auto()
    down = auto()

class Weapon():
    
    
    name = None
    
    doables = {}
    
    is_hammer_cocked = False
    
    def __repr__(self):
        return "Captured rerp function, but didn't implement it yet"
    
    
                
    def get_actions(self, arg):
        print("arg=", arg)
        for i in self.doables.keys():
            print(i)
    
    
    
    def do(self, var, arg):
        self.doables.get(var,lambda self : self.get_actions(arg) )(self)
        
        
        