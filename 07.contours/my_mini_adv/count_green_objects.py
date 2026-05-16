import cv2
import numpy as np

img = cv2.imread('shapes.png')

# Convert BGR → HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Green range
lower_green = np.array([35,50,50])
upper_green = np.array([85,255,255])

# Create mask
mask = cv2.inRange(
    hsv,
    lower_green,
    upper_green
)

# Find contours only in mask
contours, hierarchy = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contour
cv2.drawContours(
    img,
    contours,
    -1,
    (0,255,0),
    3
)

print("Green objects:", len(contours))

cv2.imshow("Mask", mask)
cv2.imshow("Result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()