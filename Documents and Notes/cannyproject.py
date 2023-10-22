import cv2
cap = cv2.VideoCapture('Video1.mov')

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)  


    cv2.imshow('Camera Feed', frame)
    cv2.imshow('Canny Edges', edges)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:   
        break

cap.release()
cv2.destroyAllWindows()
