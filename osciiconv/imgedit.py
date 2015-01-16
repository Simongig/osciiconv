# coding=UTF-8

import cv2
import cv2.cv as cv
import numpy as np

class ImageEdit:
	"""To edit the original image for better image processing"""

	def thresholding(self, image):
		ret, image = cv2.threshold(image, 170, 255, cv2.THRESH_BINARY)

		return image

	def lines(self, image):
		#self.OriginalImage = cv2.cvtColor(self.OriginalImage,cv2.COLOR_GRAY2BGR)

		edges = cv2.Canny(image, 50, 150, apertureSize = 3)
		points = cv2.HoughCircles(image,cv.CV_HOUGH_GRADIENT,100,10, param1=20,param2=20)
		#points = np.uint16(np.around(points))
		points = cv2.HoughCircles(image,cv2.cv.CV_HOUGH_GRADIENT,1,75,param1=50,param2=10,minRadius=0,maxRadius=50)

		self.OriginalImage = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)

		print np.size(points)
		for i in points[0,:]:
			# draw the outer circle
			cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
			# draw the center of the circle
			cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)

		lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
		for rho,theta in lines[0]:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + 1000*(-b))
			y1 = int(y0 + 1000*(a))
			x2 = int(x0 - 1000*(-b))
			y2 = int(y0 - 1000*(a))

			cv2.line(self.OriginalImage,(x1,y1),(x2,y2),(0,0,127),2)

			return image