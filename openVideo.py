import cv2

filePath = 'utility\People.mp4' #location video

# 0:internal video camera
# 1:external video camera
# Path of video file : open file video
#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(filePath)

while True:
    oke, frame = capture.read() #read video frame by frame
    cv2.imshow('Video', frame) #open video
    
    ##--- Chosee 1 to use
    #if cv2.waitKey(30) == 27: # ESC pressed, 27 ASCII Code ESC
    #if cv2.waitKey(30) == ord('x'): # if x pressed video close
    #if cv2.waitKey(30) & 0xFF == ord('x'): #if x pressed video close
    if cv2.waitKey(30)%256 == 27: # ESC pressed, 27 ASCII Code ESC
        break

capture.release()
cv2.destroyAllWindows()