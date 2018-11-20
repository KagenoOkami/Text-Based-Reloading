import math
import random

import Ammunitions

# Each weapon has its own class because they generally work uniquely. When weapons are very similiar, they probably also work identically internally/simplified.


class Action():
	#make this an enum, string are... BAD
	pass


class Revolver():

	name = None

	hammer_cocked = False

	# If Single (SA); doesn't cock hammer after firing
	# If Double Action Recoil [operated] (DAR); cocks hammer after firing
	# If Double Action Trigger [operated] (DAT); cocks hammer when pulling trigger
	action_type = ""

	# Fixed
	# Break
	# Swing
	loading_action = ""

	# Complex Cylinder object. Might beinteresting to make an object. Or not.
	cylinder = []

	# Which part of the cylinder is on top. Counts clockwise.
	cylinder_top = 0

	def __init__( self, name = "Default", cylinder_chamber_count = 6, action_type = "DAR", loading_action = "Swing" ):
		self.name = name

#		self.cylinder = [None]*cylinder_chamber_count
		self.cylinder = [1]*cylinder_chamber_count # Debug line

		self.action_type = action_type
		self.loading_action = loading_action

		print("Made the revolver type weapon \"" +self.name+"\" with",self.interal_storage_max,"capacity")


	def action_fire(self):

		# If the action is Double Action Trigger, cock the hammer
		if self.action_type == "DAR" and self.hammer_cocked == False:
			cock_hammer()

		if self.hammer_cocked == True:
			hammer_cocked = False

			if self.cylinder[cylinder_top] == 1:
				print("Firing round")
				self.cylinder[cylinder_top] == 0

				if self.action_type == "DA":
					# if double action, rotate the cylinder
					cylinder_top += 1
					# prevent overflow
					cylinder_top %= len(cylinder)

					# with DA, the hammer is cocked when shot
					hammer_cocked = True

			else:
				print("There was no round loaded")
		else:
			print("The hammer wasn't cocked")

	def cock_hammer():
		if self.hammer_cocked == False:
			self.hammer_cocked == True

			# if double action, rotate the cylinder
			cylinder_top += 1
			# prevent overflow
			cylinder_top %= len(cylinder)