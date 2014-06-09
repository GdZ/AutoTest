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
