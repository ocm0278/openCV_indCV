import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 파일 경로
image_path = 'Lena.png'

# 이미지 불러오기
image = cv2.imread(image_path,cv2.COLOR_BGR2RGB)

cv2.imshow('Image', image)
    
    # 사용자가 아무 키나 누를 때까지 대기
cv2.waitKey(0)
    
    # 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
grey_eq = cv2.equalizeHist(image)
# Calculate histogram of the grayscale image
hist, bins = np.histogram(grey_eq, 256, [0,255])

# Plot the histogram
plt.fill(hist)
plt.xlabel('pixel value')
plt.show()

grey_eq = cv2.equalizeHist(image)

# 평활화된 그레이스케일 이미지의 히스토그램 계산
hist, bins = np.histogram(grey_eq, 256, [0, 255])

# 평활화된 그레이스케일 이미지의 히스토그램 그리기
plt.fill_between(range(256), hist, 0)
plt.xlabel('픽셀 값')
plt.show()