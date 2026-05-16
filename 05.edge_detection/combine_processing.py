import cv2

img = cv2.imread("img.jpg",0)

# Blur to reduce noise
blur = cv2.GaussianBlur(img,(5,5),0)

# Otsu threshold
ret, thresh = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Canny edge detection
edges = cv2.Canny(thresh,100,200)

cv2.imshow("Original", img)
cv2.imshow("Blur", blur)
cv2.imshow("Threshold", thresh)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()