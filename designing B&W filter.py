import cv2;
import numpy as np;
img_path='./drive-download-20221105T090638Z-001/book_page.jpg';
img=cv2.imread(img_path);
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
cv2.imshow('img',img);
thresh_val,thresh=cv2.threshold(gray,200,255,cv2.THRESH_OTSU)
print(thresh_val);
cv2.imshow("B/W filter",thresh);
cv2.waitKey(0);