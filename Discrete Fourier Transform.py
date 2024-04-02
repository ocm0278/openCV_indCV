import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (assuming it's named 'Lena.png') in grayscale mode and normalize it
image = cv2.imread('Lena.png', 0).astype(np.float32) / 255

# Perform Discrete Fourier Transform (DFT) on the image
fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift the zero frequency component to the center
shifted = np.fft.fftshift(fft, axes=[0, 1])

# Calculate the magnitude spectrum and take the logarithm for visualization
magnitude = cv2.magnitude(shifted[:, :, 0], shifted[:, :, 1])
magnitude = np.log(magnitude)

# Plot the magnitude spectrum
plt.axis('off')
plt.imshow(magnitude, cmap='gray')
plt.tight_layout(True)
plt.show()

# Perform Inverse Discrete Fourier Transform (IDFT) to restore the image
restored = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

# Display the restored image
cv2.imshow('restored', restored)
cv2.waitKey()
cv2.destroyAllWindows()
