
import os
import cv2  

cap = cv2.VideoCapture('vid.mp4')
os.system("ffmpeg -i vid.mp4 -vn -ab 256 audio.mp3")

cv2.namedWindow("video", cv2.WINDOW_NORMAL)  
count = 0

while cap.isOpened():
    ret,frame = cap.read()
    cap.set(cv2.CAP_PROP_FPS, 60)
    cv2.resizeWindow('video',400,400)  
    cv2.imshow('video',frame)
    cv2.imwrite("/home/sarthak11/SteganographyResearch/video/write/frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        os.system("ffmpeg -i vid.mp4 -vn -ab 256 audio.mp3")
        break

#os.system("ffmpeg -i vid.mp4 -vn -ab 256 audio.mp3")
cap.release()
cap.destroyAllWindows()



