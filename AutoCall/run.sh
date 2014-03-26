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
# init adb
ADB=adb
# init script
call_file=$1

# init log folder and file
logdir=${PWD}/logs/log_`date +%Y%m%d%H%M%S`
# create log folder
mkdir -p ${logdir}

#init logpath
logpath=
logcatpath=
bugreportpath=

# just show the script file
echo ${call_file}

logfile="AutoCall_monkeyrunner_`date +%Y.%m.%d_%H.%M.%S`.log"
logpath=${logdir}/${logfile}
touch ${logpath}
tail -f ${logpath} &

function catlog()
{
	logcatfile="AutoCall_logcat_`date +%Y.%m.%d_%H.%M.%S`.log"
	logcatpath=${logdir}/${logcatfile}
	touch ${logcatpath}
	#tail -f ${logcatpath}
}

function reportlog()
{
	echo "============================ Capture bugreport."
	bugreportfile="AutoCall_bugreport_`date +%Y.%m.%d_%H.%M.%S`.log"
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

function doCall()
{
	monkeyrunner ${call_file} >> ${logpath} 2>&1
	#reportlog
	slog4pc
	sleep 2
}

#caplog &

echo 'Pay attention, the testing is beginning...'
echo 'Do testing loop 1'
doCall
echo 'Do testing loop 2'
doCall
echo 'Do testing loop 3'
doCall
echo 'Do testing loop 4'
doCall
echo 'Do testing loop 5'
doCall
echo 'Do testing loop 6'
doCall
echo 'Do testing loop 7'
doCall
echo 'Do testing loop 8'
doCall
echo 'Do testing loop 9'
doCall
echo 'Do testing loop 10'
doCall
echo 'Pay attention, the testing is finished...'
