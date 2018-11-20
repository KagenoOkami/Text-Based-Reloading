import math
import random

from enum import Enum

import Ammunitions

# Each weapon has its own class because they generally work uniquely. When weapons are very similiar, they probably also work identically internally/simplified.


class Hammer_action(Enum):
	# Single Action (SA); doesn't cock hammer after firing
	SA = 1
	
	# Double Action Recoil [operated] (DAR); cocks hammer after firing
	DAR = 2
	
	# Double Action Trigger [operated] (DAT); cocks hammer when pulling trigger
	DAT = 3

class Loading_action(Enum):
	# Front; Powder and Bullet have to be loaded seperatly.
	Front = 1
	
	# Fixed; Rounds can only be loaded one at a time.
	Fixed = 2
	
	# Break; cylinder and barrel hing forward
	Break = 3
	
	# Swing; cylinder swings to the side
	Swing = 4


class Revolver():

	name = None

	action_type = None

	loading_action = None

	is_hammer_cocked = False
	
	is_cylinder_open = False

	# Complex Cylinder object. Might beinteresting to make an object. Or not.
	cylinder = []

	# Which part of the cylinder is on top. Counts clockwise.
	cylinder_top = 0

	def __init__( self, name = "Default", cylinder_chamber_count = 6, action_type = Hammer_action.DAT, loading_action = Loading_action.Swing ):
		
		self.name = name

#		self.cylinder = [None]*cylinder_chamber_count
		self.cylinder = [1]*cylinder_chamber_count # Debug line

		self.action_type = action_type
		self.loading_action = loading_action

		print("Made the revolver type weapon \"" +self.name+"\"" )


	def action_fire(self):

		# If the action is Double Action Trigger, cock the hammer
		if self.action_type == Hammer_action.DAT:
			self.cock_hammer()

		if self.is_hammer_cocked == True:
			self.is_hammer_cocked = False
			if self.is_cylinder_open == False:
				if self.cylinder[self.cylinder_top] == 1:
					print("Firing round")
					self.cylinder[self.cylinder_top] = 0
					
					# If the action is Double Action Recoil, cock the hammer
					if self.action_type == Hammer_action.DAR:
						self.cock_hammer()
				else:
					print("The hammer struck, but the cylinder was open")

			else:
				print("There was no cartridge loaded")
		else:
			print("The hammer wasn't cocked")

	def cock_hammer(self):
		if self.is_hammer_cocked == False:
			print("Cocked hammer")
			self.is_hammer_cocked = True
			self.action_rotate_cylinder()

		else:
			print("Hammer was already cocked")
			
	def action_rotate_cylinder(self, rotate = 1):
		
		self.cylinder_top += rotate
		# prevent overflow
		self.cylinder_top %= len(self.cylinder)
		
		pass
			
	def action_open_cylinder(self):
		if self.is_cylinder_open == False:
			self.is_cylinder_open = True
			print("Opened cylinder")
		else:
			print("Cylinder was already open")
	
	def action_close_cylinder(self):
		if self.is_cylinder_open == True:
			self.is_cylinder_open = False
			print("Closed cylinder")
		else:
			print("Cylinder was already close")
	
	def action_lookat_cylinder(self):
		if self.is_cylinder_open == True:
			if self.loading_action == Loading_action.Swing:
				
				print(self.cylinder)
				mu = " "+"   "*self.cylinder_top+"^" 
				print(mu)
				#[1, 1, 1, 1, 1, 1]
				#0
		else:
			print("The cylinder is closed. Not much to look at.")
			
			
			
			
			
			
			
			
			
			