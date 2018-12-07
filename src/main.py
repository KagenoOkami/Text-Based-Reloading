import Revolvers
import Break_Action
import Bolt_Action
import Pump_Action
import Self_Chambering

import Player

from Ammunitions import Magazine
from Ammunitions import Clip


revolver = Revolvers.Revolver( name = "Revolver" )
shotgun =  Break_Action.Shotgun( name = "Double Barrel Shotgun", barrel_count = 2 )
bolt_action_rifle = Bolt_Action.Bolt_Action_Rifle( name = "Bolt Action Rifle", magazine_size = 3)
shotgun2 = Pump_Action.Pump_Action( name = "Pump Action Shotgun", magazine_size = 3)
pistol = Self_Chambering.Self_Chambering_Pistol( name = "Semi-Auto Pistol", magazine_size = 9)

player = Player()

print("")
if inhand != None:
    print("Picked", inhand.name)


from pynput.keyboard import Key, Listener, KeyCode

def on_press(key):
    #print('{0} pressed'.format(key))
    pass

def on_release(key):
    global inhand
    global secondhand
    global pouch
    
    global inventory
    
    global revolver
    global shotgun
    global bolt_action_rifle
    global shotgun2
    global pistol
    
    
    
    #
        
    if key == Key.esc:
        # Stop listener
        return False
    
    elif 'char' in key.__dict__:
        
        if str(key.char) in ["1","2","3","4","5","6","7","8","9"]:
            Player.keyasint = int(key.char)
            
            
                
        elif key.char == '`':
            print( inventory )
            print( "inhand:", inhand )
            return
        
        
        
        elif key.char in inhand.doables.keys():
            inhand.do(key.char, self)
            return   
            
    #If it isn't a character, it shouldn't do anything here        
    else:
        return

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()




'''
while True:
    var = input(inhand.name+":").lower().strip()
    
    # var_temp = var.split()
    
    # var, arg = var_temp[0], var_temp[1:]
    arg = ""
    
    if var == "exit":
        loop = False
    else:
        inhand.do(var, arg)
'''




print("Reached end of Main.py")

