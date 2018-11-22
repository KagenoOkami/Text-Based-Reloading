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
	
	# Fixed; Rounds can only be loaded one at a time.
	Fixed = 1
	
	# Swing; cylinder swings to the side
	Swing = 2


class Revolver():

	name = None

	hammer_action_is = None

	loading_action_is = None

	is_hammer_cocked = False
	
	is_action_open = False
	
	has_speed_extractor = False
	
	cartridge = None

	# Complex Cylinder container object. Just a list.
	cylinder = []

	# Which part of the cylinder is on top. Counts clockwise.
	cylinder_top = 0
	
	doables = {}

	def __init__( self, name = "Default", cylinder_chamber_count = 6, action_type = Hammer_action.DAT, loading_action = Loading_action.Swing, has_speedextractor = False ):
		
		self.name = name

		self.cylinder = [None]*cylinder_chamber_count
#		self.cylinder = [1]*cylinder_chamber_count # Debug line

		self.hammer_action_is = action_type
		self.loading_action_is = loading_action
		self.has_speed_extractor = has_speedextractor

		print("Made the revolver type weapon \"" +self.name+"\"" )
		print("\t Action:",self.hammer_action_is)
		print("\t Loading:",self.loading_action_is)
		print("\t Cylinder size:",len(self.cylinder),"cardridges")
		print("\t Speedextractor:",self.has_speed_extractor)
		
		self.doables = {	"fire" : lambda self : self.action_fire(),
							    "open action" : lambda self : self.action_open_cylinder(),
							    "close action" : lambda self : self.action_close_cylinder(),
							    "look at action" : lambda self : self.action_lookat_cylinder(),
							    "cock hammer" : lambda self : self.action_cock_hammer(),
							    "get actions" : lambda self : self.get_actions(),
							    "extract" : lambda self : self.action_extract(),
							    "load" : lambda self : self.action_load(),
							    "rotate action" : lambda self : self.action_rotate_cylinder(),
			   				}
		self.doables.setdefault("get actions")

	def __repr__(self):
		return "Captured rerp function, but didn't implement it yet"

	def action_fire(self):
		print("Firing", self.name)
		# If the action is Double Action Trigger, cock the hammer
		if self.hammer_action_is == Hammer_action.DAT:
			self.action_cock_hammer()

		if self.is_hammer_cocked == True:
			self.is_hammer_cocked = False
			if self.is_action_open == False:
				if self.cylinder[self.cylinder_top] == 1:
					print("Firing round")
					self.cylinder[self.cylinder_top] = 0
					
					# If the action is Double Action Recoil, cock the hammer
					if self.hammer_action_is == Hammer_action.DAR:
						self.action_cock_hammer()

				else:
					print("There was no armed cartridge")
			else:
				print("The hammer struck, but the cylinder was open")
		else:
			print("The hammer wasn't cocked")

	def action_cock_hammer(self):
		if self.is_hammer_cocked == False:
			print("Cocking hammer")
			self.is_hammer_cocked = True
			self.action_rotate_cylinder(1)

		else:
			print("Hammer was already cocked")
			
	def action_rotate_cylinder(self, rotate = -1):
		
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
			if self.loading_action_is == Loading_action.Swing:
				
				print(self.cylinder)
				print(self.cylinder_top)
			else:
				print("Weapon is of unimplemented loading type")
		else:
			print("The cylinder is closed. Not much to look at.")
			
	def action_extract(self, using_speedextractor = False):
		
		if self.is_action_open == True:
			if using_speedextractor == True:
				for i in range(len(self.cylinder)):
					self.cylinder[i] = None
				print("extracted all cardridges with a speed extractor")
			else:
				print("No code for extracting individual cardridge")
		else:
			print("Can't extract cardridges if the cylinder is closed")
	
	def action_load(self, using_speedloader = False):
		
		if self.is_action_open == True:
			
			if using_speedloader == True:
				print("No code for speedloading")
			else:
				if self.cylinder[self.cylinder_top] == None:
					
					print("Loading cartridge")
					self.cylinder[self.cylinder_top] = 1
					
				else:
					print("There is something in this spot")
				
		else:
			print("Can't load cartridges if the cylinder is closed")
			
	def get_actions(self):
		for i in self.doables.keys():
			print(i)
	
	
	
	def do(self, var):
		self.doables.get(var,lambda self : self.get_actions() )(self)
		
			
			