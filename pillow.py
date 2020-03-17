from PIL import Image
#print('Pillow Version:', PIL.__version__)
#Version 7.0.0

# load the image
image = Image.open('images/Regular Tackles/1.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
image.show()