#!/bin/bash
# init adb
ADB=adb
# init script
call_file=$1

# init log folder and file
logdir=${PWD}/log_`date +%Y%m%d%H%M%S`
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

logcatfile="AutoCall_logcat_`date +%Y.%m.%d_%H.%M.%S`.log"
logcatpath=${logdir}/${logcatfile}
touch ${logcatpath}
#tail -f ${logcatpath}

function reportlog()
{
	echo "Capture bugreport."
	bugreportfile="AutoCall_bugreport_`date +%Y.%m.%d_%H.%M.%S`.log"
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

function doCall()
{
	monkeyrunner ${call_file} >> ${logpath} 2>&1
	reportlog
	sleep 2
}

caplog &

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
