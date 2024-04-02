import argparse
import cv2

# 명령행 인자 파싱기를 생성합니다.
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='Lena.png', help='이미지 경로.')
params = parser.parse_args()

# 이미지를 읽어옵니다.
img = cv2.imread(params.path)
print('원본 이미지 형태:', img.shape)

# 이미지를 128x256 크기로 조절합니다.
width, height = 128, 256
resized_img = cv2.resize(img, (width, height))
print('128x256 크기로 조절한 이미지 형태:', resized_img.shape)

# 이미지를 너비의 0.25배, 높이의 0.5배로 조절합니다.
w_mult, h_mult = 0.25, 0.5
resized_img = cv2.resize(img, (0, 0), resized_img, w_mult, h_mult)
print('이미지 형태:', resized_img.shape)

# 이미지를 너비의 2배, 높이의 4배로 조절합니다.
w_mult, h_mult = 2, 4
resized_img = cv2.resize(img, (0, 0), resized_img, w_mult, h_mult, cv2.INTER_NEAREST)
print('이미지 형태:', resized_img.shape)

# 이미지를 x축을 기준으로 뒤집습니다.
img_flip_along_x = cv2.flip(img, 0)

# x축을 기준으로 뒤집은 이미지를 y축을 기준으로 뒤집습니다.
img_flip_along_x_along_y = cv2.flip(img_flip_along_x, 1)

# x축과 y축을 기준으로 동시에 뒤집은 이미지를 생성합니다.
img_flipped_xy = cv2.flip(img, -1)

# 순차적으로 x축과 y축 주변을 뒤집은 이미지와 동시에 x-y를 뒤집은 이미지가 같은지 확인합니다.
assert img_flipped_xy.all() == img_flip_along_x_along_y.all()
