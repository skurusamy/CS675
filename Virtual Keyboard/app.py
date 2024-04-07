# open cv library
import cv2 
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

# detectionCon: minimum detection confidence. default 0.5  
detector = HandDetector() 

keyboard = Controller()

final_text = ""

keys = [['Q',"W","E","R","T","Y","U","I","O","P"],
        ['A','S','D','F','G','H','J','K','L',';'],
        ['Z','X','C','V','B','N','M',',','.','/']]

# cv2. VideoCapture( ) to get a video capture object for the camera. 
# it is very easy to capture a live stream from a camera on the OpenCV window.
# VideoCapture(0): Means first camera or webcam.
# VideoCapture(1): Means second camera or webcam.
cap = cv2.VideoCapture(0)

cap.set(3,1280) #3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
cap.set(4,720) #4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.

def drawAll(img,buttonList):  
        #create rectangle and buttons for our keyboard
        #parameters - img(frame), (starting point 100,100), (ending point - 200,200), color, thickness
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img,button.pos,(x + w, y + h),(211, 211, 211),cv2.FILLED)
        cv2.putText(img, button.text,(x + 22, y + 58),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)
    return img

class Button():
    def __init__(self,pos,text,size=[80,80]) -> None:
        self.pos = pos
        self.size = size
        self.text = text

    


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        mybutton = Button([100 * j + 50, 100 * i + 50 ] , key)
        buttonList.append(mybutton)

while True:
    
    #Below lines are for opening the webcam
    success, img = cap.read() # to read the video frame by frame. 

    img = detector.findHands(img) # finds the hand
    lmlist, bboxInfo = detector.findPosition(img) # find Positions along with landmark points. 
    
    img = drawAll(img,buttonList)  

    
    if lmlist:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
            #tip of the finger is point# 8
            if x < lmlist[8][0] < x + w and y < lmlist[8][1] < y + h:
                cv2.rectangle(img,button.pos,(x + w, y + h),(128, 128, 128),cv2.FILLED)
                cv2.putText(img, button.text,(x + 22, y + 58),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)   

                # to detect the click, we are using the distance between tip of index finger and the middle finger. 
                length,_,_ = detector.findDistance(8,12,img,draw=False)
                
                if length < 30:
                    keyboard.press(button.text)
                    cv2.rectangle(img,button.pos,(x + w, y + h),(0, 255, 0),cv2.FILLED)
                    cv2.putText(img, button.text,(x + 22, y + 58),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)
                    final_text += button.text
                    sleep(0.50) # to avoid consecutive clicks

    cv2.rectangle(img,(50 ,350),(700,450),(0, 255, 0),cv2.FILLED)
    cv2.putText(img, final_text,( 72, 408),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)         
    

    cv2.imshow("Image",img) # Display the resulting frame
    cv2.waitKey(1) # if you use waitKey(0) you see a still image until you actually press something while for waitKey(1) the function will show a frame for at least 1 ms only.

