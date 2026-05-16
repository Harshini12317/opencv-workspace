import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

# Create trackbars
cv2.createTrackbar("Threshold1", "Trackbars", 100, 500, nothing)
cv2.createTrackbar("Threshold2", "Trackbars", 200, 500, nothing)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Optional: reduce noise
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Get current trackbar positions
    t1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
    t2 = cv2.getTrackbarPos("Threshold2", "Trackbars")

    # Canny edge detection
    edges = cv2.Canny(blur, t1, t2)

    cv2.imshow("Original", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()