import sys, cv2
import numpy as np

# 그레이스케일 영상 불러오기
src = cv2.imread('images_ch06/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed'); sys.exit()

dst = np.clip(src + 100, 0, 255)   # 0~255

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()