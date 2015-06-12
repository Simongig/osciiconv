# coding=UTF-8

import cv2
import copy


class glob(object):
	mouse_positions = []
	mouse_pos_noclick = (0,0)


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
		while len(glob.mouse_positions) is 0:
			if cv2.waitKey(100) is not -1:
				return False

		return glob.mouse_positions.pop()

	def get_height(self, image):
		while len(glob.mouse_positions) is 0:
			# Bild kopieren
			imgcp = copy.copy(image)
			# Höhe zeichnen
			cv2.line(imgcp, (0,glob.mouse_pos_noclick[1]), (1000,glob.mouse_pos_noclick[1]), (255,50,50), 1)
			# Bild zeichnen
			cv2.imshow("Oscilloscope", imgcp)

			if cv2.waitKey(100) is not -1:
				return False

		self.save_image(imgcp, "guckmal.png")
		return glob.mouse_positions.pop()

	def close_windows(self):
		cv2.destroyAllWindows()

	def save_image(self, image, filename):
		cv2.imwrite(filename, image)



def locate_mouse(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		glob.mouse_positions.append((x, y))
	else:
		glob.mouse_pos_noclick = (x,y)

