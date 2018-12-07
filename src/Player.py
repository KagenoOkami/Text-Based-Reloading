



class Player():

    
    inhand = None
    secondhand = None
    
    inventory = [shotgun2, None, None, None, None]
    
    pouch = 10 # Bullets
    
    def inventory_management(self, slot):

        #Pull item out of inventory and put in hand
        if inventory[keyasint-1] != None:
            if inhand == None:
                inhand = inventory[keyasint-1]
                inventory[keyasint-1] = None
                print("put", inhand, "in hand")
                return
            else:
                print("something is already in hand")
            
        #Take out of hand and put in inventory
        else:
            if inhand != None:
                inventory[keyasint-1] = inhand
                print("Put", inventory[keyasint-1], "in inventory slot", keyasint)
                inhand = None
                return
            else:
                print("There's already something in this slot")