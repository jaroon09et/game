from parinya import LINE
import time
import cv2
line= LINE('a4cbbedeca6373e7642fac2399b640fa4008e856

')
cap= cv2.VideoCapture(0)
  while True:
   _, frame = cap.read()
line.sendimage(frame[:, :, ::-1])
time.sleep(1)
