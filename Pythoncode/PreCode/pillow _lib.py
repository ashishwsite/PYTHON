# PILLOW LIBERARY IS PHYTHON LIBERY WHICH HELP IN DIGIAL IMAGE PROCEESING 
# SOME OTHER IMAGE LIBRARY IS SKLERN
# 3 PILLOW HELP IN  image processing tasks, such as opening, manipulating, and saving various image file formats.
# 4 IN PILLOW LIBERAY MANY MODULE IS PRESENT 
# # PIL IS MODULE HELP IN OPENING THE IMAGE 
# MODULE ME SE METHOD KO IMPORT KARKE CLASS KI TARAH USED KARTE HAI (.)DOT OPERATOR KI TARAH KI JSE
# 5 PNG format OF Image IS HIGH QUALITY AND LOSSLESS Image
# 6 OPEN() METHOD return AN object
# RESIZE() METHOD IS HELPFULL IN RESIZEING THE IMAGE 
# 7 PIXCELVALUE () IS METHOD WHICH return THE  VALUE OF IMAGE PIXCEL
# 8 CONVERT METHOD IS USED TO CONVERT IMAGE INTO GREYVALU
from PIL import Image

# Open an image file
image = Image.open("download.jpeg")
print("Image format:", image.format)
print("Image size:", image.size)

# Show the image
image.show()

# Save a copy of the image
# image.save("copy.jpg")

# Close the image file
# image.close()
