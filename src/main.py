import Revolvers

import Break_Action

import Bolt_Action

import Pump_Action
    
import Self_Chambering

import subprocess

revolver = Revolvers.Revolver( name = "Revolver" )
shotgun =  Break_Action.Shotgun( name = "Shotgun", barrel_count = 2 )
bolt_action_rifle = Bolt_Action.Bolt_Action_Rifle( name = "Rifle", magazine_size = 3)
shotgun2 = Pump_Action.Pump_Action( name = "Pump Action Shotgun", magazine_size = 3)


inhand = shotgun2


print("")

loop = True

while loop:

    var = input(inhand.name+":").lower()
    
    if var == "exit":
        loop = False
    else:
        inhand.do(var)



print("Ending program")









