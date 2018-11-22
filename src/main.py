from Weapons import Revolvers

import subprocess

revolver = Revolvers.Revolver(
                             name = "Revolver",
                             cylinder_chamber_count = 6,
                             action_type = Revolvers.Hammer_action.DAT,
                             loading_action = Revolvers.Loading_action.Swing
                            )



print("")

loop = True

while loop:

    var = input("---:").lower()
    
    if var == "exit":
        loop = False
    else:
        revolver.do(var)



print("Ending program")









