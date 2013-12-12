package com.cgmobile.earspeakertester;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

public class TimeRunnable implements Runnable {
    public static final String TAG = "TimeRunnable";
    
    public static final String TIME_STARTED = "time_started";
    public static final String TIME_RUNNING = "time_running";
    // this is the time total running
    public static final String TIME_ALL = "time_all";
    
    public static final int TIME_SLEEP = 1000;
    
    public static final int TIMES_SAVE = 60;
    private int times2Save = TIMES_SAVE;
    
    private MainService service;
    private Intent intent;
    private Bundle bundle;
    private boolean shouldRun = true;
    private boolean shouldCount = true;
    
    public TimeRunnable(MainService context) {
        this.service = context;
        intent = new Intent(MainActivity.ACTION_TIME);
        bundle = new Bundle();
        bundle.putLong(TIME_STARTED, service.getStartedTime());
    }
    
    public void stopIt (){
        shouldRun = false;
    }
    
    public void shouldCount (boolean shouldCount){
        this.shouldCount = shouldCount;
    }

    @Override
    public void run() {
        while (shouldRun){
            try {
                Thread.sleep(TIME_SLEEP);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            
            if(Thread.currentThread().isInterrupted()){
                Log.e(TAG, "the time thread has been interrupted, return");
                return;
            }
            
            if(shouldCount){
                service.setPlayedTime(service.getPlayedTime() + TIME_SLEEP);
            }
            bundle.putLong(TIME_RUNNING, service.getPlayedTime());
            intent.replaceExtras(bundle);
            service.sendBroadcast(intent);
            
            if(-- times2Save <= 0){
                times2Save = TIMES_SAVE;
                service.saveTimes();
            }
        }
    }
}
