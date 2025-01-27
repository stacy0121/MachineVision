import cv2
import matplotlib.pyplot as plt

# 컬러 영상과 그레이스케일 영상 출력
imgBGR = cv2.imread('images_ch06/lenna.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread('images_ch06/lenna.bmp', cv2.IMREAD_GRAYSCALE)

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')   # 1행 2열로
plt.show()