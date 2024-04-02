import math  # Importing the math module for mathematical operations
import cv2  # Importing OpenCV library for image processing
import numpy as np  # Importing numpy for numerical operations
import matplotlib.pyplot as plt  # Importing matplotlib for visualization

# Read the image 'Lena.png' in grayscale and convert pixel values to float32 in the range [0, 1]
image = cv2.imread('Lena.png', 0).astype(np.float32) / 255

# Create a Gabor kernel with specified parameters
kernel = cv2.getGaborKernel((21, 21), 5, 1, 10, 1, 0, cv2.CV_32F)

# Normalize the kernel to have unit length in its vector representation
kernel /= math.sqrt((kernel * kernel).sum())

# Apply the Gabor filter to the image using cv2.filter2D
filtered = cv2.filter2D(image, -1, kernel)

# Visualize the original image, Gabor kernel, and filtered image
plt.figure(figsize=(8, 3))

# Subplot 1: Original image
plt.subplot(131)
plt.axis('off')
plt.title('image')
plt.imshow(image, cmap='gray')

# Subplot 2: Gabor kernel
plt.subplot(132)
plt.title('kernel')
plt.imshow(kernel, cmap='gray')

# Subplot 3: Filtered image
plt.subplot(133)
plt.axis('off')
plt.title('filtered')
plt.imshow(filtered, cmap='gray')

# Adjust layout for better visualization
plt.tight_layout()

# Display the plots
plt.show()
