import cv2
import numpy as np

img = cv2.imread('shapes.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(
    gray,
    240,
    255,
    cv2.THRESH_BINARY_INV
)

contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Find largest contour
largest = max(contours, key=cv2.contourArea)

# Area of largest object
area = cv2.contourArea(largest)

print("Largest area:", area)

# Draw only largest contour
cv2.drawContours(
    img,
    [largest],
    -1,
    (0,255,0),
    4
)

cv2.imwrite('largest.jpg',img)