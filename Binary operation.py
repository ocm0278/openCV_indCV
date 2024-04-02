import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a blank image for the circle
circle_image = np.zeros((500,500), np.uint8)
# Draw a filled white circle in the center of the image
cv2.circle(circle_image, (250,250), 100, 255, -1)

# Create a blank image for the rectangle
rect_image = np.zeros((500,500), np.uint8)
# Draw a filled white rectangle
cv2.rectangle(rect_image, (100,100), (400,250), 255, -1)

# Perform bitwise AND operation between the circle and rectangle images
circle_and_rect_image = circle_image & rect_image
# Perform bitwise OR operation between the circle and rectangle images
circle_or_rect_image = circle_image | rect_image

# Plotting the images using Matplotlib
plt.figure(figsize=(10,10))

# Plot the circle image
plt.subplot(221)
plt.axis('off')
plt.title('circle')
plt.imshow(circle_image, cmap='gray')

# Plot the rectangle image
plt.subplot(222)
plt.axis('off')
plt.title('rectangle')
plt.imshow(rect_image, cmap='gray')

# Plot the result of bitwise AND operation
plt.subplot(223)
plt.axis('off')
plt.title('circle & rectangle')
plt.imshow(circle_and_rect_image, cmap='gray')

# Plot the result of bitwise OR operation
plt.subplot(224)
plt.axis('off')
plt.title('circle | rectangle')
plt.imshow(circle_or_rect_image, cmap='gray')

# Adjust layout for better visualization
plt.tight_layout(True)
# Show the plots
plt.show()
