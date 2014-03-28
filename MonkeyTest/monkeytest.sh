#!/bin/bash
black_file=/home/zhanggd/develop/branch.git/AutoTest/MonkeyTest/blacklist.txt

log_fold="log_`date +%Y%m%d`"
mkdir -p ${log_fold}
cd ${log_fold}

adb push ${black_file} /data/local/tmp/blacklist.txt

adb shell logcat -v threadtime > logcat_`date +%Y%m%d%H%M%S`.log &

while true; do
#adb shell monkey --pkg-blacklist-file /data/blacklist.txt -v-v-v --throttle 1000 5000
adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt -c android.intent.category.LAUNCHER -c android.intent.category.MONKEY -c android.intent.category.DEFAULT -c android.intent.category.BROWSABLE -c android.intent.category.TAB -c android.intent.category.ALTERNATIVE -c android.intent.category.SELECTED_ALTERNATIVE -c android.intent.category.INFO -c android.intent.category.HOME -c android.intent.category.PREFERENCE -c android.intent.category.TEST -c android.intent.category.CAR_DOCK -c android.intent.category.DESK_DOCK -c android.intent.category.CAR_MODE --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -s 1130 -v -v -v --throttle 1000 180000 > Monkey_`date +%Y%m%d%H%M%S`.log
#sleep 1
done

