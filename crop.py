import os
import cv2

path = 'crop'
if not os.path.exists(path):
    os.mkdir(path)
else:
    print('Folder has already exists!!!!')

ESC_KEY = 27
interval = 1
video_file = 'video/sana2.mp4'
window_name = 'video'
cascade_file = "cascade/lbpcascade_animeface.xml"

cascade = cv2.CascadeClassifier(cascade_file)

def detect_face(image):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors = 5, minSize=(50, 50))
    return faces

video = cv2.VideoCapture(video_file)
cv2.namedWindow(window_name)
end_flag, frame = video.read()

frame_cnt = 0
face_frame_cnt = 1700

while end_flag:
    frame_cnt = frame_cnt + 1
    print(frame_cnt)

    if frame_cnt % 20 == 0:
        for(x, y, w, h) in detect_face(frame):
            face_frame_cnt = face_frame_cnt + 1
            croped = frame[y:y+h, x:x+w]
            croped = cv2.resize(croped, (128, 128))
            cv2.imshow(window_name, croped)
            cv2.imwrite('crop/'+ str(face_frame_cnt) + '.jpg', croped)
            print('Croped!!!')

    key = cv2.waitKey(interval)
    if key == ESC_KEY:
        break

    end_flag, frame = video.read()

# end function
cv2.destroyAllWindows()
video.release()
print('ALL FINISHED!!!!!!!!!!!')