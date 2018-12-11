

from Ammunitions import Magazine

from inventoryitem import Item



class Player():

    
    inhand = None
    secondhand = None
    
    inventory = [None]*9
    
    pouch = 10 # Bullets
    
    def inventory_management(self, slot):
        slot-=1
        #Pull item out of inventory and put in hand
        if self.inventory[slot] != None:
            if isinstance(self.inventory[slot], Magazine):
                if self.inhand == None:
                    self.inhand = self.inventory[slot]
                    self.inventory[slot] = None
                    print("put", self.inhand, "in hand")
                    return
                elif self.secondhand == None:
                    self.secondhand = self.inventory[slot]
                    self.inventory[slot] = None
                    print("put", self.secondhand, "in second hand")
                    return
                else:
                    print("something is already in both hands")
                    return
                    
            else:
                if self.inhand == None:
                    self.inhand = self.inventory[slot]
                    self.inventory[slot] = None
                    print("put", self.inhand, "in hand")
                    return
                else:
                    print("something is already in hand")
                    return
            
        #Take out of hand and put in inventory
        else:
            if self.secondhand != None:
                self.inventory[slot] = self.secondhand
                print("Put", self.inventory[slot], "in inventory slot", slot)
                self.secondhand = None
                return
            elif self.inhand != None:
                self.inventory[slot] = self.inhand
                print("Put", self.inventory[slot], "in inventory slot", slot)
                self.inhand = None
                return
            else:
                print("Hands are empty")
                return

    def pass_action(self, command):
        if self.inhand != None:
            self.inhand.do(command, self)
        elif secondhand != None:
            self.secondhand.do(command, self)
        else:
            print("Hands are empty")
        return





