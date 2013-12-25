
package com.cgmobile.earspeakertester;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.media.AudioManager;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.concurrent.TimeUnit;

public class MainActivity extends Activity {
    public static final String TAG = "[ljfy]MainActivity";
    public static final String ACTION_TIME = "com.cgmobile.earspeakertester.timegoing";

    private MainReceiver receiver;
    private IntentFilter intentFilter;
    private Button buttonPlay;
    private Button buttonStop;
    private TextView tvStartedTime;
    private TextView tvRunningTime;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        buttonPlay = (Button) this.findViewById(R.id.button_play);
        buttonStop = (Button) this.findViewById(R.id.button_stop);
        tvStartedTime = (TextView) this.findViewById(R.id.tv_start_time);
        tvRunningTime = (TextView) this.findViewById(R.id.tv_running_time);

        receiver = new MainReceiver();
        intentFilter = new IntentFilter(ACTION_TIME);

        // we use the volume button to control the voice call volume
        setVolumeControlStream(AudioManager.STREAM_VOICE_CALL);
    }

    /*
     * @Override public boolean onKeyDown(int keyCode, KeyEvent event) {
     * if(keyCode == KeyEvent.KEYCODE_VOLUME_UP){ } // do your stuff here... if
     * ((keyCode == KeyEvent.KEYCODE_VOLUME_UP) || (keyCode ==
     * KeyEvent.KEYCODE_VOLUME_DOWN)) { return super.onKeyUp(keyCode, event); }
     * return true; }
     */

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
//        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    /*@Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case R.id.action_clear_record:
                break;
        }
        return super.onOptionsItemSelected(item);
    }*/

    public boolean onButtonClick(View v) {
        Intent intent = new Intent();
        intent.setClass(this, MainService.class);
        switch (v.getId()) {
            case R.id.button_play:
                Log.d(TAG, "click the play button");
                this.startService(intent);
                break;
            case R.id.button_stop:
                Log.d(TAG, "click the stop button");
                this.stopService(intent);
                break;
            default:
                Log.e(TAG, "unknown button click : " + v.getId());
                break;
        }

        return true;
    }

    @Override
    protected void onStart() {
        super.onStart();
        this.registerReceiver(receiver, intentFilter);
        // setVolumeControlStream(AudioManager.STREAM_VOICE_CALL);
        Log.d(TAG, "registering the broadcast receiver");
    }

    @Override
    protected void onStop() {
        this.unregisterReceiver(receiver);
        Log.d(TAG, "unregistering the broadcast receiver");
        super.onStop();
    }

    private void setTime(Bundle bundle) {
        if (bundle != null) {
            if (bundle.containsKey(TimeRunnable.TIME_STARTED)) {
                // this time not changed often
                // if(!tvStartTime.getText().equals("")){
                SimpleDateFormat format = new SimpleDateFormat("MM-dd HH:mm:ss",
                        Locale.getDefault());
                tvStartedTime.setText(format.format(new Date(bundle
                        .getLong(TimeRunnable.TIME_STARTED))));
                // }

            } else {
                Log.e(TAG, "the time started of bundle is null???");
            }
            if (bundle.containsKey(TimeRunnable.TIME_RUNNING)) {
                long timeLong = bundle.getLong(TimeRunnable.TIME_RUNNING);
                long day = TimeUnit.MILLISECONDS.toDays(timeLong);
                long dayTime = day * 24;
                long hour = TimeUnit.MILLISECONDS.toHours(timeLong) - dayTime;
                dayTime *= 60;
                long hourTime = hour * 60;
                long min = TimeUnit.MILLISECONDS.toMinutes(timeLong) - dayTime - hourTime;
                dayTime *= 60;
                hourTime *= 60;
                long minTime = min * 60;
                long sec = TimeUnit.MILLISECONDS.toSeconds(timeLong) - dayTime - hourTime - minTime;
                tvRunningTime.setText(String.format("%02d", day) + "天"
                        + String.format("%02d", hour) + "时" + String.format("%02d", min) + "分"
                        + String.format("%02d", sec) + "秒");
            } else {
                Log.e(TAG, "the time running of bundle is null???");
            }
        } else {
            Log.e(TAG, "the bundle of intent is null???");
        }
    }

    class MainReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals(ACTION_TIME)) {
                setTime(intent.getExtras());
                return;
            }

            Log.w(TAG, "we got a unknown broadcast : " + action);
        }
    }
}
