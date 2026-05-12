import cv2
import numpy as np

# read the image
img = cv2.imread('Rose2.png')

# convert the image rgb to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# save the image
cv2.imwrite('Rose2_gray.png', img_gray)

# print the image properties
print(img_gray.shape)
print(img_gray.size)
print(type(img_gray))

# show the image
cv2.imshow('image', img_gray)
cv2.waitKey(0)

