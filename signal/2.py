
import cv2
import numpy as np
import os

# Read the image in grayscale
img = cv2.imread(r"C:\Users\praku\OneDrive\Desktop\MAchine Learning Algo\signal\file_sheet\shri-kashi-vishwanath copy.jpg", 0)

# Validate image loaded
if img is None:
    raise FileNotFoundError("Image not found. Check the path.")

m, n = img.shape

# --- 1. Negative Transformation ---
L = img.max()
img_neg = L - img
cv2.imwrite(r"C:\Users\praku\OneDrive\Desktop\MAchine Learning Algo\signal\file_sheet\shri-kashi-vishwanath_negative.jpg", img_neg)

#  Binary_Thresholdingk
T = 150
img_thresh = np.zeros((m, n), dtype=np.uint8)

for i in range(m):
    for j in range(n):
        if img[i, j] < T:
            img_thresh[i, j] = 0
        else:
            img_thresh[i, j] = 255

cv2.imwrite(r"C:\Users\praku\OneDrive\Desktop\MAchine Learning Algo\signal\file_sheet\shri-kashi-vishwanath_thresh.jpg", img_thresh)

# --- 3. Background Thresholding (Range T1 to T2) ---
T1 = 100
T2 = 180
img_thresh_back = np.zeros((m, n), dtype=np.uint8)

for i in range(m):
    for j in range(n):
        if T1 < img[i, j] < T2:
            img_thresh_back[i, j] = 255
        else:
            img_thresh_back[i, j] = img[i, j]  # ✅ Fixed line

cv2.imwrite(r"C:\Users\praku\OneDrive\Desktop\MAchine Learning Algo\signal\file_sheet\shri-kashi-vishwanath_thresh_back.jpg", img_thresh_back)
