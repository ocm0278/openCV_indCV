import cv2, numpy as np

# Create a named window
cv2.namedWindow('window')

# Initialize fill value with white color (255, 255, 255)
fill_val = np.array([255, 255, 255], np.uint8)


# Define a trackbar callback function to update fill_val based on trackbar position
def trackbar_callback(idx, value):
    fill_val[idx] = value
    
# Create trackbars for adjusting R, G, and B values    
cv2.createTrackbar('R', 'window', 255, 255, lambda v: trackbar_callback(2, v))
cv2.createTrackbar('G', 'window', 255, 255, lambda v: trackbar_callback(1, v))
cv2.createTrackbar('B', 'window', 255, 255, lambda v: trackbar_callback(0, v))


# Main loop to update the image based on trackbar values
while True:
    # Create an image filled with the current fill value
    image = np.full((500, 500, 3), fill_val)
    
    # Display the image in the window
    cv2.imshow('window', image)
    
     # Wait for a key press for 3 milliseconds
    key = cv2.waitKey(3)
    
    # If the key pressed is 'Esc' (27), exit the loop
    if key == 27:
        break
    
# Destroy all OpenCV windows
cv2.destroyAllWindows()
