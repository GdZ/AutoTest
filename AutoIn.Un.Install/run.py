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
import sys;
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

# t-Shark postition
TAG = "AutoIn.Un.Install"
testCount = 1000
dType = ""
tmp = ""
ct = 0

## This is the list of package will install and uninstall
pkgList = [{'apk':'91xiongmaokanshu_6010.apk', 'pkg':'com.nd.android.pandareader', 'act':'', 'pos':1, 'ins':0},
	{'apk':'anjuke_313787.apk', 'pkg':'com.anjuke.android.app', 'act':'', 'pos':1, 'ins':0},
	{'apk':'baidushoujizhushou_16783875.apk', 'pkg':'com.baidu.appsearch', 'act':'', 'pos':1, 'ins':0},
	{'apk':'baiduyuyinzhushou_16779783.apk', 'pkg':'com.baidu.voiceassistant', 'act':'', 'pos':1, 'ins':0},
	{'apk':'chelunkaojiazhao_42.apk', 'pkg':'cn.eclicks.drivingtest', 'act':'', 'pos':1, 'ins':0},
	{'apk':'haoduolingsheng_29.apk', 'pkg':'com.haoduolingsheng.RingMore', 'act':'', 'pos':1, 'ins':0},
	{'apk':'lvxingfanyiguan_70.apk', 'pkg':'com.mfw.voiceguide', 'act':'', 'pos':1, 'ins':0},
	{'apk':'MIUIExpress_200.apk', 'pkg':'com.miui.miuilite', 'act':'', 'pos':1, 'ins':0},
	{'apk':'mojitianqi_36002.apk', 'pkg':'com.moji.mjweather', 'act':'', 'pos':1, 'ins':0},
	{'apk':'MomentCam_38.apk', 'pkg':'com.manboker.headportrait', 'act':'', 'pos':1, 'ins':0},
	{'apk':'nice_21.apk', 'pkg':'com.nice.main', 'act':'', 'pos':1, 'ins':0},
	{'apk':'qiudali_51.apk', 'pkg':'com.imdali', 'act':'', 'pos':1, 'ins':0},
	{'apk':'shengriguanjia_495.apk', 'pkg':'com.octinn.birthdayplus', 'act':'', 'pos':1, 'ins':0},
	{'apk':'sougousousuo_260.apk', 'pkg':'com.sogou.activity.src', 'act':'', 'pos':1, 'ins':0},
	{'apk':'VoiceSearch_214.apk', 'pkg':'com.google.android.voicesearch', 'act':'', 'pos':1, 'ins':0},
	{'apk':'yingyuliulishuo_195.apk', 'pkg':'com.liulishuo.engzo', 'act':'', 'pos':1, 'ins':0}]

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

def InitArgs():
	dType = sys.argv[1]
	print "dType: ", dType

	""" Must copy dType to tmp
	Because dType contain some non-display character
	I'm so amazing about this
	"""
	" modify @2014.08.06 begin "
	for i in range(0,len(dType)-1):
		print "dType[%d]=%c" %(i, dType[i])
		if('\0' == dType[i]):
			break
		else:
			ct = ct + 1
		tmp = tmp + "" + dType[i]
	print "ct:%d,dType:%d" %(ct, len(dType)-1)
	" modify @2014.08.06 end "

def InstallAPK(pkginfo):
	mTAG = 'InstallAPK'
	LOGD(TAG, "Install Package: " + pkginfo['apk'] + ' the package name is: ' + pkginfo['pkg'])
	MonkeyRunner.sleep(1)
	LOGD(mTAG, 'Begin to Install package...')
	ret = device.installPackage(pkginfo['apk'])
	MonkeyRunner.sleep(1)
	return ret

def UninstallAPK(pkginfo):
	mTAG = 'UninstallAPK'
	LOGD(mTAG, "Uninstall Package: " + pkginfo['apk'] + ' the package name is: ' + pkginfo['pkg'])
	MonkeyRunner.sleep(1)
	LOGD(mTAG, 'Begin to Uninstall package...')
	ret = device.removePackage(pkginfo['pkg'])
	MonkeyRunner.sleep(1)
	return ret

def doTask():
	testCount = len(pkgList)
	ct = 0
	index = 0

	for i in range(0, testCount):
		LOGD(TAG, str(i) + '/' + str(testCount) + ':Begin to Install package...')
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
		LOGD(TAG, pkgList[i])
		ret = InstallAPK(pkgList[i])
		if ret == True:
			LOGD(TAG, 'Install package ok...')
			installed[ct] = i
			ct = ct + 1
			pkgList[i]['ins'] = 1
		else:
			LOGD(TAG, 'Install package fail...')
			LOGD(TAG, str(i) + '/' + str(testCount) + ':Begin to Uninstall package...')
			t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
			index = ct - 1
			if(pkgList[installed[index]]['ins'] == 1):
				LOGD(TAG, pkgList[installed[index]])
				UninstallAPK(pkgList[installed[index]])
				ct = ct - 1
		LOGD(mTAG, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	for j in installed:
		LOGD(TAG, str(i) + '/' + str(testCount) + ':Begin to Uninstall package...')
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
		index = ct - 1
		LOGD(TAG, pkgList[installed[index]])
		UninstallAPK(pkgList[installed[index]])

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
doClick('KEYCODE_BACK','DOWN_AND_UP')
doTask();
LOGD(TAG, "THIS MODULE TEST HAVE DONE............")
