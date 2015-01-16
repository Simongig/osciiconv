# coding=UTF-8

import cv2
import numpy as np

class OscProp(object):
	"""Properties of given Oscilloscope-Screen eg Division-Count, pixels, etc.."""

	def __init__(self, oscname):
		"""Loads properties of known oscilloscope"""
		if (oscname is not None):
			print "Fixme"
		else:
			self.div_x = 0
			self.div_y = 0


