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
print "dType: ", dType

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
