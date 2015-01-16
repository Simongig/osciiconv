from osciiconv import images
from osciiconv import imgedit


img = images.Images()
imgedit = imgedit.ImageEdit()

if(img.load_image('test.jpg')):
	img.OriginalImage = imgedit.thresholding(img.OriginalImage)
	img.OriginalImage = imgedit.lines(img.OriginalImage)
	img.show_edited()
	print "success"