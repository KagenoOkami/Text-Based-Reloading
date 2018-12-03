
from Weapons import Weapon
from Ammunitions import Cardridge




class Revolver(Weapon):
	
	is_action_open = False
	
	is_doubleAction = True

	# Complex Cylinder container object. Just a list.
	cylinder = [None]*6

	# Which part of the cylinder is on top. Counts clockwise.
	cylinder_top = 0
	
	doables = {	"j" : lambda self : self.action_fire(),
			    "r" : lambda self : self.action_open_cylinder(),
			    "v" : lambda self : self.action_close_cylinder(),
			    "s" : lambda self : self.action_lookat_cylinder(),
			    "u" : lambda self : self.action_cock_hammer(),
			    "," : lambda self : self.action_extract(),
			    "k" : lambda self : self.action_load(),
			    "i" : lambda self : self.action_rotate_cylinder(-1),
			    "o" : lambda self : self.action_rotate_cylinder(1)
				}

	def __init__( self, name = "Default", is_doubleAction = True ):
		
		self.name = name
		self.is_doubleAction = is_doubleAction
		
		print("Made a revolver type weapon \"" +self.name+"\"" )

	def __repr__(self):
		return "Captured rerp function, but didn't implement it yet"

	def action_fire(self):
		print("Firing", self.name)

		if self.is_hammer_cocked == True:
			self.is_hammer_cocked = False
			
			if self.is_action_open == False:
				
				if type(self.cylinder[self.cylinder_top]) == type(Cardridge()):
					if self.cylinder[self.cylinder_top].bullet:
						print("Firing round")
						self.cylinder[self.cylinder_top].fire()
						if self.is_doubleAction:
							# If the action is Double Action Trigger, cock the hammer
							self.action_cock_hammer()
					else:
						print("The cartridge wasn't armed")
				else:
					print("There was no cartridge" )
			else:
				print("The hammer struck, but the cylinder was open")
		else:
			print("The hammer wasn't cocked")

	def action_cock_hammer(self):
		if self.is_hammer_cocked == False:
			print("Cocking hammer")
			self.is_hammer_cocked = True
			self.action_rotate_cylinder(-1)

		else:
			print("Hammer was already cocked")
			
	def action_rotate_cylinder(self, rotate = 1):
		
		self.cylinder_top += rotate
		# prevent overflow
		self.cylinder_top %= len(self.cylinder)
		
		pass
			
	def action_open_cylinder(self):
		if self.is_action_open == False:
			self.is_action_open = True
			print("Opened cylinder")
		else:
			print("Cylinder was already open")
	
	def action_close_cylinder(self):
		if self.is_action_open == True:
			self.is_action_open = False
			print("Closed cylinder")
		else:
			print("Cylinder was already closed")
	
	def action_lookat_cylinder(self):
		if self.is_action_open == True:
			print(self.cylinder)
			print(self.cylinder_top)
		else:
			print("The cylinder is closed. Not much to look at.")
			
	def action_extract(self):
		
		if self.is_action_open == True:
			for i in range(len(self.cylinder)):
				self.cylinder[i] = None
			print("extracted all cardridges with a speed extractor")
		else:
			print("Can't extract cardridges if the cylinder is closed")
	
	def action_load(self):
		
		#Replace with more universal code for loading the empty spots without user input
		#It barely has user input anyway, but trying to load a specific spot is impossible in the current action_look() system
		if self.is_action_open == True:
			if self.cylinder[self.cylinder_top] == None:
				
				print("Loading cartridge")
				self.cylinder[self.cylinder_top] = Cardridge()
				self.action_rotate_cylinder(1)
			else:
				print("There is something in this spot")
		else:
			print("Can't load cartridges if the cylinder is closed")

		
			
			