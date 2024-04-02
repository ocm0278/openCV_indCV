import argparse
import cv2, numpy as np, random

# Argument parser to take command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='Lena.png', help='Image path.')
params = parser.parse_args()

# Read the image specified by the path
image = cv2.imread(params.path)

# Create a copy of the original image for display
image_to_show = np.copy(image)

# Get width and height of the image
w, h = image.shape[1], image.shape[0]

# Function to generate a random point within the image boundaries
def rand_pt():
    return (random.randrange(w),
            random.randrange(h))
    
# Initialize the finish flag to False
finish = False

# Main loop to handle user input and draw on the image
while not finish:
    # Display the current image
    cv2.imshow("result", image_to_show)
    
    # Wait for a key press
    key = cv2.waitKey(0)
    
    # If the key pressed is 'p', draw circles at random points
    if key == ord('p'):
        for pt in [rand_pt() for _ in range(10)]:
            cv2.circle(image_to_show, pt, 3, (255, 0, 0), -1)
            
     # If the key pressed is 'l', draw a line between two random points
    elif key == ord('l'):
        cv2.line(image_to_show, rand_pt(), rand_pt(), (0, 255, 0),3)
        
    # If the key pressed is 'r', draw a rectangle with random points as vertices
    elif key == ord('r'):
        cv2.rectangle(image_to_show, rand_pt(), rand_pt(), (0,0,255),3)
        
     # If the key pressed is 'e', draw an ellipse with random center, axes, and rotation angle
    elif key == ord('e'):
        cv2.ellipse(image_to_show, rand_pt(), rand_pt(), random.randrange(360), 0, 360, (255, 255,0),3)
        
    # If the key pressed is 't', add text at a random position
    elif key == ord('t'):
        cv2.putText(image_to_show, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),3)
        
    # If the key pressed is 'c', reset the image to the original
    elif key == ord('c'):
        image_to_show = np.copy(image)
        
     # If the key pressed is 'Esc' (27), set the finish flag to True to exit the loop
    elif key == 27:
        finish = True
    