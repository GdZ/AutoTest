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
import sys;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

#log=open("./copy&del/copy&del.log","w")

POST_X = 238;
POST_Y = 188;
POST_X_CON = 160;
POST_Y_CON = 80;
POST_X_SD = 168;
POST_Y_SD = 300;
POST_X_COPY = 200;
POST_Y_COPY = 313;
POST_X_SDCARD = 230;
POST_Y_SDCARD = 538;
POST_X_COPYS = 358;
POST_Y_COPYS = 80;
POST_X_MENU = 430;
POST_Y_MENU = 75;
POST_X_MANY = 330;
POST_Y_MANY = 300;
POST_X_ALL = 430;
POST_Y_ALL = 150;
POST_X_ONE = 430;
POST_Y_ONE = 230;
POST_X_DEL = 350;
POST_Y_DEL = 80;
POST_X_ENT = 330;
POST_Y_ENT = 530;

testCount = 1000
copyCount = 1000

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

device = MonkeyRunner.waitForConnection()
package = 'com.sprd.fileexplorer' 
activity = 'com.sprd.fileexplorer.activities.FileExploreActivity'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(3) 

t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
print "%s [DEBUG] This test is beginning..." %(t);
#Switching SD-Card list
device.touch(POST_X_CON,POST_Y_CON,MonkeyDevice.DOWN_AND_UP);
MonkeyRunner.sleep(1);
device.touch(POST_X_SD,POST_Y_SD,MonkeyDevice.DOWN_AND_UP);
MonkeyRunner.sleep(1);
t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
print "%s [DEBUG] This test is beginning..." %(t);

for i in range(0, testCount):
#Script cycle
    for j in range(0, copyCount):
#Replication cycle
        t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
        print "%s [DEBUG] [%04d] [%04d] This test is copy..." %(t,i,j);
        device.touch(POST_X,POST_Y,MonkeyDevice.DOWN);
        MonkeyRunner.sleep(3);
        device.touch(POST_X,POST_Y,MonkeyDevice.UP);
        MonkeyRunner.sleep(2);
        device.touch(POST_X_COPY,POST_Y_COPY,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(2);
        device.touch(POST_X_SDCARD,POST_Y_SDCARD,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(2);
        device.touch(POST_X_COPYS,POST_Y_COPYS,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(5);
    else:
        t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
        print "%s [DEBUG] [%04d] This test is del all file..." %(t,i);   
        device.touch(POST_X_MENU,POST_Y_MENU,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(1);
        device.touch(POST_X_MANY,POST_Y_MANY,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(1);
        device.touch(POST_X_ALL,POST_Y_ALL,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(1);
        device.touch(POST_X_ONE,POST_Y_ONE,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(1);
        device.touch(POST_X_DEL,POST_Y_DEL,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(1);
        device.touch(POST_X_ENT,POST_Y_ENT,MonkeyDevice.DOWN_AND_UP);
        MonkeyRunner.sleep(6);
        t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
    	print "%s [DEBUG] [%04d] This test is del OK..." %(t,i); 
else:
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
    print "%s [DEBUG] The test is completed ..." %(t);
