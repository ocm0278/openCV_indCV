import argparse
import cv2

# Define and parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='Lena.png', help='Image path')
params = parser.parse_args()

# Read the image
img = cv2.imread(params.path)

#Check if image was successfully read.
assert img is not None

print('read {}'.format(params.path))
print('shape:', img.shape)
print('dtype:',img.dtype)

# Convert the image to grayscale
img = cv2.imread(params.path, cv2.IMREAD_GRAYSCALE)

# Check if the grayscale image was successfully generated
assert img is not None

print('read {} as grayscale'.format(params.path))
print('shape:', img.shape)
print('dtype:', img.dtype)