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
# This is the test for Auto call, just for speaker's keepon test.
# Develop by zgd1348833@gmail.com
# This is just for T8702A (Hisense)
#
#####################################################################################
"""
# import the monkeyrunner modules used by this program
import time;
import sys;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

TAG = "AutoCall"
DEBUG = 1
testCount = 1000;
NOT_FOUND = -1

module='com.android.dialer/.DialtactsActivity'

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
		module='com.android.dialer/.DialtactsActivity'
		# call icon position in callboard
		CALL_ICON_X = 240;
		CALL_ICON_Y = 805;
		# end call
		END_ICON_X = 247;
		END_ICON_Y = 792;
		# sim card selection
		SIM1_ICON_X = 226;
		SIM1_ICON_Y = 449;
		SIM2_ICON_X = 226;
		SIM2_ICON_Y = 537;
	elif(NOT_FOUND != tmp.find("7061")):
		""" This is a area you can modify
		"""
		module='com.android.dialer/.DialtactsActivity'
		# call icon position in callboard
		CALL_ICON_X = 240;
		CALL_ICON_Y = 805;
		# end call
		END_ICON_X = 247;
		END_ICON_Y = 792;
		# sim card selection postion
		SIM1_ICON_X = 226;
		SIM1_ICON_Y = 449;
		SIM2_ICON_X = 226;
		SIM2_ICON_Y = 537;
	else:
		""" This is else branch
		"""

def doTask():
	for i in range(0, testCount):
		MonkeyRunner.sleep(2);
		LOGD("doTask", "make a Call -- SIM-1")
		makeCall(1, i)
		LOGD("doTask", "make a Call -- SIM-2")
		makeCall(2, i)

def LOGD(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] %s: %s" %(t, TAG, msg)

def pressKey(keyStr):
	mTAG = "pressKey"
	LOGD(mTAG, "Press the " + keyStr)
	device.press(keyStr, 'DOWN_AND_UP');
	MonkeyRunner.sleep(1);

def touchPos(pos_x, pos_y):
	mTAG = "touchPos"
	LOGD(mTAG, "Touch the postion is (" + str(pos_x) + "," + str(pos_y) + ")")
	device.touch(pos_x, pos_y, MonkeyDevice.DOWN_AND_UP);
	MonkeyRunner.sleep(1);

def makeCall(sim, loop):
	mTAG = "makeCall"
	if (1 == sim):
		sim_x = SIM1_ICON_X
		sim_y = SIM1_ICON_Y
	elif (2 == sim):
		sim_x = SIM2_ICON_X
		sim_y = SIM2_ICON_Y

	# open dail pad
	MonkeyRunner.sleep(1);
	LOGD(mTAG, "[" + str(loop) + "] Openning phone call dial...")
	device.startActivity(component=module);
	MonkeyRunner.sleep(1);

	# dail a number
	LOGD(mTAG, "[" + str(loop) + "] click dial pad...")
	touchPos(CALL_ICON_X, CALL_ICON_Y)
	LOGD(mTAG, "[" + str(loop) + "] click dial pad...")
	touchPos(CALL_ICON_X, CALL_ICON_Y)

	# select sim card
	LOGD(mTAG, "[" + str(loop) + "] select a sim1 card...")
	touchPos(sim_x, sim_y)
	MonkeyRunner.sleep(15);

	# end call
	LOGD(mTAG, "[" + str(loop) + "] end call...")
	touchPos(END_ICON_X, END_ICON_Y)

	# press key_back and key_home
	pressKey('KEYCODE_BACK')
	pressKey('KEYCODE_HOME')

checkParams()
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
pressKey('KEYCODE_BACK')
pressKey('KEYCODE_HOME')
doTask()
LOGD(TAG, "Test finished.")
