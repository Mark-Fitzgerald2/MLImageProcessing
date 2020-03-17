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

"""
from matplotlib import image
from matplotlib import pyplot

#load image as pixel array 
data = image.imread('images/Regular Tackles/1.jpg')

#summarise shape of the pixel array
print(data.dtype)
print(data.shape)

#display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()
"""


#load an image and convert to and from NumPy array

from numpy import asarray
#load the image
image = Image.open('images/Regular Tackles/1.jpg')
#summarise image details
print("Image 1")
print(image.format)
print(image.mode)
print(image.size)
#convert image to numpy array
data = asarray(image)
#summarise shape
print(data.shape)
#create Pillow image
image2 = Image.fromarray(data)
#summarise image details
print(image2.format)
print(image2.mode)
print(image2.size)
#show the image
image2.show()
#save the image
#image2.save("my_file.jpeg")