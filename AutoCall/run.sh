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
#
# This Script is just for Auto Call testing.
# Before test:
#	Dail a number. Which can be 10086 and other number. Through this is just create
#	a record in calllog.
#
# Test Step:
#	1. Open dial pad
#	2. Dail number from last call
#	3. Dail the number
#	4. After 15 seconds end the call
#	5. Double click on back key, return to desktop
#
# Some other:
#   As this test just want to do 10,000 times calls, which monkeyrunner can do 1000
# times a loop, so just do 10 times loop, which is no need to use for-loop statement.
#
#####################################################################################
## You can set some var to DEBUG

## init adb
ADB=adb
# init script file
run_file=$1
proj=$2
DEBUG=$3
echo "DEBUG:"$DEBUG
repeat=
if [ -z $4 ]
then
	repeat=10
else
	repeat=$4
fi
echo "Set repeat to ${repeat}"

#DTYPE=`adb shell getprop ro.yulong.version.software | cut -d'.' -f6`
DTYPE=`adb shell getprop ro.yulong.version.software`

# init log folder and file
logdir=${PWD}/logs/${proj}_`date +%Y%m%d%H%M%S`
# create log folder
mkdir -p ${logdir}

# set log file full path
logpath=
logcatpath=
bugreportpath=

# just show the script file
echo ${call_file}

logfile="Monkeyrunner_`date +%Y.%m.%d_%H.%M.%S`.log"
logpath=${logdir}/${logfile}
touch ${logpath}
tail -f ${logpath} &

function catlog()
{
	logcatfile="Logcat_`date +%Y.%m.%d_%H.%M.%S`.log"
	logcatpath=${logdir}/${logcatfile}
	touch ${logcatpath}
	#tail -f ${logcatpath}
}

function reportlog()
{
	echo "============================ Capture bugreport."
	bugreportfile="Bugreport_`date +%Y.%m.%d_%H.%M.%S`.log"
	bugreportpath=${logdir}/${bugreportfile}
	touch ${bugreportpath}
	#tail -f ${bugreportpath}
	${ADB} shell bugreport >> ${bugreportpath} 2>&1
}

function caplog()
{
	echo "============================= Capture logcat."
	${ADB} shell logcat -v threadtime >> ${logcatpath} 2>&1
}

function slog4pc()
{
	echo "============================== Capture slog."
	${PWD}/slog/linux/LogAndroid2PC.sh
}

function doRun()
{
	#echo "monkeyrunner ${run_file} ${DTYPE} >> ${logpath} 2>&1"
	monkeyrunner ${run_file} ${DTYPE} >> ${logpath} 2>&1
	if [ $DEBUG -eq 0 ]
	then
		echo "Just do the test."
		#reportlog
		slog4pc
	else
		echo "This is just show doRun tips"
	fi
	sleep 2
}

echo 'Pay attention, the testing is beginning...'
for(( i=0; i<${repeat}; i++ )){
	echo 'Do doRun loop '$i
	doRun
}
echo 'Pay attention, the testing is finished...'
