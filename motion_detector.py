import cv2
import numpy as np
from playsound import playsound
import threading

def play_alarm():
    playsound('alarm.mp3')  

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

alarm_triggered = False

while cap.isOpened():
    # Compute the absolute difference between two frames
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 2000:
            continue  # ignore small movements (like light flicker)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1, "Movement Detected!", (10,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

       
        if not alarm_triggered:
            alarm_triggered = True
            threading.Thread(target=play_alarm, daemon=True).start()
  
    cv2.imshow("Motion Detection", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
