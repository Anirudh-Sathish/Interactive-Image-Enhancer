import numpy as np
import cv2

def logarithmic_transformation(img, c=None):
    # Read the input image as grayscale using OpenCV
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_array = np.array(img, dtype=np.float32)

    # Apply logarithmic transformation
    if c is None:
        c = 255 / np.log(1 + np.max(img_array))
    log_image = c * np.log(1 + img_array)

    # Convert the transformed array back to an OpenCV image
    log_image = np.array(log_image, dtype=np.uint8)

    return log_image
