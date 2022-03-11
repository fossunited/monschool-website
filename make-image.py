"""
Script to prepare the course image to fit into mon.school.

The mon.school course images are displyed in two different sizes and often
getting cropped if not enough care is taken.

This script takes any image and generates a new image that works for both of those
sizes.

The sizes that are used in the mon school app are 348x168 and 350x200.

To make the image work for both sizes, the image is resized to 340x170 and placed
in the center of 350x200 image.
"""
from PIL import Image
import sys

im = Image.open(sys.argv[1])
im.thumbnail((340, 170))

im2 = Image.new(mode="RGBA", size=(350, 200), color=(0, 0, 0, 0))
offset = (im2.width-im.width) // 2, (im2.height-im.height)//2
im2.paste(im, offset)
im2.save("a.png")
print("saved the new image as a.png")
