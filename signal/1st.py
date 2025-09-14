
import cv2
import matplotlib.pyplot as plt

# Loading the image
image = cv2.imread(r"signal\file_sheet\shri-kashi-vishwanath.jpg", 1)

# Resizing the image
half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
shrinking = cv2.resize(image, (1050, 1610))
stretch_near = cv2.resize(image, (800, 600), interpolation=cv2.INTER_LINEAR)

# Convert BGR to RGB for proper matplotlib display
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
half = cv2.cvtColor(half, cv2.COLOR_BGR2RGB)
shrinking = cv2.cvtColor(shrinking, cv2.COLOR_BGR2RGB)
stretch_near = cv2.cvtColor(stretch_near, cv2.COLOR_BGR2RGB)

# Titles and images
Titles = ["Original", "Half", "Shrinking", "Interpolation Nearest"]
images = [image, half, shrinking, stretch_near]

# Plotting the images in a 2x2 grid
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
    plt.axis('off')  # Optional: Hide axes for cleaner view

plt.tight_layout()   # Optional: Auto-adjust subplot params
plt.show()
