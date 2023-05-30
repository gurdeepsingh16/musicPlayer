# importing the libraries
import cv2
import numpy as np

# creating an array using np.full
# 255 is code for white color
array_created = np.full((500, 500, 3),
						255, dtype = np.uint8)

# displaying the image
cv2.imshow("image", array_created)
