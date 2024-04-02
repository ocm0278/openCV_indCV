import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread('Lena.png', 0)

# Apply Otsu's thresholding to obtain a binary image
_, binary = cv2.threshold(image, -1, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Perform morphological erosion with a 3x3 kernel, repeated 10 times
eroded = cv2.morphologyEx(binary, cv2.MORPH_ERODE, (3, 3), iterations=10)

# Perform morphological dilation with a 3x3 kernel, repeated 10 times
dilated = cv2.morphologyEx(binary, cv2.MORPH_DILATE, (3, 3), iterations=10)

# Perform morphological opening with a 5x5 elliptical kernel, repeated 5 times
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=5)

# Perform morphological closing with a 5x5 elliptical kernel, repeated 5 times
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=5)

# Perform morphological gradient with a 5x5 elliptical kernel
grad = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))

# Plotting the images
plt.figure(figsize=(10, 10))

# Plot the original binary image
plt.subplot(231)
plt.axis('off')
plt.title('binary')
plt.imshow(binary, cmap='gray')

# Plot the eroded image
plt.subplot(232)
plt.axis('off')
plt.title('eroded 10 times')
plt.imshow(eroded, cmap='gray')

# Plot the dilated image
plt.subplot(233)
plt.axis('off')
plt.title('dilate 10 times')
plt.imshow(dilated, cmap='gray')

# Plot the opened image
plt.subplot(234)
plt.axis('off')
plt.title('open 5 times')
plt.imshow(opened, cmap='gray')

# Plot the closed image
plt.subplot(235)
plt.axis('off')
plt.title('close 5 times')
plt.imshow(closed, cmap='gray')

# Plot the gradient image
plt.subplot(236)
plt.axis('off')
plt.title('gradient')
plt.imshow(grad, cmap='gray')

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
