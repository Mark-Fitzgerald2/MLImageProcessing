from PIL import Image
#print('Pillow Version:', PIL.__version__)
#Version 7.0.0


#Print details of an image

"""
# load the image
image = Image.open('images/Regular Tackles/1.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
image.show()
"""


#load and display an image with Matplotlib


from matplotlib import image
from matplotlib import pyplot

#load image as pixel array 
data = image.imread('images/Regular Tackles/1.jpg')

#summarize shape of the pixel array
print(data.dtype)
print(data.shape)

#display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()