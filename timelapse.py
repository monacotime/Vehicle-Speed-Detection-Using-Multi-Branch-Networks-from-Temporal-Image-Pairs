import numpy as np
from PIL import ImageGrab
import cv2
import time
import os

count = 0
main_dir = r"C:\Users\monac\Videos\speed\timelapse"
cur_dir = f"{main_dir}\{int(time.time())}"
os.mkdir(cur_dir)

while(True):
    printscreen_pil =  ImageGrab.grab(bbox=None)
    printscreen_pil.save(f"{cur_dir}\{count}.jpg","JPEG")
    print("ss no: ", count)
    count+= 1
    time.sleep(10)
