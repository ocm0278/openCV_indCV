import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lena.png 이미지를 grayscale로 읽어와서 [0, 1] 범위로 변환
image = cv2.imread('Lena.png', 0).astype(np.float32) / 255

# 2D 이미지에 대한 디스크리트 푸리에 변환 수행
fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

# 주파수 도메인에서 0Hz가 중앙에 위치하도록 FFT를 이동
fft_shift = np.fft.fftshift(fft, axes=[0, 1])

# 고주파 성분을 제거하기 위한 마스크 생성
sz = 25  # 마스크 크기
mask = np.zeros(fft.shape, np.uint8)
mask[image.shape[0]//2-sz:image.shape[0]//2+sz,
     image.shape[1]//2-sz:image.shape[1]//2+sz, :] = 1

# 마스크를 사용하여 고주파 성분을 제거
fft_shift *= mask

# 역으로 FFT 이동
fft = np.fft.ifftshift(fft_shift, axes=[0, 1])

# 역 디스크리트 푸리에 변환을 수행하여 필터링된 이미지 생성
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

# 마스크 이미지를 새로운 채널에 추가하여 컬러 이미지로 변환
mask_new = np.dstack((mask, np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)))

# 결과를 시각화하기 위한 subplot 설정
plt.figure()
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')

plt.subplot(132)
plt.axis('off')
plt.title('no high frequencies')
plt.imshow(filtered, cmap='gray')

plt.subplot(133)
plt.axis('off')
plt.title('mask')
plt.imshow(mask_new*255, cmap='gray')

plt.tight_layout(True)
plt.show()
