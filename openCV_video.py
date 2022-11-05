
import cv2
# videos handling
video_reader=cv2.VideoCapture(0);
#  zero is used for accessing  the webcam 
while True:
    success,frame=video_reader.read()
    #used to read th frame return the two parameters first success whether we are able to read the frame or not second the next frame 
    if not success:
        break;
    cv2.imshow("my video",frame)
    key=cv2.waitKey(10)
    if(key==ord('q')):#ord function basically return the unicode of the letter
        break;
video_reader.release();#for releasing all the sources that are acquired by the program
cv2.destroyAllWindows();#,for closing all th windows