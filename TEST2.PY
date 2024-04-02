import cv2
image_path='Lena.png'
image =cv2.imread(image_path,cv2.IMREAD_COLOR)
cv2.imshow('COlOr',image)
cv2.waitKey(0)
cv2.destroyAllWindows()