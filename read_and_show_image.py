import cv2
import numpy as np

img = cv2.imread('Rose1.png')

# print the image properties
# print(img)
print(img.shape)
print(img.size)
print(type(img))

# show the image
cv2.imshow('image', img)
cv2.waitKey(0)

