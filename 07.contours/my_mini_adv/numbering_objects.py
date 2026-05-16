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

for i, contour in enumerate(contours):

    x, y, w, h = cv2.boundingRect(contour)

    # Draw contour
    cv2.drawContours(
        img,
        [contour],
        -1,
        (0,255,0),
        3
    )

    # Put object number
    cv2.putText(
        img,
        f"Obj {i+1}",
        (x, y-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,0,255),
        2
    )

cv2.imwrite('numbered_objects.jpg',img)