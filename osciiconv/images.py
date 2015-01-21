# coding=UTF-8

import cv2
import time


mouse_positions = []


class Images(object):
	"""Class contains original and new image"""

	def __init__(self):
		self.OriginalImage = None
		self.EditedImage   = None
		self.NewImage      = None

		self.contours = None
		self.centers  = None
#-------------------------------------------------------------------------------
	def load_image(self, path):
		self.OriginalImage = None
		self.OriginalImage = cv2.imread(path)
		if (self.OriginalImage is not None):
			self.OriginalImage = cv2.medianBlur(self.OriginalImage,5)
			self.EditedImage = cv2.cvtColor(self.OriginalImage, cv2.COLOR_BGR2GRAY)
			return True
		return False


	def show_image(self, image, wait=True, locate_clicks=False):
		cv2.namedWindow("Oscilloscope", cv2.WINDOW_NORMAL)
		if locate_clicks:
			cv2.setMouseCallback("Oscilloscope", locate_mouse)
		cv2.imshow("Oscilloscope", image)
		if wait:
			cv2.waitKey(0)

	def get_coordinate(self):
		while len(mouse_positions) is 0:
			if cv2.waitKey(100) is not -1:
				return False

		return mouse_positions.pop()

	def close_windows(self):
		cv2.destroyAllWindows()

	def save_image(self, image, filename):
		cv2.imwrite(filename, image)



def locate_mouse(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		mouse_positions.append((x, y))

