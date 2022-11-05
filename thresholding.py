import cv2;
import numpy as np;
# thresholding bascially refers to the seprating the pixels into two forms 
# 1.background
# 2.foreground
# if the value of the pixels is greater than the certain value then we make it frontground and if less than that then background
img_path ='./drive-download-20221105T090638Z-001/gray_scale.png'
img=cv2.imread(img_path);
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
cv2.imshow("img",gray);
_,thresh=cv2.threshold(gray,127,100,cv2.THRESH_BINARY);
#this function basically takes four input the image then the threshold_value,then the value we want it to be and thresh binary

cv2.imshow("img2",thresh);
(a,b)=gray.shape;
arr=np.copy(gray)

cv2.imshow("Gray", arr)
for i in  range(0,a-1):
    for j in  range(0,b-1):
        if (arr[i,j]>=125):
            arr[i,j]=255;
        else:
            arr[i,j]=0;

cv2.imshow("imgi",arr);

cv2.waitKey(0);
