
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("C:\Users\praku\OneDrive\Desktop\images (1).jpg")
# Logarithmic Transformation
c_log = 255 / np.log(1 + np.max(image))
log_transformed = c_log * np.log(1 + image)
log_transformed = np.array(log_transformed, dtype=np.uint8)
# Power Law (Gamma) Transformation
gamma = 2.2
c_gamma = 255 / (255 ** gamma)
gamma_transformed = c_gamma * (image ** gamma)
gamma_transformed = np.array(gamma_transformed, dtype=np.uint8)
# Plotting the images
plt.figure(figsize=(10,5))
plt.subplot(132)
plt.title('Log Transformation')
plt.imshow(log_transformed, cmap='gray')
plt.subplot(133)
plt.title('Gamma Transformation')
plt.imshow(gamma_transformed, cmap='gray')
plt.show()