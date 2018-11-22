import Revolvers

import Break_Action

#Bolt_Action
#Pump_Action
#Lever_Action
    
#Self_Loading

import subprocess

revolver = Revolvers.Revolver( name = "Revolver" )
shotgun =  Break_Action.Shotgun( name = "Shotgun" )


print("")

loop = True

while loop:

    var = input("shotgun:").lower()
    
    if var == "exit":
        loop = False
    else:
        shotgun.do(var)



print("Ending program")









