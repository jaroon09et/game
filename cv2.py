from parinya import LINE
import time
import cv2
line= LINE('โทเค็น')
cap= cv2.VideoCapture(0)
  while True:
   _, frame = cap.read()
line.sendimage(frame[:, :, ::-1])
time.sleep(1)
