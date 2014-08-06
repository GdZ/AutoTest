import time;
import sys;
#import pydoc;
#import sys;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

testCount = 10000
TAG = "AutoWlanShift"
DEBUG = 1
lteCamera='com.android.settings/com.android.settings.Settings'
OPEN_CLOSE_X = 368
OPEN_CLOSE_Y = 182

dType = sys.argv[1]
print "%s" %(dType)

""" Must copy dType to tmp
Because dType contain some non-display character
I'm so amazing about this
"""
" modify @2014.08.06 begin "
tmp = ""
ct = 0
for i in range(0,len(dType)-1):
	print "dType[%d]=%c" %(i, dType[i])
	if('\0' == dType[i]):
		break
	else:
		ct = ct + 1
	tmp = tmp + "" + dType[i]
print "ct:%d,dType:%d" %(ct, len(dType)-1)
" modify @2014.08.06 end "

if("7060S" == tmp):
	print "This is 7060S"
	OPEN_CLOSE_X = 340
	OPEN_CLOSE_Y = 260
elif("YourType" == tmp):
	""" If you want add devices, just modify bellow
	Add your device's position here.
	"""
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
for i in range(0,testCount):
	device.startActivity(component=lteCamera);
	MonkeyRunner.sleep(2);
	LOGD(TAG, str(i)+"click open and close 1st.")
	device.touch(OPEN_CLOSE_X,OPEN_CLOSE_Y,MonkeyDevice.DOWN_AND_UP);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	#imageA = device.takeSnapshot();
	#Files = "./test/time_" + t + "_count_" + str(i) + "_Open.png";
	#imageA.writeToFile(Files,'png');
	#print "%s round %04d open" %(t,i+1);
	MonkeyRunner.sleep(5);
	LOGD(TAG, str(i)+"click open and close 1st.")
	device.touch(OPEN_CLOSE_X,OPEN_CLOSE_Y,MonkeyDevice.DOWN_AND_UP);
	#t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	#imageA = device.takeSnapshot();
	#Files = "./test/time_" + t + "_count_" + str(i) + "_Close.png";
	#imageA.writeToFile(Files,'png');
	#print "%s round %04d close" %(t,i+1);
	MonkeyRunner.sleep(3);
