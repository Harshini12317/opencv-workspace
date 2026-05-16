import cv2

img = cv2.imread("img.jpg",0)

ret, otsu = cv2.threshold(
    img,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print("Threshold value:", ret)

cv2.imshow("Otsu", otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()