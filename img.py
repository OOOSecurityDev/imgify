#!/usr/bin/env python
#----import--#
from PIL import Image
from PIL.ExifTags import TAGS
import pyfiglet

blu = '\033[34m'
yl = '\033[93m'
os.system("clear")
banner = pyfiglet.figlet_format("IMGIFY")
print (blu+banner)
print (yl+"===========================================================")
print ("""
coding <: UTF-8'
Author <: David Patrick (OOOSecurityDev)
""")
#path to the file
image_name = input(blu+"Enter the file <: ")
#read the img data using PIL
try:
	image = Image.open(image_name)
	#extracts Exif data
	exif_data = image.getexif()
	#use the TAGS dictionary from PIL.ExifTags module to map each IDs into human readable text
	#iterating overall exif_data:
	for tag_id in exif_data:
		#gets the tag name, unstead if human unreadable tag_id.
		tag = TAGS.get(tag_id, tag_id)
		data = exif_data.get(tag_id)
		#decode bytes
		if isinstance(data, bytes):
			data = data.decode()
		print (f"{blu}{tag:25} : {yl}{data}")

except Exception as e:
	print (f"Error:{yl} {e}")
