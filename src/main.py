import Revolvers
import Break_Action
import Bolt_Action
import Pump_Action
import Self_Chambering


revolver = Revolvers.Revolver( name = "Revolver" )
shotgun =  Break_Action.Shotgun( name = "Double Barrel Shotgun", barrel_count = 2 )
bolt_action_rifle = Bolt_Action.Bolt_Action_Rifle( name = "Bolt Action Rifle", magazine_size = 3)
shotgun2 = Pump_Action.Pump_Action( name = "Pump Action Shotgun", magazine_size = 3)
pistol = Self_Chambering.Self_Chambering_Pistol( name = "Semi-Auto Pistol", magazine_size = 9)


inhand = shotgun2

inventory = [None]*10

print("")


from pynput.keyboard import Key, Listener, KeyCode

def on_press(key):
    #print('{0} pressed'.format(key))
    pass

def on_release(key):

    if False:
        pass
        
    
    elif key.char == '1':
        # (inventory[0], inhand) = (inhand, inventory[0])
        inhand = revolver
    elif key.char == '2':
        inhand = shotgun
    elif key.char == '3':
        inhand = bolt_action_rifle
    elif key.char == '4':
        inhand = shotgun2
    elif key.char == '5':
        inhand = pistol
        
    # Goes last; weapons should never overwrite non-weapon actions
    elif key.char in inhand.doables.keys():
        inhand.do(key.char, "")
        
    elif key == Key.esc:
        # Stop listener
        return False
    else:
        print(key.char, "pressed")

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

