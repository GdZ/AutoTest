#!/bin/bash
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
#                       ATTENTION PLEASE
# -----------------------------------------------------------------------------------
# @2013.12.17
# @M.R.Z <zgd1348833@gmail.com>
# ___________________________________________________________________________________
#    If you want use this script, you must make sure that you
# have configure your android develop environment.
#
# export SDK_HOME=${HOME}/download/android-sdk-linux
# export PATH=${SDK_HOME}:${SDK_HOME}/tools:${SDK_HOME}/platform-tools:$PATH
#
#    After that, you must add the following variable to your
# .bashrc or profile file. Then use command:
#	source ~/.bashrc
#	or
#	source ~/profile
# to enable your environment vaiable.
#
#    At last you can use this script to run the monkeyrunner
# testing.
#
#####################################################################################

# The test modules init area
sh_AutoCall=./AutoCall/runCall.sh
sh_AutoCamera=./AutoCamera/runCamera.sh

function menu()
{
	echo "
	===========================================
	                AutoTest Menu
	-------------------------------------------
	   1. Auto Call Test.
	   2. Auto Camera Test.
	   *. Other just reverse
	===========================================
	";
}

function AutoCall()
{
	${sh_AutoCall} ${PWD}/AutoCall/Call.py
}

function AutoCamera()
{
	${sh_AutoCamera} ${PWD}/AutoCamera/Camera.py
}

menu
read -p "Choose the test you want do? " ch
case $ch in
	1)
		echo "run AutoCall test [01]."
		AutoCall
		echo "run AutoCall test [02]."
		AutoCall
		;;
	2)
		echo "run AutoCamera test [01]."
		AutoCamera
		echo "run AutoCamera test [02]."
		AutoCamera
		;;
	*)
		echo $ch
		echo "Input error"
		;;
esac
