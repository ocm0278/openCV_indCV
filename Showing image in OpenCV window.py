import argparse
import cv2

# Argument parser to take command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='Lena.png', help='Image path.')
parser.add_argument('--iter', default=50, help='Downsampling-upsampling iterations number.')
params = parser.parse_args()

# Read the original image
orig =cv2.imread(params.path)
orig_size = orig.shape[0:2]


# Display the original image
cv2.imshow("Original image", orig)
cv2.waitKey(2000)

# Perform downsampling and upsampling iterations
resized = orig

for i in range(params.iter):
    resized =cv2.resize(cv2.resize(resized,(256, 256)), orig_size)
    cv2.imshow("downsized&restored",resized)
    cv2.waitKey(100)  # Wait for 100 milliseconds
    
cv2.destroyWindow("downsized&restroed") # Destroy the downsized and restored image window


# Create named windows for original and result images
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("result")

# Display original and result images
cv2.imshow("original", orig)
cv2.imshow("result",resized)
cv2.waitKey(0) # Wait indefinitely until a key is pressed

cv2.destroyAllWindows() # Close all OpenCV windows