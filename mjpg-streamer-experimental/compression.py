import cv2
import time

def filter(image):
    time.sleep(0.01)
    return cv2.resize(image,(100,100))
def init_filter():
    return filter
