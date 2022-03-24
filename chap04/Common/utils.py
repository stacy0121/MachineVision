import cv2, time
import numpy as np

def print_matInfo(name, image):                    # 행렬 정보 출력 함수
    if image.dtype == 'uint8':  mat_type = 'CV_8U'
    elif image.dtype == 'int8':  mat_type = 'CV_8S'
    elif image.dtype == 'uint16':  mat_type = 'CV_16U'
    elif image.dtype == 'int16':  mat_type = 'CV_16S'
    elif image.dtype == 'float32':  mat_type = 'CV_32F'
    elif image.dtype == 'float64':  mat_type = 'CV_64F'
    nchannel = 3 if image.ndim == 3 else 1

    ## depth, channel 출력
    print("%12s: depth(%s), channel(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type, nchannel))