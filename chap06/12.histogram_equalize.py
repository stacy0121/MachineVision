import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]   # 한 계급 너비

    for i, h in enumerate(hist):
        x = int(round(i*gap))               # 막대 사각형 시작 x 좌표
        w = int(round(gap))                 # 막대 사각형 가로 길이
        roi = (x, 0, w, int(h))
        cv2.rectangle(hist_img, roi, 0, cv2.FILLED)
        print(h)
    return cv2.flip(hist_img, 0)            # x축 반전

image = cv2.imread("images_ch06/buildings.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

bins, ranges = [256], [0, 256]
hist = cv2.calcHist([image], [0], None, bins, ranges)        # 히스토그램 계산

# 히스토그램 누적 계산
accum_hist = np.zeros(hist.shape[:2], np.float32)
accum_hist[0] = hist[0]
for i in range(1, hist.shape[0]):
    accum_hist[i] = accum_hist[i-1] + hist[i]

accum_hist = (accum_hist / sum(hist)) * 255                  # 누적합의 정규화
dst1 = [[accum_hist[val] for val in row] for row in image]   # 화소값 할당
dst1 = np.array(dst1, np.uint8)

dst2 = cv2.equalizeHist(image)                               # OpenCV 히스토그램 평활화
hist1 = cv2.calcHist([dst1], [0], None, bins, ranges)        # 히스토그램 계산
hist2 = cv2.calcHist([dst2], [0], None, bins, ranges)
hist_img = draw_histo(hist)
hist_img1 = draw_histo(hist1)
hist_img2 = draw_histo(hist2)

cv2.imshow("image", image);       cv2.imshow("hist_img", hist_img)
cv2.imshow("dst1_User", dst1);    cv2.imshow("User_hist", hist_img1)
cv2.imshow("dst2_OpenCV", dst2);  cv2.imshow("OpenCV_hist", hist_img2)
cv2.waitKey()