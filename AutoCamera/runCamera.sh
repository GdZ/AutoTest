#!/bin/bash
camera_file=$1
echo ${camera_file}
logdir=${PWD}/log
logfile="monkeyrunner_`date +%Y%m%d%H%M%S`.log"
logpath=${logdir}/${logfile}

mkdir -p ${logdir}
touch ${logpath}
tail -f ${logpath} &

function doCamera()
{
	monkeyrunner ${camera_file} >> ${logpath} 2>&1
}

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
