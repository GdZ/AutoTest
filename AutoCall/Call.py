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
# This is the test for Auto call, just for speaker's keepon test.
# Develop by zgd1348833@gmail.com
# This is just for T8702A (Hisense)
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
# call icon position in lanucher
PHONE_ICON_X = 64;
PHONE_ICON_Y = 789;

# call icon position in callboard
CALL_ICON_X = 117;
CALL_ICON_Y = 722;

# sim card selection
SIM1_ICON_X = 226;
SIM1_ICON_Y = 449;
SIM2_ICON_X = 226;
SIM2_ICON_Y = 537;

# end call
END_ICON_X = 247;
END_ICON_Y = 792;

testCount = 500;


for i in range(0, testCount):
	MonkeyRunner.sleep(2);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]This test is beginning..." %(t,i)

	# open phone from lanucher
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Openning phone call dial..." %(t,i)
	device.touch(PHONE_ICON_X, PHONE_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(1);

	# click on call icon
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]click dial pad..." %(t,i)
	device.touch(CALL_ICON_X, CALL_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(4);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]click dial pad..." %(t,i)
	device.touch(CALL_ICON_X, CALL_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(3);

	# select sim1
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]select a sim1 card..." %(t,i)
	device.touch(SIM1_ICON_X, SIM1_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(15);

	# end call
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]end call..." %(t,i)
	device.touch(END_ICON_X, END_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	device.press('KEYCODE_BACK', 'DOWN_AND_UP');
	MonkeyRunner.sleep(2);
	device.press('KEYCODE_BACK', 'DOWN_AND_UP');
	MonkeyRunner.sleep(2);

	#================================================
	# open phone from lanucher
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Openning phone call dial..." %(t,i)
	device.touch(PHONE_ICON_X, PHONE_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(2);

	# click on call icon
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]click dial pad..." %(t,i)
	device.touch(CALL_ICON_X, CALL_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(4);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]click dial pad..." %(t,i)
	device.touch(CALL_ICON_X, CALL_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(3);

	# select sim1
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]select a sim2 card..." %(t,i)
	device.touch(SIM2_ICON_X, SIM2_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(15);

	# end call
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]end call..." %(t,i)
	device.touch(END_ICON_X, END_ICON_Y, MonkeyDevice.DOWN_AND_UP);
	device.press('KEYCODE_BACK', 'DOWN_AND_UP');
	MonkeyRunner.sleep(3);
	device.press('KEYCODE_BACK', 'DOWN_AND_UP');
	MonkeyRunner.sleep(3);

	# this is finished
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]This test is finished." %(t,i)
print "Test finished."
