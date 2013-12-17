#!/bin/bash
# init adb
ADB=adb
# init script file
camera_file=$1

# init log folder and file
logdir=${PWD}/log_`date +%Y%m%d%H%M%S`
# create log folder
mkdir -p ${logdir}

# set log file full path
logpath=
logcatpath=
bugreportpath=

# just show the script file
echo ${call_file}

logfile="AutoCamera_monkeyrunner_`date +%Y.%m.%d_%H.%M.%S`.log"
logpath=${logdir}/${logfile}
touch ${logpath}
tail -f ${logpath} &

logcatfile="AutoCamera_logcat_`date +%Y.%m.%d_%H.%M.%S`.log"
logcatpath=${logdir}/${logcatfile}
touch ${logcatpath}
#tail -f ${logcatpath}

function reportlog()
{
	echo "Capture bugreport."
	bugreportfile="AutoCamera_bugreport_`date +%Y.%m.%d_%H.%M.%S`.log"
	bugreportpath=${logdir}/${bugreportfile}
	touch ${bugreportpath}
	#tail -f ${bugreportpath}
	${ADB} shell bugreport >> ${bugreportpath} 2>&1
}

function caplog()
{
	echo "Capture logcat."
	${ADB} shell logcat -v threadtime >> ${logcatpath} 2>&1
}

function doCamera()
{
	monkeyrunner ${camera_file} >> ${logpath} 2>&1
	reportlog
	sleep 2
}

caplog &

#reportlog
#echo $logpath
#echo $logcatpath
#echo $bugreportpath
#exit 0

echo 'Pay attention, the testing is beginning...'
echo 'Do testing loop 1'
doCamera
echo 'Do testing loop 2'
doCamera
echo 'Do testing loop 3'
doCamera
echo 'Do testing loop 4'
doCamera
echo 'Do testing loop 5'
doCamera
echo 'Do testing loop 6'
doCamera
echo 'Do testing loop 7'
doCamera
echo 'Do testing loop 8'
doCamera
echo 'Do testing loop 9'
doCamera
echo 'Do testing loop 10'
doCamera
echo 'Pay attention, the testing is finished...'
