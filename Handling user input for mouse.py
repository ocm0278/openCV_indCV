import argparse
import cv2
import numpy as np

# 명령행 인자를 받기 위한 Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='Lena.png', help='Image path.')  # 입력 이미지의 경로
params = parser.parse_args()

# 지정된 경로의 이미지 읽기
image = cv2.imread(params.path)
image_to_show = np.copy(image)

# 마우스 이벤트와 좌표를 추적하기 위한 전역 변수
mouse_pressed = False 
s_x = s_y = e_x = e_y = -1

# 마우스 이벤트를 처리하는 콜백 함수
def mouse_callback(event, x, y, flags, param):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed
    
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 누름 이벤트
        mouse_pressed = True
        s_x, s_y = x, y  # 시작 좌표 설정
        image_to_show = np.copy(image)  # 원본 이미지의 복사본 생성
        
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동 이벤트
        if mouse_pressed:  # 마우스 버튼이 눌린 경우
            image_to_show = np.copy(image)  # 원본 이미지의 복사본 생성
            cv2.rectangle(image_to_show, (s_x, s_y), (x, y), (0, 255, 0), 1)  # 사각형 그리기
    
    elif event == cv2.EVENT_LBUTTONUP:  # 왼쪽 마우스 버튼 놓음 이벤트
        mouse_pressed = False
        e_x, e_y = x, y  # 끝 좌표 설정

# 창 생성 및 마우스 콜백 함수 설정
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

# 이미지 표시 및 키보드 이벤트 처리를 위한 메인 루프
while True:
    cv2.imshow('image', image_to_show)
    k = cv2.waitKey(1)
    
    if k == ord('c'):  # 'c' 키가 눌린 경우
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        if s_x > e_x:
            s_x, e_x = e_x, s_x
            
        if e_y - s_y > 1 and e_x - s_x > 0:  # 너비와 높이가 0보다 큰지 확인
            image = image[s_y:e_y, s_x:e_x]  # 이미지 자르기
            image_to_show = np.copy(image)  # 표시할 이미지 업데이트
            
    elif k == 27:  # 'Esc' 키가 눌린 경우
        break  # 루프 종료
    
# 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
