import os
import fnmatch
import time
import multiprocessing
import re

pattern = re.compile("MODEL_ID")

cameras = []

visionCamID = "IDHERE"
cameraNum = None
cameraMap = open("/home/nvidia/cameraMap.txt", "r")
for cameraStr in cameraMap:
  if visionCamID in cameraStr:
    cameraNum = cameraStr.split()[0]
    cameraNum = cameraNum.replace("/dev/video", "")
    cameraNum = int(cameraNum)
    cameras.append(cameraNum)
'''
for file in os.listdir('/dev'): # For each plugged in camera
  if fnmatch.fnmatch(file, 'video[0-9]'):
      cameras.append(int(file[-1:])) # Add camera ID to list
#print cameras
'''

def launchcam(id, port):
    os.popen('mjpg_streamer -o "output_http.so -w ./www -p '+str(port)+'" -i "./input_opencv.so --filter ./cvfilter_py.so --fargs ./compression.py --d '+str(cameras[id])+'"')

'''
def back_camera():
    for camera in cameras:
	for i, line in enumerate(os.popen("sudo udevadm info --query=all /dev/video"+str(camera))):
	    if "E: ID_MODEL_ID=" in str(line) and ( not "0779" in str(line) ):
                os.popen('mjpg_streamer -o "output_http.so -w ./www -p '+str(25565)+'" -i "input_opencv.so --d '+str(camera)+'"')
def front_camera():
    for camera in cameras:
	for i, line in enumerate(os.popen("sudo udevadm info --query=all /dev/video"+str(camera))):
	    if "E: ID_MODEL_ID=0779" in str(line):
                os.popen('mjpg_streamer -o "output_http.so -w ./www -p '+str(25567)+'" -i "input_opencv.so --d '+str(camera)+'"') 
'''
	
p1 = multiprocessing.Process(target=launchcam,args=(cameras[0],5800,))
p1.start()
time.sleep(2)
p2 = multiprocessing.Process(target=launchcam,args=(cameras[1],5801,))
p2.start()
time.sleep(2)
p1.join()




