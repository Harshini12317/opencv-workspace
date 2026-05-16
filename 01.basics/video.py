import cv2

cap= cv2.VideoCapture(0) 

# para =0 means default camera
# 1 means second camera of usb
# video.mp4 for file include
#  this line activates camera

while True:
    ret,frame = cap.read()
    # ret= true if frame is there or else not

    frame = cv2.flip(frame,1)
    # 0 --> vertical flip
    # 1--> horizontal flip
    # -1 --> both flips

    cv2.imshow('myWindow',frame)

    if cv2.waitKey(1)==27:
        break
        # 27 key for esc key

cap.release()
cv2.destroyAllWindows()

