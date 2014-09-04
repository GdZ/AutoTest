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
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice;
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By;


TAG = "AutoIn.Un.Install"
DEBUG = 1
testCount = 1000;
NOT_FOUND = -1

dType = ""
tmp = ""
ct = 0

## This is the list of package will install and uninstall
""" You can Modify this variable for yourself define.
This variable contain pkginfo, such as
	apk: path of the apk file
	pkg: package name of this apk
	act: the main activity of this package
	pos: the prefer install location
	ins: is this apk have been install or not
"""
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

""" This area just use for format the output, friendly to read
and find out the programe running state.
"""
def LOGI(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [INFO] %s: %s" %(t, TAG, msg)

def LOGD(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] %s: %s" %(t, TAG, msg)

def LOGW(TAG, msg):
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [WARN] %s: %s" %(t, TAG, msg)

""" This is self define function, for useful action
"""
def doClick(keycode, action):
	TAG = "doClick"
	LOGD(TAG, "Do " + keycode + " click " + action)
	MonkeyRunner.sleep(1);
	device.press(keycode, action);
	MonkeyRunner.sleep(1);

""" This is get args from export script
"""
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

# Install one apk files
def InstallAPK(pkginfo):
	mTAG = 'InstallAPK'
	LOGD(mTAG, 'Begin to Install package...')
	ret = device.installPackage(pkginfo['apk'])
	#MonkeyRunner.sleep(1)
	return ret

# Install all package in the pkgList
def InstallAll():
	mTAG = 'InstallAll'
	testCount = len(pkgList)
	for i in range(0, testCount):
		LOGD(mTAG, str(i) + '/' + str(testCount) + ':Begin to Install package...')
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
		LOGD(mTAG, pkgList[i])
		ret = InstallAPK(pkgList[i])
		if ret == True:
			LOGD(mTAG, 'Install package ok...')
			pkgList[i]['ins'] = 1
		else:
			LOGD(mTAG, 'Install package fail...')
			LOGD(mTAG, str(i) + '/' + str(testCount) + ':Uninstall one package for install new package...')
			t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
			for ii in range(0, i, 1) :
				if pkgList[ii]['ins'] == 1:
					LOGD(mTAG, pkgList[ii]['apk'] + ' will be uninstall....')
					UninstallAPK(pkgList[ii])
					pkgList[ii]['ins'] = 0
				else:
					LOGD(mTAG, pkgList[ii]['apk'] + ' is not install no need to uninstall.')
					continue
		LOGD(mTAG, pkgList[i])
	LOGD(mTAG, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# Uninstall apk package files
def UninstallAPK(pkginfo):
	mTAG = 'UninstallAPK'
	LOGD(mTAG, 'Begin to Uninstall package...')
	ret = device.removePackage(pkginfo['pkg'])
	#MonkeyRunner.sleep(1)
	return ret

# Uninstall all packages
def UninstallAll():
	mTAG = 'UninstallAll'
	testCount = len(pkgList)
	for i in range(0, testCount):
		LOGD(mTAG, str(i) + '/' + str(testCount) + ':Begin to Uninstall all package...')
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
		LOGD(mTAG, pkgList[i])
		if pkgList[i]['ins'] == 1 :
			UninstallAPK(pkgList[i])
		LOGD(mTAG, pkgList[i])
	LOGD(mTAG, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# This function just use to delete all package without judgement the install status
def PrepareEnv():
	mTAG = 'PrepareEnv'
	testCount = len(pkgList)
	for i in range(0, testCount):
		LOGD(mTAG, str(i) + '/' + str(testCount) + ':Begin to Uninstall all package...')
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
		LOGD(mTAG, pkgList[i])
		UninstallAPK(pkgList[i])
		LOGD(mTAG, pkgList[i])

def doTask():
	#PrepareEnv()
	LOGD(TAG, 'Install all package begin..................')
	InstallAll()
	LOGD(TAG, 'Uninstall all package begin..................')
	UninstallAll()

checkParams()
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
doClick('KEYCODE_BACK','DOWN_AND_UP')
doTask();
testCount = len(pkgList)
for i in range(0, testCount):
	LOGD(TAG, 'pkgList:' + str(pkgList[i]))
LOGD(TAG, "THIS MODULE TEST HAVE DONE............")

