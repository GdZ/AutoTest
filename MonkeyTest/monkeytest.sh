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
black_file=${HOME}/develop/branch.git/AutoTest/MonkeyTest/blacklist.txt

log_fold="log_`date +%Y%m%d`"
mkdir -p ${log_fold}
cd ${log_fold}

adb push ${black_file} /data/local/tmp/blacklist.txt

adb shell logcat -v threadtime > logcat_`date +%Y%m%d%H%M%S`.log &

while true; do
#adb shell monkey --pkg-blacklist-file /data/blacklist.txt -v-v-v --throttle 1000 5000
adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt \
                 -c android.intent.category.LAUNCHER \
                 -c android.intent.category.MONKEY \
                 -c android.intent.category.DEFAULT \
                 -c android.intent.category.BROWSABLE \
                 -c android.intent.category.TAB \
                 -c android.intent.category.ALTERNATIVE \
                 -c android.intent.category.SELECTED_ALTERNATIVE \
                 -c android.intent.category.INFO \
                 -c android.intent.category.HOME \
                 -c android.intent.category.PREFERENCE \
                 -c android.intent.category.TEST \
                 -c android.intent.category.CAR_DOCK \
                 -c android.intent.category.DESK_DOCK \
                 -c android.intent.category.CAR_MODE \
                 --ignore-crashes \
                 --ignore-timeouts \
                 --ignore-security-exceptions \
                 --ignore-native-crashes \
                 --monitor-native-crashes \
                 -s 1130 -v -v -v --throttle 1000 180000 > Monkey_`date +%Y%m%d%H%M%S`.log
#sleep 1
done

