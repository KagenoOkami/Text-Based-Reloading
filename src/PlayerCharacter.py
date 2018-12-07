

from Ammunitions import Magazine

from inventoryitem import Item



class Player():

    
    inhand = None
    secondhand = None
    
    inventory = [None]*9
    
    pouch = 10 # Bullets
    
    def inventory_management(self, slot):

        #Pull item out of inventory and put in hand
        if inventory[keyasint-1] != None:
            if isinstance(self.inventory[keyasint-1], Ammunitions.Magazine):
                if self.inhand == None:
                    self.inhand = inventory[keyasint-1]
                    self.inventory[keyasint-1] = None
                    print("put", inhand, "in hand")
                    return
                elif self.secondhand == None:
                    self.secondhand = inventory[keyasint-1]
                    self.inventory[keyasint-1] = None
                    print("put", secondhand, "in second hand")
                    return
                else:
                    print("something is already in both hands")
                    return
                    
            else:
                if self.inhand == None:
                    self.inhand = inventory[keyasint-1]
                    self.inventory[keyasint-1] = None
                    print("put", self.inhand, "in hand")
                    return
                else:
                    print("something is already in hand")
                    return
            
        #Take out of hand and put in inventory
        else:
            if self.inhand != None:
                inventory[keyasint-1] = inhand
                print("Put", self.inventory[keyasint-1], "in inventory slot", keyasint)
                self.inhand = None
                return
            else:
                print("There's already something in this slot")
                return

    def pass_action(self, command):
        if self.inhand != None:
            self.inhand.do(command, self)
        elif secondhand != None:
            self.secondhand.do(command, self)
        else:
            print("Hands are empty")
        return





