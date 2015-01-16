# coding=UTF-8

import cv2
import numpy as np

class Images(object):
	"""Class contains original and new image"""

	def __init__(self):
		self.OriginalImage = None
		self.NewImage      = None
#-------------------------------------------------------------------------------
	def load_image(self, path):
		self.OriginalImage = None
		self.OriginalImage = cv2.imread(path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
		if (self.OriginalImage is not None):
			self.OriginalImage = cv2.medianBlur(self.OriginalImage,5)
			return True
		return False

	def show_edited(self):
		cv2.namedWindow("Oscilloscope", 1)
		cv2.imshow("Oscilloscope", self.OriginalImage)
		cv2.waitKey(0)

	def show_new(self):
		cv2.namedWindow("Oscilloscope", 1)
		cv2.imshow("Oscilloscope", self.NewImage)
		cv2.waitKey(0)

	def save_edited(self, name):
		cv2.imwrite(name, self.OriginalImage)

	def save_new(self, name):
		cv2.imwrite(name, self.NewImage)


