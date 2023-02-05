import os
import numpy as np
import cv2
import rawpy
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

def info(path):
    print(path)
    input = []
    for file in os.listdir(path):
        file = f'{path}{file}'
        with rawpy.imread(file) as raw:
            print(raw.color_desc)
            print(raw.num_colors)
            print(raw.postprocess())

def stack(path):
    M = None
    first_image = None
    last_image = None
    files = 0
    for file in os.listdir(path):
        files += 1
        image = cv2.imread(f'{path}{file}', 1).astype(np.float32) / 255
        last_image = image
        if first_image is None:
            # convert to gray scale floating point image
            first_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            stacked_image = image
        else:
            # Estimate perspective transform
            s, M = cv2.findTransformECC(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY), first_image, M, cv2.MOTION_HOMOGRAPHY)
            w, h, _ = image.shape
            # Align image to first image
            image = cv2.warpPerspective(image, M, (h, w))
            stacked_image += image
    # stacked_image /= files
    stacked_image = (stacked_image * 255).astype(np.uint8)
    cv2.imshow('last', first_image * 7)
    cv2.imshow('stacked', stacked_image)
    cv2.waitKey(0)

if __name__ == '__main__':
    stack('input/')
