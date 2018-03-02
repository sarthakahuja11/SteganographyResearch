
import cv2  
cap = cv2.VideoCapture('a.mp4')
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    #cap.set(cv2.cv.CV_CAP_PROP_FPS, 60)
    cv2.imshow('window-name',frame)
    #cv2.imwrite("frame%d.jpg" % count, cv2)
    cv2.imwrite("/home/sarthak11/SteganographyResearch/video/write/frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    #ffmpeg -i IMG_1155.MOV -vn -ab 256 audio.mp3

cap.release()
cap.destroyAllWindows()



'''
import cv2

cap = cv2.VideoCapture("a.mp4")
while not cap.isOpened():
    cap = cv2.VideoCapture("a.mp4")
    cv2.waitKey(1000)
    print "Wait for the header"

pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
while True:
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        cv2.imshow('video', frame)
        pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        print str(pos_frame)+" frames"
    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
        print "frame is not ready"
        # It is better to wait for a while for the next frame to be ready
        cv2.waitKey(1000)

    if cv2.waitKey(10) == 27:
        break
    if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break
'''
