import cv2
import numpy as np

# Create black image
img= cv2.imread('shapes.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contours
cv2.drawContours(img, contours, -1, (0,255,0), 3)

# cv2.imshow("Contour", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('output.jpg', img)

print("Number of object : ", len(contours))