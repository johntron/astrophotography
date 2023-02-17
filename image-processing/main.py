import math
import os

import cv2
import matplotlib
import pandas as pd
import skimage

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import rawpy
from parallel_pandas import ParallelPandas

ParallelPandas.initialize(n_cpu=12)

def info(path):
    print(path)
    input = []
    for file in os.listdir(path):
        file = f'{path}{file}'
        with rawpy.imread(file) as raw:
            print(raw.color_desc)
            print(raw.num_colors)
            print(raw.postprocess())


def read_raw(path):
    return rawpy.imread(path).postprocess()


def stack(path):
    M = None
    first_image = None
    last_image = None
    files = pd.DataFrame([f'{path}{file}' for file in os.listdir(path)], columns=['path'])
    files['raw'] = files['path'].apply(read_raw)
    raw = files['raw']
    show_hist(raw[0])
    show_subs(files)
    plt.show()
    #    image = cv2.cvtColor(raw.postprocess(), cv2.COLOR_RGB2BGR).astype(np.float32) / 255
    #    last_image = image
    #    if first_image is None:
    #        # convert to gray scale floating point image
    #        first_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #        stacked_image = image
    #    else:
    #        # Estimate perspective transform
    #        s, M = cv2.findTransformECC(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), first_image, M,
    #                                    cv2.MOTION_HOMOGRAPHY)
    #        w, h, _ = image.shape
    #        # Align image to first image
    #        image = cv2.warpPerspective(image, M, (h, w))
    #        stacked_image += image
    # stacked_image /= len(files)
    # stacked_image = (stacked_image * 255).astype(np.uint8)
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.set_title('last')
    # ax1.imshow(last_image)
    # ax2.set_title('stacked')
    # ax2.imshow(stacked_image)
    # plt.show()
    # cv2.imwrite('output.jpg', stacked_image)
    # cv2.waitKey(0)


def show_subs(files):
    rows = cols = math.ceil(math.sqrt(files.shape[0]))
    fig, axs = plt.subplots(rows, cols, squeeze=False)
    axs = axs.flatten()
    for (i, file) in enumerate(files['raw']):
        axs[i].imshow(cv2.cvtColor(file, cv2.COLOR_BGR2RGB))
        axs[i].axis('off')
    plt.tight_layout()
    plt.subplots_adjust(top=1,
                        bottom=0,
                        left=0,
                        right=1,
                        hspace=0,
                        wspace=0)

def show_hist(file):
    fig, axs = plt.subplots(3, sharex=True, sharey=True)
    for (i, color) in enumerate(['red', 'green', 'blue']):
        hist, bins = skimage.exposure.histogram(file[..., i], source_range='dtype')
        axs[i].plot(bins, hist)
        axs[i].set_title(color)



def apply_theme():
    plt.tight_layout()


if __name__ == '__main__':
    apply_theme()
    stack('input/M42 RAW 41F ISO800 8min/')
