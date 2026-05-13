import cv2


image =cv2.imread('img.jpg',0)
#  1 is default  1-> color
# 0 meand grayscale
# -1 unchanged
#  here image is a mattix of pixel values
cv2.imshow('MyImage',image)
# first para-> window name ,  second -> image name 

cv2.waitKey(0)
# wait infinitely until a key is pressed if waitKey(0)
#if waitkey(1000) means wait 1000ms ie.  1s
cv2.imwrite('createdImg.jpg', image)
    

cv2.destroyAllWindows()