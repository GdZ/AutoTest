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
from __future__ import division

import time;
import pydoc;
import sys;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

testCount = 100
PAGE = 3

ONE_X = 60
ONE_Y = 153
TWO_X = 180
TWO_Y = 313
THREE_X = 300
THREE_Y = 463
FOUR_X = 420
FOUR_Y = 633
END_X = 450
END_Y = 650
UP_X = 120
UP_Y = 160

dType = sys.argv[1]
print "dType: ", dType

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
imageA = MonkeyRunner.loadImageFromFile("./screen/screen.png")
device = MonkeyRunner.waitForConnection()
t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
print "%s [DEBUG] This test is beginning..." %(t);
i=0;
for i in range(0,testCount):
    j=0;
    for j in range(0,PAGE):
        y = ONE_Y;
        b = 0;
        s = 0;
        for b in range(0,4):
            x = ONE_X;
            a = 1;
            for a in range(1,5):
                t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
                device.touch(x,y,MonkeyDevice.DOWN_AND_UP);
                s = s+1;
                print "x=%d y=%d" %(x,y);
                print "%s Round %d Open the %d app in page %d" %(t,i+1,s,j+1);
                MonkeyRunner.sleep(2);
                imageB = device.takeSnapshot();
                Files = "./test/time_" + t + "_count_" + str(i) + "_pages_"+ str(j) +"_app_"+ str(a+b)+".png"
                imageB.writeToFile(Files,'png');
                device.press('KEYCODE_HOME','DOWN_AND_UP');
                MonkeyRunner.sleep(2);
                device.press('KEYCODE_HOME','DOWN_AND_UP');
                MonkeyRunner.sleep(2);
                device.touch(238,813,MonkeyDevice.DOWN_AND_UP);
                MonkeyRunner.sleep(2);
                x = x+UP_X;
            else:
                y = y+UP_Y;
        else:
            device.drag((430,330),(30,330),0.1,1);
            s = 0;
            MonkeyRunner.sleep(2);
