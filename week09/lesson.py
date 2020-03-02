import cv2
import numpy as np
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (128, 128, 128)
RED   = (0, 0, 255)
GREEN = (0, 255, 0)


def set_pixel(image, pt, color):
	""" Not much, but it is the bases of graphics """
	image[pt[0], pt[1]] = color


# ------------------------------------------------------------------------------------------
def draw_line(image, pt1, pt2, color):
	"""
	draw_line() will draw a line between pt1 and pt2
	pt1 and pt2 are tuples (x, y) (ie., (10, 23))
	"""

	# TODO -> Add your line drawing code here

	# Sample code to draw white dots at pt1 and pt2 positions
	set_pixel(image, pt1, color)
	set_pixel(image, pt2, color)



def main():
	# Create 8-bit image to draw one
	img = np.zeros((400, 400, 3), dtype=np.uint8)

	# Test one
	draw_line(img, (100, 100), (300, 300), WHITE)

	# Test two
	# draw_line(img, (300, 100), (100, 300), RED)

	# Test three
	# draw_line(img, (random.randint(0, 400), random.randint(0, 400)), (random.randint(0, 400), random.randint(0, 400)), GREEN)

	cv2.imshow('final drawing', img)
	cv2.waitKey(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()