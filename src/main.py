import Revolvers

import Break_Action

#Bolt_Action
#Pump_Action
#Lever_Action
    
#Self_Loading

import subprocess

revolver = Revolvers.Revolver( name = "Revolver" )
shotgun =  Break_Action.Shotgun( name = "Shotgun", barrel_count = 2 )


print("")

loop = True

while loop:

    var = input("shotgun:").lower()
    
    if var == "exit":
        loop = False
    else:
        shotgun.do(var)



print("Ending program")









