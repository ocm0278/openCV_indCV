import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
grey = cv2.imread('Lena.png', 0)

# Display the original grayscale image
cv2.imshow('original grey', grey)
cv2.waitKey()

# Calculate histogram of the grayscale image
hist, bins = np.histogram(grey, 256, [0, 255])

# Plot the histogram
plt.fill(hist)
plt.xlabel('pixel value')
plt.show()

# Equalize the histogram of the grayscale image
grey_eq = cv2.equalizeHist(grey)

# Calculate histogram of the equalized grayscale image
hist, bins = np.histogram(grey_eq, 256, [0, 255])

# Plot the histogram of the equalized grayscale image
plt.fill_between(range(256), hist, 0)
plt.xlabel('pixel value')
plt.show()

# Display the equalized grayscale image
cv2.imshow('equalized grey', grey_eq)
cv2.waitKey()

# Load the color image
color = cv2.imread('Lena.png')

# Convert color image to HSV color space
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# Equalize the histogram of the value channel in HSV
hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])

# Convert the equalized HSV image back to BGR color space
color_eq = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Display the original color image
cv2.imshow('original color', color)

# Display the equalized color image
cv2.imshow('equalized color', color_eq)
cv2.waitKey()
cv2.destroyAllWindows()
