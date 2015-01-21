# coding=UTF-8

import cv2
import copy
import numpy as np

import images

class ImageEdit(object):
	"""To edit the original image for better image processing"""

	def process_image(self, images):
		self.thresholding(images)
		images.contours = self.contours(images)
		images.centers = self.centers(images)
		#self.lines(images, images.centers)


	def thresholding(self, images):
		ret, images.EditedImage = cv2.threshold(images.EditedImage, 170, 255, cv2.THRESH_BINARY)


	def contours(self, images, draw=True):
		# Find contours
		img = copy.copy(images.EditedImage)
		contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		if draw:
			cv2.drawContours(images.OriginalImage, contours, -1, (50,255,50), 3)
		return contours


	def centers(self, images, draw=True):
		# Calculate center-points
		height, width = images.OriginalImage.shape[:2]
		centers = np.zeros((height,width, 1), np.uint8)
		for contour in images.contours:
			mo = cv2.moments(contour)
			# Calculate mass-centers
			x = int(0.5+mo['m10']/mo['m00'])
			y = int(0.5+mo['m01']/mo['m00'])

			# Draw center in original image
			if draw:
				cv2.circle(images.OriginalImage, (x,y), 1, (255,50,50), 2)

			# Add center in new image/array
			centers[y][x] = [255]


		return centers

	def find_next_center(self, images, pos, draw=True):
		# FIXME läuft unschön, Punkte lassen sich teilweise schlecht auswählen
		c = None
		for i in range(0,10):
			x = y = -i

			for x in range(-i, i+1):
				if images.centers[y+pos[1]][x+pos[0]] == [255]:
					c = (x + pos[0], y + pos[1])
					break
			for y in range(-i, i+1):
				if images.centers[y+pos[1]][x+pos[0]] == [255]:
					c = (x + pos[0], y + pos[1])
					break
			for x in range(i, -i+1):
				if images.centers[y+pos[1]][x+pos[0]] == [255]:
					c = (x + pos[0], y + pos[1])
					break
			for y in range(i, -i+1):
				if images.centers[y+pos[1]][x+pos[0]] == [255]:
					c = (x + pos[0], y + pos[1])
					break

			if c is not None:
				if draw:
					cv2.circle(images.OriginalImage, c, 3, (50,50,255), 4)
				return c

		return None


	def lines(self, images, centers):
#		contours, hierarchy = cv2.findContours(centers, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#		cv2.drawContours(centers, contours, -1, (50,255,50), 3)

#		cv2.namedWindow("Oscilloscope", 1)
#		cv2.imshow("Oscilloscope", centers)
#		cv2.waitKey(0)

		#lines = cv2.HoughLinesP(centers, 30, np.pi/180 * 1, 40, minLineLength=100, maxLineGap=1000)
		lines = cv2.HoughLines(centers, 40, float(np.pi/180 * 0.5), 35)#, srn=100, stn=0)
		for line in lines:
			#for x1,y1,x2,y2 in line:
			for rho, theta in line:

				#print x1, x2, y1, y2
				#if np.tan((x2-x1)/(y2-y1)) < (np.pi/180 * 10):
				#	cv2.line(images.OriginalImage, (x1,y1), (x2,y2), (255,0,255), 2)

				#if np.abs(theta) < (np.pi/180 * 10):
				a = np.cos(theta)
				b = np.sin(theta)

				x0 = a*rho
				y0 = b*rho

				cv2.line(images.OriginalImage, (int(x0 + 10000*b + 0.5), int(y0 + 10000*a + 0.5)), (int(x0 + 10000*b + 0.5), int(y0 - 10000*a)), (255, 0, 255), 2)



	def transform(self, images, lu, ru, rd, ld):
		# Load size from osci-settings (display-resolution) (FIXME)
		height = 3 * (10*20+1)
		width  = 3 * (12*20+1)
		#images.EditedImage = np.zeros((height, width, 1), np.uint8) # Hier nicht notwendig

		# Matrix for transformed image
		dst = np.array([
			[0, 0],
			[width - 1, 0],
			[width - 1, height - 1],
			[0, height - 1]], dtype = "float32")

		# Get transformation matrix
		transmtx = cv2.getPerspectiveTransform(np.array([lu, ru, rd, ld]), dst)

		# Apply perspective transformation
		images.EditedImage = cv2.warpPerspective(images.EditedImage, transmtx, (width, height));
