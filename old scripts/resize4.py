"""
Run this script from a folder with image files to resize them all to a desired width.
Set 'DESIRED_WIDTH' to choose output images width (height will be calculated automatically to preserve ratio).
Set 'ROTATION' to optionally rotate image before resizing.
Set 'EXTENSIONS' to change what type of files to process.
Note: requires PIL package.
"""
import os
from PIL import Image
import shutil

# the output width of all images
DESIRED_WIDTH = 1000
ROTATION = 0

# list of extensions to process
EXTENSIONS = ['.jpg', '.png', '.bmp']

# recreate the output folder
if os.path.exists("output"):
	shutil.rmtree("output")
os.mkdir("output")			

def process_image(filename, desired_width, rotation):
	"""
	Resize and rotate a single image
	"""
	img = Image.open(filename)
	
	# apply rotation
	if rotation:
		img = img.rotate(rotation, expand=True)
	
	# resize to desired width
	wpercent = (desired_width / float(img.size[0]))
	height = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((desired_width, height), Image.ANTIALIAS)
	
	# save output image
	img.save(os.path.join('output', file))


# iterate all images in folder and process them
for files in os.walk('.'):
	for file in files[2]:
		if os.path.splitext(file)[1].lower() in EXTENSIONS:
			print(file)
			process_image(file, DESIRED_WIDTH, ROTATION)