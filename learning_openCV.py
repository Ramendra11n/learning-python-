# an image is just a function of two variables x and y and the value of the function denotes the intensity 
# grayscale 
# 0-black
# top -white (255)
# every pixel is an element of the two -d array and its stores the values for the intensity the values range from the 0-255
# the colored image sare formed using the rgb and now the colored images are basically combination of the rgb individual intensity 
#  hsi model 
# hue-predominant colour
# saturation:how much pure it is
# intensity

import cv2
import numpy as np

img_path="./drive-download-20221105T090638Z-001/sherlock_kid.png";
print(img_path);
img =cv2.imread(img_path);#this show the matrix form of the image in which there will be three column representing the intensity of three colours and the resolution of the colors 
# cv2.imshow("image",img);#this function is basically used for the sake of showing the current image in the python 
print(img);
#cv2.waitKey(0);#this function is used to make the image wait while displaying.
# converting the format in from  bgr to hva or grayscale 
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
cv2.imshow("image",img);
cv2.imshow("image1",img_gray);#this function is basically used for the sake of showing the current image in the python 
# the parameter of this function accepts the name of tthe window and second accepts the name of the variables
# saving the image
cv2.imwrite("./drive-download-20221105T090638Z-001/sher.png",img_gray);
# the function accepts two parameters first being the location and after that the second parameter is the name of the image variable you  want to save .
print(np.shape(img_gray));
print(np.shape(img));
# resizing the image 
img_resized=cv2.resize(img,(500,500))
cv2.imshow("resizedimage",img_resized);

# image cropping is nothing but slicing of the array
img_cropped= img [:,335:];
cv2.imshow("croppeddimage",img_cropped);
(a,b,d)=np.shape(img);
c=int(0.25*b);

img_cropped_2=img[:,c:];
cv2.imshow("cropped",img_cropped_2);
cv2.waitKey(0);




# videos handling
video_reader=cv2.VideoCapture(0);
#  zeroe is used for the webcam 
while true:
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





