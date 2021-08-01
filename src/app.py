import pyautogui
import time
import sys
import math
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None

# centralize mouse
height = 1920
width = 1080
pyautogui.moveTo(height / 2, width / 2)

## loop to move in circle
try:
	print('\nPress Ctrl + c to stop.')
	while(True):
		# Radius 
		R = 400
		# measuring screen size
		(x,y) = pyautogui.size()
		# locating center of the screen 
		(X,Y) = pyautogui.position(x/2,y/2)
		# offsetting by radius 
		pyautogui.moveTo(X+R,Y)

		for i in range(360):
			# setting pace with a modulus 
			if i%6==0:
			   pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
except KeyboardInterrupt:
    print('\nDone.')	