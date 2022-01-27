import cv2
import PoseModule as pm
import time



cap = cv2.VideoCapture('PoseVideos/21.m4v')
cTime = 0
pTime = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    #print(list)  # it is giving an error that index is out of range - impossible        
    if len(lmList) != 0: # to fix the problem above
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (255, 0, 0), cv2.FILLED)    

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)


