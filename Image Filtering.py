import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and normalize pixel values to the range [0, 1]
image = cv2.imread('Lena.png').astype(np.float32) / 255

# Add Gaussian noise to the image
noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0, 1)

# Display the noisy image
plt.imshow(noised[:, :, [2, 1, 0]])
plt.title('Noisy Image')
plt.show()

# Apply Gaussian blur to the noisy image
gauss_blur = cv2.GaussianBlur(noised, (7, 7), 0)

# Display the image after Gaussian blur
plt.imshow(gauss_blur[:, :, [2, 1, 0]])
plt.title('Gaussian Blur')
plt.show()

# Apply median blur to the noisy image
median_blur = cv2.medianBlur((noised * 255).astype(np.uint8), 7)

# Display the image after median blur
plt.imshow(median_blur[:, :, [2, 1, 0]])
plt.title('Median Blur')
plt.show()

# Apply bilateral filter to the noisy image
bilat = cv2.bilateralFilter(noised, -1, 0.3, 10)

# Display the image after bilateral filter
plt.imshow(bilat[:, :, [2, 1, 0]])
plt.title('Bilateral Filter')
plt.show()
