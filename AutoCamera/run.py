"""
#####################################################################################
#
# Copyright (c) 2013 M.R.Z <zgd1348833@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#====================================================================================
#
# This Script is just for Auto Camera testing.
# Before test:
#   As this you would take 10,000 pictures. One picture is more than 460kB, the total
# is more than 4.6GB, so you must insert a 8GB or bigger SDCARD into the phone. Only
# in this way your testing will be continue correctly.
#
# Test Step:
#	1. Open Camera
#	2. Take photo
#	3. Exit Camera
#	4. After 15 seconds end the call
#	5. Double click on back key, return to desktop
#
# Some other:
#   As this test just want to do 10,000 times calls, which monkeyrunner can do 1000
# times a loop, so just do 10 times loop, which is no need to use for-loop statement.
#
#####################################################################################
"""
# import the monkeyrunner modules used by this program
import time;
import sys;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

TAG = "AutoCamera"
testCount = 1000;
DEBUG = 1
NOT_FOUND = -1

## define four points
# 0--------->x
# | 11   12
# |   . .
# |    .
# |   . .
# | 21   22
# V
# y
# point 11
x11 = 200;
y11 = 600;
dx = 100;
dy = 150;
# point 22
x22 = x11 + dx;
y22 = y11 + dy;
# point 12
x12 = x11 + dx;
y12 = y11;
# point 21
x21 = x11;
y21 = y11 + dy;
DURATION = 0.1;
STEPS = 100;
A11 = (x11, y11);
A12 = (x12, y12);
A21 = (x21, y21);
A22 = (x22, y22);

## tips for comp
Video='com.android.camera2/com.android.camera.VideoCamera'
Photo='com.android.camera2/com.android.camera.CameraActivity'
actVideo='android.media.action.VIDEO_CAMERA'
actPhoto='android.media.action.STILL_IMAGE_CAMERA'

# t-Shark postition
POST_X = 240;
POST_Y = 744;
POST_X_V = 272;

def checkParams():
	dType = sys.argv[1]
	print "%s" %(dType)
	print "dType.length=%d" %(len(dType))

	# Just show all characters of get from args
	"""
	for i in range(0,len(dType)):
		print "dType[%d]=%c" %(i, dType[i])
	"""

	""" Modify for this just because sys.argv, which is get from shell,
	which contain some special non-display character
	"""
	tmp = dType
	if(NOT_FOUND != tmp.find("7060S")):
		POST_X = 240;
		POST_Y = 744;
		POST_X_V = 272;
		Photo='com.android.camera2/com.android.camera.CameraActivity'
		actPhoto='android.media.action.STILL_IMAGE_CAMERA'
		Video='com.android.camera2/com.android.camera.VideoCamera'
		actVideo='android.media.action.VIDEO_CAMERA'
	elif(NOT_FOUND != tmp.find("7061")):
		POST_X = 240;
		POST_Y = 744;
		POST_X_V = 272;
		Photo='com.android.camera2/com.android.camera.CameraActivity'
		actPhoto='android.media.action.STILL_IMAGE_CAMERA'
		Video='com.android.camera2/com.android.camera.VideoCamera'
		actVideo='android.media.action.VIDEO_CAMERA'
	elif(NOT_FOUND != tmp.find("YourType")):
		""" If you want add devices, just modify bellow
		Add your device's position here.
		"""
		print "What you want to show"
	else:
		print "Why are you goto here"

def LOGI(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [INFO] %s: %s" %(t, TAG, msg)

def LOGD(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] %s: %s" %(t, TAG, msg)

def LOGW(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [WARN] %s: %s" %(t, TAG, msg)

def doClick(keycode, action):
	TAG = "doClick"
	LOGD(TAG, "Do " + keycode + " click " + action)
	MonkeyRunner.sleep(1);
	device.press(keycode, action);
	MonkeyRunner.sleep(1);

def P11_P12(i):
	#i = 11,12;
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]flick from left to right" %(t,i)
	device.drag(A11,A12,DURATION,STEPS);

def Flick(i,start,end):
	#i = 11,12;
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]flick from right to left" %(t,i)
	device.drag(start,end,DURATION,STEPS);

def capVideo(i):
	## switch to Video
	LOGD(TAG, str(i) + ":Switch to video capture...");
	MonkeyRunner.sleep(1);
	device.startActivity(component=Video,action=actVideo)
	LOGD(TAG, str(i) + ":Take video begin...");
	MonkeyRunner.sleep(2);
	device.touch(POST_X, POST_Y, MonkeyDevice.DOWN_AND_UP);
	LOGD(TAG, str(i) + ":Recording video...");
	MonkeyRunner.sleep(10);
	device.touch(POST_X_V, POST_Y, MonkeyDevice.DOWN_AND_UP);
	LOGD(TAG, str(i) + ":Waiting for store video...");
	doClick('KEYCODE_BACK', 'DOWN_AND_UP');
	LOGD(TAG, str(i) + ":Take video finished.");

def capPhoto(i):
	## switch to Photo
	LOGD(TAG, str(i) + ":Switch to photo capture...");
	MonkeyRunner.sleep(1);
	device.startActivity(component=Photo,action=actPhoto)
	LOGD(TAG, str(i) + ":Take photo...");
	MonkeyRunner.sleep(2);
	device.touch(POST_X, POST_Y, MonkeyDevice.DOWN_AND_UP);
	LOGD(TAG, str(i) + ":Exiting Photo...");
	doClick('KEYCODE_BACK', 'DOWN_AND_UP');
	LOGD(TAG, str(i) + ":Take photo finished.")

def doTask():
	for i in range(0, testCount):
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
		LOGD(TAG, str(i) + ':Begin a new take photo test...')
		doClick('KEYCODE_BACK', 'DOWN_AND_UP');
		LOGD(TAG, str(i) + ':Begin to cap video...')
		capVideo(i);
		LOGD(TAG, str(i) + ':Begin to cap photo...')
		doClick('KEYCODE_BACK', 'DOWN_AND_UP');
		capPhoto(i);

checkParams()
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
doClick('KEYCODE_BACK','DOWN_AND_UP')
#LOGD('test', 'this is the test....')
#sprdCamera();
#huaweiCamera();
doTask();
#doTask(hwCamera);

