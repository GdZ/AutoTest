#!/bin/bash
black_file=/home/zhanggd/develop/branch.git/AutoTest/MonkeyTest/blacklist.txt
adb push ${black_file} /sdcard/blacklist.txt
while true; do
#adb shell monkey --pkg-blacklist-file /data/blacklist.txt -v-v-v --throttle 1000 5000
adb shell monkey --pkg-blacklist-file /mnt/sdcard/blacklist.txt -c android.intent.category.LAUNCHER -c android.intent.category.MONKEY -c android.intent.category.DEFAULT -c android.intent.category.BROWSABLE -c android.intent.category.TAB -c android.intent.category.ALTERNATIVE -c android.intent.category.SELECTED_ALTERNATIVE -c android.intent.category.INFO -c android.intent.category.HOME -c android.intent.category.PREFERENCE -c android.intent.category.TEST -c android.intent.category.CAR_DOCK -c android.intent.category.DESK_DOCK -c android.intent.category.CAR_MODE --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -s 1130 -v -v -v --throttle 1000 180000 > Monkey_`date +%Y%m%d%H%M%S`.log
#sleep 1
done

