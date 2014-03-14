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

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
device.press('KEYCODE_HOME','DOWN_AND_UP')

# t-Shark postition
POST_X = 240;
POST_Y = 744;

testCount = 500;

for i in range(0, testCount):
	MonkeyRunner.sleep(2);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]This test is beginning..." %(t,i)
	# open Camera
	# android 4.0 8825cd
	#device.startActivity(component='com.android.camera/.Camera');
	# android 4.1 tshark
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Openning Camera..." %(t,i)
	device.startActivity(component='com.android.gallery3d/com.android.camera.Camera')

	MonkeyRunner.sleep(2);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Waiting for take photo..." %(t,i)

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

	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Have take photo..." %(t,i)

	MonkeyRunner.sleep(4);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Exiting Camera..." %(t,i)

	# exit Camera
	ret = device.press('KEYCODE_BACK', 'DOWN_AND_UP');
	print "%s [DEBUG] [%4d]ret:%s" %(t,i,ret)

	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]This test is finished." %(t,i)
