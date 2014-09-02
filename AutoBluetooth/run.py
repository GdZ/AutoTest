import time;
import sys;
#import pydoc;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

testCount = 10000
TAG = "AutoBluetooth"
DEBUG = 1
NOT_FOUND = -1
module='com.android.settings/com.android.settings.Settings'
OPEN_CLOSE_X = 368
OPEN_CLOSE_Y = 182

dType = sys.argv[1]
print "%s" %(dType)
print "dType.length=%d" %(len(dType))

# Just show all characters of get from args
for i in range(0,len(dType)):
	print "dType[%d]=%c" %(i, dType[i])

""" Modify for this just because sys.argv, which is get from shell,
which contain some special non-display character
"""
tmp = dType
if(NOT_FOUND != tmp.find("7060S")):
	print "This is 7060S"
	OPEN_CLOSE_X = 340
	OPEN_CLOSE_Y = 330
elif(NOT_FOUND != tmp.find("7061")):
	print "This is 7061"
	OPEN_CLOSE_X = 335
	OPEN_CLOSE_Y = 325
elif(NOT_FOUND != tmp.find("YourType")):
	""" If you want add devices, just modify bellow
	Add your device's position here.
	"""
	print "What you want to show"
else:
	print "Why are you goto here"

device = MonkeyRunner.waitForConnection()
#width = MonkeyDevice.getProperty(display.width);
#height = MonkeyDevice.getProperty(display.height);

def LOGD(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] %s: %s" %(t, TAG, msg)

def doClick(keycode, action):
	TAG = "doClick"
	LOGD(TAG, "Do " + keycode + " click " + action)
	device.press(keycode, action);
	MonkeyRunner.sleep(1);


#def main():
print "start"
doClick('KEYCODE_BACK', 'DOWN_AND_UP');
doClick('KEYCODE_BACK', 'DOWN_AND_UP');
device.startActivity(component=module);
MonkeyRunner.sleep(2);
for i in range(0,testCount):
	MonkeyRunner.sleep(2);
	LOGD(TAG, str(i)+" click open and close 1st-click.")
	device.touch(OPEN_CLOSE_X,OPEN_CLOSE_Y,MonkeyDevice.DOWN_AND_UP);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	MonkeyRunner.sleep(2);
	LOGD(TAG, str(i)+" click open and close 2nd-click.")
	device.touch(OPEN_CLOSE_X,OPEN_CLOSE_Y,MonkeyDevice.DOWN_AND_UP);

