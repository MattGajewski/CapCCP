import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open camera")
    
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Camera Feed', frame)
        
        if cv2.waitKey(25) & 0xFF == ord('d'):
            break
    
    else:
        break
    
cap.release()

cv2.destroyAllWindows()