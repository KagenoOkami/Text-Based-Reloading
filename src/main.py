import Revolvers

import Break_Action

import Bolt_Action

#Pump_Action
    
#Self_Loading

import subprocess

revolver = Revolvers.Revolver( name = "Revolver" )
shotgun =  Break_Action.Shotgun( name = "Shotgun", barrel_count = 2 )
bolt_action_rifle = Bolt_Action.Bolt_Action_Rifle( name = "Rifle", magazine_size = 3)


print("")

loop = True

while loop:

    var = input(bolt_action_rifle.name+":").lower()
    
    if var == "exit":
        loop = False
    else:
        bolt_action_rifle.do(var)



print("Ending program")









