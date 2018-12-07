import Revolvers
import Break_Action
import Bolt_Action
import Pump_Action
import Self_Chambering

import Ammunitions

import Weapons

from inventoryitem import Item

import PlayerCharacter

theplayer = PlayerCharacter.Player()

revolver = Revolvers.Revolver( name = "Revolver" )
shotgun =  Break_Action.Shotgun( name = "Double Barrel Shotgun", barrel_count = 2 )
bolt_action_rifle = Bolt_Action.Bolt_Action_Rifle( name = "Bolt Action Rifle", magazine_size = 3)
shotgun2 = Pump_Action.Pump_Action( theplayer, name = "Pump Action Shotgun", magazine_size = 3)
pistol = Self_Chambering.Self_Chambering_Pistol( name = "Semi-Auto Pistol", magazine_size = 9)

theplayer.inhand = shotgun2
theplayer.inventory[1] = Ammunitions.Magazine()

print("")

print(isinstance(theplayer.inventory[1], Ammunitions.Magazine ))

print("")


from pynput.keyboard import Key, Listener, KeyCode

def on_press(key):
    #print('{0} pressed'.format(key))
    pass

def on_release(key):
    global theplayer
        
    if key == Key.esc:
        # Stop listener
        return False
    
    elif 'char' in key.__dict__:
        
        if str(key.char) in ["1","2","3","4","5","6","7","8","9"]:
            keyasint = int(key.char)
            theplayer.inventory_management(keyasint)
            
            
                
        elif key.char == '`':
            print( theplayer.inventory )
            print( "inhand:", theplayer.inhand )
            return
        
        
        
        elif key.char in theplayer.inhand.doables.keys():
            theplayer.pass_action(key.char)
            return   
            
    #If it isn't a character, it shouldn't do anything, least of all not crash everything        
    else:
        return

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()





print("Reached end of Main.py")

