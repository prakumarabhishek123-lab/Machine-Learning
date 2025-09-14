import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
image = cv2.imread(r'C:\Users\praku\OneDrive\Desktop\image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if image is None:
    print("C:\Users\praku\OneDrive\Desktop\Bar-chart-versus-histogram-chart-elements-representation.png")
    exit()

# Step 1: Compute histogram
hist, bins = np.histogram(image.flatten(), 256, [0, 256])

# Step 2: Compute cumulative distribution function (CDF)
cdf = hist.cumsum()

# Step 3: Normalize the CDF (for plotting only — optional)
cdf_normalized = cdf * hist.max() / cdf.max()

# Step 4: Mask all 0 values in the CDF to avoid division by zero
cdf_m = np.ma.masked_equal(cdf, 0)

# Step 5: Apply histogram equalization formula
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())

# Step 6: Fill masked values with 0 and convert to uint8
cdf_final = np.ma.filled(cdf_m, 0).astype('uint8')

# Step 7: Map the equalized CDF to the original image
image_equalized = cdf_final[image]

# Step 8: Display original and equalized images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(image_equalized, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()
