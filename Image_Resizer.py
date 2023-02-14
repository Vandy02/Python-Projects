# install pillow
# import pillow
# open up the image you want to resize
# print current sie of image
# specify the size you want to change it to
# save the new resized image

from PIL import Image

image = Image.open('qrimg.png')

print(f"Current Size: {image.size}")

resized_image = image.resize((500, 500))

resized_image.save('facebook.jpeg')