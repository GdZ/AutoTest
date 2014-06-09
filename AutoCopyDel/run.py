from __future__ import division

import time;
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
