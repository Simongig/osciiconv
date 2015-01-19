from osciiconv import images
from osciiconv import imgedit


img = images.Images()
imgedit = imgedit.ImageEdit()

if(img.load_image('test.jpg')):
	imgedit.process_image(img)
	img.show_original()
	img.save_edited("result.jpg")
	print "success"