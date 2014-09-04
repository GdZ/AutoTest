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
#
#####################################################################################
"""
# import the monkeyrunner modules used by this program
import time;
import sys;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

TAG = "AutoFlick"
testCount = 1000;
DEBUG = 1
NOT_FOUND = -1

# postition
b_x = 330;
b_y = 570;
# 0--------->x
# | 11   12
# |   . .
# |    .
# |   . .
# | 21   22
# V
# y
# point 11
x11 = 130;
y11 = 440;
xx = 240;
yy = 160;
# point 22
x22 = x11 + xx;
y22 = y11 + yy;
# point 12
x12 = x11 + xx;
y12 = y11;
# point 21
x21 = x11;
y21 = y11 + yy;

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
	elif(NOT_FOUND != tmp.find("7061")):
	elif(NOT_FOUND != tmp.find("YourType")):
		""" If you want add devices, just modify bellow
		Add your device's position here.
		"""
		print "What you want to show"
	else:
		print "Why are you goto here"

def P11_P22(i):
	#i = 11,22;
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]flick from up-left to down-right" %(t,i)
	device.drag((x11,y11),(x22,y22),0.1);

def P12_P21(i):
	#i = 12,21;
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]flick from up-right to down-left" %(t,i)
	device.drag((x12,y12),(x21,y21),0.1);

def P11_P12(i):
	#i = 11,12;
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]flick from up-right to down-left" %(t,i)
	device.drag((x11,y11),(x12,y12),0.1);

def click_btn(i):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]flick from up-right to down-left" %(t,i)
	device.touch(b_x, b_y, MonkeyDevice.DOWN_AND_UP)

def loop():
	for ii in range(0, testCount):
		P11_P22(ii)
		MonkeyRunner.sleep(2);
		P12_P21(ii)
		MonkeyRunner.sleep(2);
		click_btn(ii)
		MonkeyRunner.sleep(5);

checkParams()
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection();
loop()
