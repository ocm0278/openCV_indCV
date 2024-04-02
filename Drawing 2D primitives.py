import argparse
import cv2, random

# Argument parser to take command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='Lena.png', help='Image path.')
params = parser.parse_args()

# Read the image specified by the path
image = cv2.imread(params.path)

# Get width and height of the image
w, h = image.shape[1], image.shape[0]


# Function to generate a random point within the image boundaries
def rand_pt(mult=1.):
    return (random.randrange(int(w * mult)),
            random.randrange(int(h * mult)))
    
# Draw various shapes and text on the image
cv2.circle(image, rand_pt(), 40, (255,0,0))  # Draw a blue circle
cv2.circle(image, rand_pt(), 5, (255, 0, 0), cv2.FILLED)  # Draw a filled blue circle
cv2.circle(image, rand_pt(),40, (255, 85, 85), 2) # Draw a circle with a specific thickness and color
cv2.circle(image, rand_pt(), 40, (255,170,170),2,cv2.LINE_AA) # Draw an anti-aliased circle
cv2.line(image, rand_pt(), rand_pt(), (0, 255, 0))  # Draw a green line
cv2.line(image, rand_pt(), rand_pt(), (85, 255,85),3) # Draw a thick green line
cv2.line(image, rand_pt(),rand_pt(), (170,255,170),3,cv2.LINE_AA) # Draw an anti-aliased green line
cv2.arrowedLine(image, rand_pt(), rand_pt(),(0,0,255),3,cv2.LINE_AA) # Draw a red arrowed line
cv2.rectangle(image, rand_pt(),rand_pt(),(255,255,0),3)# Draw a yellow rectangle
cv2.ellipse(image, rand_pt(), rand_pt(0.3), random.randrange(360), 0, 360, (255, 255, 255),3) # Draw a white ellipse
cv2.putText(image,'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX ,1,(0,0,0),3)# Add OpenCV text

# Display the resulting image
cv2.imshow("result", image)
# Wait for a key press
key = cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()