import cv2

img = cv2.imread("img.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

edges = cv2.Canny(thresh,100,200)

cv2.imshow("Original",img)
cv2.imshow("Threshold",thresh)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()