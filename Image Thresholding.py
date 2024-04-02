import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Load the image (assuming it's named 'Lena.png')
image = cv2.imread('Lena.png')

# Define the kernel size and alpha value for the Gaussian filter
KSIZE = 11
ALPHA = 2

# Generate the Gaussian kernel
kernel = cv2.getGaussianKernel(KSIZE, 0)
# Modify the kernel to implement the Laplacian of Gaussian (LoG) filter
kernel = -ALPHA * kernel @ kernel.T
kernel[KSIZE//2, KSIZE//2] += 1 + ALPHA

# Print kernel information for verification
print(kernel.shape, kernel.dtype, kernel.sum())

# Apply the filter to the image using filter2D function
filtered = cv2.filter2D(image, -1, kernel)

# Plot the original and filtered images using Matplotlib
plt.figure(figsize=(8, 4))

# Plot the original image
plt.subplot(121)
plt.axis('off')
plt.title('image')
plt.imshow(image[:,:,[2,1,0]])

# Plot the filtered image
plt.subplot(122)
plt.axis('off')
plt.title('filtered')
plt.imshow(filtered[:,:,[2,1,0]])

# Adjust layout for better visualization
plt.tight_layout(True)
# Show the plots
plt.show()

# Display the original and filtered images using OpenCV
cv2.imshow('before', image)
cv2.imshow('after', filtered)
cv2.waitKey()
cv2.destroyAllWindows()
