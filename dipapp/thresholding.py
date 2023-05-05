import numpy as np
import cv2

def threshold_image(img, threshold_value):
    # Read the input image as grayscale using OpenCV
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding
    _, thresholded_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

    return thresholded_img