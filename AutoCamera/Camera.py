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

testCount = 1000;

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

	MonkeyRunner.sleep(1);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Waiting for take photo..." %(t,i)

	device.touch(POST_X, POST_Y, MonkeyDevice.DOWN_AND_UP);
	#easy_device = EasyMonkeyDevice(device);
	#easy_device.touch(By.id('id/shutter_button'), MonkeyDevice.DOWN_AND_UP);

	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Have take photo..." %(t,i)

	MonkeyRunner.sleep(4);
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]Exiting Camera..." %(t,i)

	# exit Camera
	device.press('KEYCODE_BACK', 'DOWN_AND_UP');

	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
	print "%s [DEBUG] [%04d]This test is finished." %(t,i)
