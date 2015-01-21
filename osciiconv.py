from osciiconv import ImageEdit
from osciiconv import Images

import numpy as np


def main():
	img = Images()
	imgedit = ImageEdit()

	if(img.load_image('test.jpg')):
		img.show_image(img.OriginalImage, False)
		imgedit.process_image(img)
		img.show_image(img.OriginalImage, False, True)

		rect = get_rect(img, imgedit)
		imgedit.transform(img, rect[0],rect[1],rect[2],rect[3])
		img.show_image(img.EditedImage)

		img.save_image(img.EditedImage, "result.jpg")

		img.close_windows()
		print "success"


def get_rect(img, imgedit):
	rect = np.zeros((4, 2), dtype = "float32")
	i = 0
	while i < 4:
		pos = imgedit.find_next_center(img, img.get_coordinate(), True)
		if pos is not None:
			rect[i] = pos
			img.show_image(img.OriginalImage, False)
			i += 1

	# Sort ..

	return rect


if __name__ == '__main__':
	main()
