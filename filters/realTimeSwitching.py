import cv2

cap = cv2.VideoCapture(0)

mode = 0

while True:

    ret, frame = cap.read()

    # Apply filters based on mode
    if mode == 0:
        output = frame

    elif mode == 1:
        output = cv2.blur(frame, (9,9))

    elif mode == 2:
        output = cv2.GaussianBlur(frame, (9,9), 0)

    elif mode == 3:
        output = cv2.medianBlur(frame, 9)

    elif mode == 4:
        output = cv2.bilateralFilter(frame, 9, 75, 75)

    # Show output
    cv2.imshow("Filter Switching", output)

    # Read keyboard input
    key = cv2.waitKey(1)

    # Switch filters
    if key == ord('0'):
        mode = 0

    elif key == ord('1'):
        mode = 1

    elif key == ord('2'):
        mode = 2

    elif key == ord('3'):
        mode = 3

    elif key == ord('4'):
        mode = 4

    # Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()