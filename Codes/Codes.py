#from unittest import result
import cv2
import mediapipe as mp
import time
from math import sqrt


def dist(x1,y1,x2,y2):
    distance=sqrt((x1-x2)**2 + (y1-y2)**2 )
    return distance

cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

pTime=0
cTime=0

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    lmlist=[]
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                #print(id,cx,cy)

                lmlist.append([id,cx,cy])                   #lmlist here is the list of all the coordinates of landmarks and id represents the index of it
                #print(lmlist)

            r1=dist(lmlist[20][1],lmlist[20][2],lmlist[0][1],lmlist[0][2])/dist(lmlist[17][1],lmlist[17][2],lmlist[0][1],lmlist[0][2])

            r2=dist(lmlist[16][1],lmlist[16][2],lmlist[0][1],lmlist[0][2])/dist(lmlist[13][1],lmlist[13][2],lmlist[0][1],lmlist[0][2])

            r3=dist(lmlist[12][1],lmlist[12][2],lmlist[0][1],lmlist[0][2])/dist(lmlist[9][1],lmlist[9][2],lmlist[0][1],lmlist[0][2])

            r4=dist(lmlist[8][1],lmlist[8][2],lmlist[0][1],lmlist[0][2])/dist(lmlist[5][1],lmlist[5][2],lmlist[0][1],lmlist[0][2])

            r5=dist(lmlist[4][1],lmlist[4][2],lmlist[0][1],lmlist[0][2])/dist(lmlist[2][1],lmlist[2][2],lmlist[0][1],lmlist[0][2])

            #print(r5)


                
                         
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    

    cv2.imshow('img',img)
    cv2.waitKey(1)

    