"""
Utility to prepare the course image to fit into mon.school.

The mon.school course images are displyed in two different sizes and often
getting cropped if not enough care is taken.

The `prepare_image` function takes any image and generates a new image that works for both of those
sizes.

The sizes that are used in the mon school app are 348x168 and 350x200.

To make the image work for both sizes, the image is resized to 340x170 and placed
in the center of 350x200 image.
"""
from PIL import Image
import sys

def prepare_image(source_path, dest_path):
    """Takes the image provides at the `source_path` and resizes it as suitable for
    mon.school and saves it to the `dest_path`."""
    # resize the given image to 340x170
    im = Image.open(source_path)
    im.thumbnail((340, 170))

    # and paste it in the center of a 350x200 image
    im2 = Image.new(mode="RGBA", size=(350, 200), color=(0, 0, 0, 0))
    offset = (im2.width-im.width) // 2, (im2.height-im.height)//2
    im2.paste(im, offset)
    im2.save(dest_path)
    print("created", dest_path)
