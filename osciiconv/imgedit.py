# coding=UTF-8

import cv2
import cv2.cv as cv
import numpy as np

import images

class ImageEdit:
	"""To edit the original image for better image processing"""

	def process_image(self, images):
		self.thresholding(images)
		#self.centers(images)
		self.lines(images, self.centers(images))


	def thresholding(self, images):
		ret, images.EditedImage = cv2.threshold(images.EditedImage, 170, 255, cv2.THRESH_BINARY)


	def centers(self, images):
		# Find contours
		contours, hierarchy = cv2.findContours(images.EditedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(images.OriginalImage, contours, -1, (50,255,50), 3)

		# Calculate center-points
		height, width = images.OriginalImage.shape[:2]
		centers = np.zeros((height,width, 1), np.uint8)
		for contour in contours:
			mo = cv2.moments(contour)
			# Calculate mass-centers
			x = int(0.5+mo['m10']/mo['m00'])
			y = int(0.5+mo['m01']/mo['m00'])

			# Draw center in original image
			cv2.circle(images.OriginalImage, (x,y), 1, (50,50,255), 2)

			# Add center in new image/array
			centers[y][x] = [255]

		return centers


	def lines(self, images, centers):

		cv2.namedWindow("Oscilloscope", 1)
		cv2.imshow("Oscilloscope", centers)
		cv2.waitKey(0)

		lines = cv2.HoughLines(centers,1,np.pi/180,200)
		for rho,theta in lines:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + 1000*(-b))
			y1 = int(y0 + 1000*(a))
			x2 = int(x0 - 1000*(-b))
			y2 = int(y0 - 1000*(a))

			cv2.line(images.OriginalImage, (x1,y1), (x2,y2), (0,0,255), 2)


	def transform(self, images):
		a = None