import numpy as np
import cv2 as cv
# Read image
img = cv.imread(r"C:\Users\praku\OneDrive\Desktop\images.jpg")

# Check if image was loaded successfully
if img is None:
    print("Error: Image not loaded. Check the path.")
    exit()

# Get image dimensions
rows, cols = img.shape[:2]

# Define translation matrix (move image 100px right, 50px down)
M = np.float32([[1, 0, 100], [0, 1, 50]])

# Apply affine transformation
dst = cv.warpAffine(img, M, (cols, rows))

# Show result
cv.imshow('Translated Image', dst)
cv.waitKey(0)
cv.destroyAllWindows()
