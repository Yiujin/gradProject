import cv2
import numpy as np

def blurMovie():
    src = cv2.imread("sample_image.jpg", cv2.IMREAD_COLOR)

    # 세로, 가로, 채널 값 추출.
    height, width, channel = src.shape
    # 코덱 설정.
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    # 프레임 설정.
    fps = 20

    # 동영상을 저장하는 객체 생성.
    Movie = cv2.VideoWriter("./Result/Blur/Blur_Moive.avi", fcc, fps, (width, height))

    # 블러 처리.
    for i in range(1, 300):
        # 블러 처리 정도.
        k = int((-20/(150**2))*(i-150)+20)
        dst = cv2.blur(src, (k, k), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
        Movie.write(dst)
        print(i,"/300")

    print("Success.")


blurMovie()