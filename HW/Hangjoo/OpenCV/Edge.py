import cv2

def EdgeImage():
    src = cv2.imread("sample_image.jpg", cv2.IMREAD_COLOR)

    # 원본 이미지 그레이스케일로 변환.
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Edge 추출 방식. 참고로 멀응수에서 배움.
    Canny = cv2.Canny(src, 70, 200)
    Sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
    Laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

    # "./Result/Edge" 디렉토리에 이미지 저장.
    cv2.imwrite("./Result/Edge/Canny_image.jpg", Canny)
    cv2.imwrite("./Result/Edge/Sobel_image.jpg", Sobel)
    cv2.imwrite("./Result/Edge/Laplacian_image.jpg", Laplacian)

EdgeImage()