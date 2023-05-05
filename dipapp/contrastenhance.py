import numpy as np
import cv2

def enhance_contrast(img, alpha, beta):
    # Read the input image as grayscale using OpenCV
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_array = np.array(img, dtype=np.float32)

    # Apply contrast enhancement
    img_array = alpha * img_array + beta
    img_array = np.clip(img_array, 0, 255)

    # Convert the enhanced array back to an OpenCV image
    enhanced_img = img_array.astype(np.uint8)

    return enhanced_img