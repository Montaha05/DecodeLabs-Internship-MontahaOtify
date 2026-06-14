import cv2

def preprocess_image(image_path):
    """
        Perform:
        1. Grayscale conversion
        2. Gaussian blur
        3. Adaptive thresholding

    """
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Can't load image: {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    threshold = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )
    return image, gray, blur, threshold
