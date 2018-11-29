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


print("")

loop = True

while loop:

    var = input(inhand.name+":").lower().strip()
    
    var_temp = var.split()
    
#    var, arg = var_temp[0], var_temp[1:]
    arg = ""
    
    if var == "exit":
        loop = False
    else:
        inhand.do(var, arg)



print("Ending program")









