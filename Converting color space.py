import cv2
import numpy as np

# Read the image and normalize pixel values to range [0, 1]
image = cv2.imread('Lena.png').astype(np.float32) / 255
print('Shape:', image.shape)
print('Data type:', image.dtype)

# Display the original image
cv2.imshow('original image', image)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print('Converted to grayscale')
print('Shape:', gray.shape)
print('Data type:', gray.dtype)
cv2.imshow('gray-scale image', gray)

# Convert the image to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print('Converted to HSV')
print('Shape:', hsv.shape)
print('Data type:', hsv.dtype)

# Increase the brightness of the V channel (Value) in HSV
hsv[:, :, 2] *= 2

# Convert the image back to BGR from HSV
from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
print('Converted back to BGR from HSV')
print('Shape:', from_hsv.shape)
print('Data type:', from_hsv.dtype)
cv2.imshow('from HSV to BGR', from_hsv)

cv2.waitKey()
cv2.destroyAllWindows()
