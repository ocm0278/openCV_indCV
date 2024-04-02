import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (assuming it's named 'Lena.png') in grayscale mode
image = cv2.imread('Lena.png', 0)

# Compute the gradients using Sobel operator along x and y directions
dx = cv2.Sobel(image, cv2.CV_32F, 1, 0)  # Gradient along x-direction
dy = cv2.Sobel(image, cv2.CV_32F, 0, 1)  # Gradient along y-direction

# Plotting the original image and its gradients using Matplotlib
plt.figure(figsize=(8, 3))

# Plot the original image
plt.subplot(131)
plt.axis('off')
plt.title('image')
plt.imshow(image, cmap='gray')

# Plot the gradient along x-direction
plt.subplot(132)
plt.axis('off')
plt.imshow(dx, cmap='gray')
plt.title(r'$\frac{dI}{dx}$')  # LaTeX expression for dI/dx

# Plot the gradient along y-direction
plt.subplot(133)
plt.axis('off')
plt.title(r'$\frac{dI}{dy}$')  # LaTeX expression for dI/dy
plt.imshow(dy, cmap='gray')

# Adjust layout for better visualization
plt.tight_layout()
# Show the plots
plt.show()
