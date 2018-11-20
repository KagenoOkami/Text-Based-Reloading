import math
import random






class Weapon():

	name = None
	interal_storage_max = 0
	interal_storage = 0
	round_in_chamber = False

	def __init__( self, name = "Default", interal_storage_max = 6 ):
		self.name = name
		self.interal_storage_max = interal_storage_max

		self.interal_storage = self.interal_storage_max # Debugging line!

		print("Made the weapon \"",self.name,"\" with",self.interal_storage_max,"capacity")

	def load(self):
		if self.interal_storage > 0:
			if self.round_in_chamber == False:
				print("Loading round to chamber")
				self.round_in_chamber = True
				self.interal_storage -= 1
			else:
				print("There was already a round loaded")
		else:
			print("Weapon is empty, please reload")

	def fire(self):
		if self.round_in_chamber == True:
			print("Firing round")
			self.round_in_chamber = False
		else:
			print("There was no round loaded")
