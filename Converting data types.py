import cv2
import numpy as np

# Read the image
image = cv2.imread('Lena.png')

# Print the shape and data type of the image
print('Shape:', image.shape)
print('Data type:', image.dtype)

# Display the original image
cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

# Convert the data type of the image to float32 and normalize it
image = image.astype(np.float32) / 255
print("Shape:", image.shape)
print('Data type:', image.dtype)

# Display the image (multiply by 2 and clip between 0 and 1)
cv2.imshow('image', np.clip(image*2, 0, 1))
cv2.waitKey()
cv2.destroyAllWindows()

# Convert the data type of the image back to uint8 and scale it back to 0-255
image = (image * 255).astype(np.uint8)
print('Shape:', image.shape)
print('Data type:', image.dtype)

# Display the final image
cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()
