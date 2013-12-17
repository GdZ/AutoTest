#!/bin/bash
call_file=$1
echo ${call_file}
logdir=${PWD}/log
logfile="monkeyrunner_`date +%Y%m%d%H%M%S`.log"
logpath=${logdir}/${logfile}

mkdir -p ${logdir}
touch ${logpath}
tail -f ${logpath} &

function doCall()
{
	monkeyrunner ${call_file} >> ${logpath} 2>&1
}

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
