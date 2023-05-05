import cv2
import numpy as np

def negate_image(img):
    # Read the input image
    # img = cv2.imread(image_path)

    # Negate the image by subtracting it from 255
    negated_img = 255 - img

    return negated_img