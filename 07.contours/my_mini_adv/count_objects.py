import cv2
import numpy as np

img = cv2.imread('shapes.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert threshold
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

cv2.drawContours(
    img,
    contours,
    -1,
    (0,255,0),
    3
)

print("Number of objects:", len(contours))


cv2.imwrite('output.jpg',img)