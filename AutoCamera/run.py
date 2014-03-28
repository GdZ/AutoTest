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
# import the monkeyrunner modules used by this program
import time;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

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
	device.press(keycode, action);
	MonkeyRunner.sleep(1);

def sprdCamera():
	# t-Shark postition
	TAG = "sprdCamera"
	POST_X = 240;
	POST_Y = 744;
	testCount = 1000;
	for i in range(0, testCount):
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
		LOGD(TAG, str(i) + ':Begin a new take photo test...')
		doClick('KEYCODE_BACK', 'DOWN_AND_UP');
		MonkeyRunner.sleep(1);
		doClick('KEYCODE_BACK', 'DOWN_AND_UP');

		MonkeyRunner.sleep(2);
		LOGD(TAG, str(i) + ':This test is beginning...')
		# open Camera
		# sprd android 4.0 8825c
		#device.startActivity(component='com.android.camera/.Camera');
		# sprd android 4.1 tshark
		LOGD(TAG, str(i) + ":Openning Camera...");
		device.startActivity(component='com.android.gallery3d/com.android.camera.Camera')

		MonkeyRunner.sleep(2);
		LOGD(TAG, str(i) + ":Waiting for take photo...")

		#/////////////////////////////////////////////////////////////////////////
		#
		#    EasyMonkeyDevice cannot be used in some version of phone, so replaced
		# by touch point position.
		#
		#------------------------------------------------------------------------
		#easy_device = EasyMonkeyDevice(device);
		#easy_device.touch(By.id('id/shutter_button'), MonkeyDevice.DOWN_AND_UP);
		#------------------------------------------------------------------------
		device.touch(POST_X, POST_Y, MonkeyDevice.DOWN_AND_UP);
		#/////////////////////////////////////////////////////////////////////////
		LOGD(TAG, str(i) + ":Have take photo...")

		MonkeyRunner.sleep(4);
		LOGD(TAG, str(i) + ":Exiting Camera...")

		# exit Camera
		doClick('KEYCODE_BACK', 'DOWN_AND_UP');
		LOGD(TAG, str(i) + ":This test is finished.")

def huaweiCamera():
	# t-Shark postition
	TAG = "huaweiCamera"
	POST_X = 240;
	POST_Y = 744;
	testCount = 1000;
	for i in range(0, testCount):
		MonkeyRunner.sleep(2);
		LOGD(TAG, str(i) + ":This test is beginning...")
		# open Camera
		# android 4.0 8825cd
		#device.startActivity(component='com.android.camera/.Camera');
		# android 4.1 tshark
		LOGD(TAG, str(i) + ":Openning Camera...")
		## this is for sprd test.
		#device.startActivity(component='com.android.gallery3d/com.android.camera.Camera')
		## this is for huawei test
		device.startActivity(component='com.android.gallery3d/com.android.camera.CameraLauncher')

		MonkeyRunner.sleep(2);
		LOGD(TAG, str(i) + ":Waiting for take photo...")

		#/////////////////////////////////////////////////////////////////////////
		#
		#    EasyMonkeyDevice cannot be used in some version of phone, so replaced
		# by touch point position.
		#
		#------------------------------------------------------------------------
		#easy_device = EasyMonkeyDevice(device);
		#easy_device.touch(By.id('id/shutter_button'), MonkeyDevice.DOWN_AND_UP);
		#------------------------------------------------------------------------
		device.touch(POST_X, POST_Y, MonkeyDevice.DOWN_AND_UP);
		#/////////////////////////////////////////////////////////////////////////
		LOGD(TAG, str(i) + ":Have take photo...")

		MonkeyRunner.sleep(4);
		LOGD(TAG, str(i) + ":Exiting Camera...")

		# exit Camera
		doClick('KEYCODE_BACK', 'DOWN_AND_UP');
		LOGD(TAG, str(i) + ":This test is finished.")


# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
doClick('KEYCODE_HOME','DOWN_AND_UP')
#LOGD('test', 'this is the test....')
sprdCamera();
#huaweiCamera();

