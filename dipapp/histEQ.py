import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
from PIL import Image

def custom_histogram_equalization(img ,probabilities, num_bins):
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    height, width = img.shape
    a = np.zeros((256,), dtype=np.float16)
    b = np.zeros((256,), dtype=np.float16)

    # Compute the image histogram
    for i in range(width):
        for j in range(height):
            g = img[j, i]
            a[g] = a[g] + 1

    # Interpolate the input probabilities to 256 bins
    x = np.linspace(0, 255, num_bins)
    x_new = np.arange(0, 256)
    probabilities = np.interp(x_new, x, probabilities)

    # Perform histogram equalization
    tmp = 1.0 / (height * width)
    for i in range(256):
        for j in range(i + 1):
            b[i] += a[j] * tmp * probabilities[j]
        b[i] = round(b[i] * 255)

    b = b.astype(np.uint8)

    # Remap values from equalized histogram into the image
    for i in range(width):
        for j in range(height):
            g = img[j, i]
            img[j, i] = b[g]
    return img