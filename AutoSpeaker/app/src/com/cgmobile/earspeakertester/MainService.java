
package com.cgmobile.earspeakertester;

import android.app.Notification;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.media.AudioManager;
import android.media.AudioManager.OnAudioFocusChangeListener;
import android.media.MediaPlayer;
import android.os.IBinder;
import android.util.Log;

import java.io.IOException;

public class MainService extends Service implements OnAudioFocusChangeListener {
    public static final String TAG = "MainService";
    public static final String PREFERENCE_FILE_NAME = "info.xml";
    public static final int ID_NOTIFICATION = 1;

    private static final String AUDIO_FILE_NAME = "all rise.mp3";
    // private static final String AUDIO_FILE_PATH = "file:///android_asset/" +
    // AUDIO_FILE_NAME;

    private MediaPlayer mediaPlayer;
    private Thread timeThread;
    private TimeRunnable timeRunnable;

    private long startedTime;
    private long playedTime = 0;

    @Override
    public IBinder onBind(Intent arg0) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public void onCreate() {
        Log.i(TAG, "onCreate");

        if (gainAudioFocus()) {
            setAudioUp();
        }

        startedTime = System.currentTimeMillis();

        timeRunnable = new TimeRunnable(this);
        timeThread = new Thread(timeRunnable);
        timeThread.start();

        startNotification();
        super.onCreate();
    }

    /**
     * use this method to start service on the foreground
     */
    private void startNotification() {
        Notification.Builder builder = new Notification.Builder(this);
        this.startForeground(ID_NOTIFICATION, builder.getNotification());
    }

    public long getPlayedTime() {
        return playedTime;
    }

    public void setPlayedTime(long playedTime) {
        this.playedTime = playedTime;
    }

    public long getStartedTime() {
        return startedTime;
    }

    private boolean gainAudioFocus() {
        AudioManager audioManager = (AudioManager) this.getSystemService(Context.AUDIO_SERVICE);
        audioManager.setMode(AudioManager.MODE_IN_CALL);
        int requestAudioFocus = audioManager.requestAudioFocus(this,
                AudioManager.STREAM_VOICE_CALL,
                AudioManager.AUDIOFOCUS_GAIN);
        if (requestAudioFocus == AudioManager.AUDIOFOCUS_REQUEST_GRANTED) {
            Log.i(TAG, "gain audio focus successed");
            return true;
        } else {
            Log.i(TAG, "gain audio focus failed???");
            return false;
        }
    }

    private boolean dropAudioFocus() {
        AudioManager audioManager = (AudioManager) this.getSystemService(Context.AUDIO_SERVICE);
        audioManager.setMode(AudioManager.MODE_NORMAL);
        int requestAudioFocus = audioManager.abandonAudioFocus(this);
        if (requestAudioFocus == AudioManager.AUDIOFOCUS_REQUEST_GRANTED) {
            Log.i(TAG, "drop audio focus successed");
            return true;
        } else {
            Log.i(TAG, "drop audio focus failed???");
            return false;
        }
    }

    private void setAudioUp() {
        if (mediaPlayer == null) {
            mediaPlayer = new MediaPlayer();
        }

        mediaPlayer.setAudioStreamType(AudioManager.STREAM_VOICE_CALL);

        try {
            mediaPlayer.setDataSource(this.getAssets().openFd(AUDIO_FILE_NAME).getFileDescriptor());
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        } catch (IllegalStateException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        mediaPlayer.setLooping(true);
        // mediaPlayer.setOnPreparedListener(new OnPreparedListener() {
        // @Override
        // public void onPrepared(MediaPlayer mp) {
        // mp.start();
        // }
        // });
        try {
            mediaPlayer.prepare();
        } catch (IllegalStateException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    private boolean pauseOrResumeAudio() {
        if (mediaPlayer != null) {
            if (mediaPlayer.isPlaying()) {
                mediaPlayer.pause();
                setShouldCountTime(false);
            } else {
                mediaPlayer.start();
                timeRunnable.shouldCount(true);
            }
        } else {
            Log.e(TAG, "the media player is null???");
            return false;
        }
        return true;
    }

    private boolean pauseAudio() {
        if (mediaPlayer != null) {
            if (mediaPlayer.isPlaying()) {
                mediaPlayer.pause();
                timeRunnable.shouldCount(false);
            } else {
                Log.w(TAG, "the media player is not playing");
            }
        } else {
            Log.e(TAG, "the media player is null???");
            return false;
        }
        return true;
    }

    private boolean resumeAudio() {
        if (mediaPlayer != null) {
            if (!mediaPlayer.isPlaying()) {
                mediaPlayer.start();
                timeRunnable.shouldCount(true);
            } else {
                Log.w(TAG, "the media player is already playing");
            }
        } else {
            Log.e(TAG, "the media player is null???");
            return false;
        }
        return true;
    }

    private void setShouldCountTime(boolean shouldCount) {
        if (timeRunnable != null) {
            timeRunnable.shouldCount(shouldCount);
        } else {
            Log.e(TAG, "the time runnable is null???");
        }
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.i(TAG, "onStartCommand");
        if (!pauseOrResumeAudio()) {
            // if we didn't resume audio successful, we should try to do this
            // from the beginning.
            justPlayIt();
        }
        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public void onDestroy() {
        Log.i(TAG, "onDestory");
        killAudio();
        dropAudioFocus();
        killThread();
        this.stopForeground(true);

        super.onDestroy();
    }

    private void killThread() {
        if (timeRunnable != null) {
            timeRunnable.stopIt();
        }
        // if (timeThread != null) {
        // if (timeThread.isAlive()) {
        // timeThread.interrupt();
        // }
        // }
    }

    private void killAudio() {
        if (mediaPlayer != null) {
            if (mediaPlayer.isPlaying()) {
                mediaPlayer.stop();
            }
            mediaPlayer.reset();
            mediaPlayer.release();
            mediaPlayer = null;
        } else {
            Log.e(TAG, "the media player is null???");
        }
    }

    private void justPlayIt() {
        if (gainAudioFocus()) {
            setAudioUp();
            resumeAudio();
        }
    }

    @Override
    public void onAudioFocusChange(int focusChange) {
        Log.i(TAG, "on Audio focus change : " + focusChange);
        switch (focusChange) {
            case AudioManager.AUDIOFOCUS_GAIN:
                Log.i(TAG, "gainning audio focus");
                if (!resumeAudio()) {
                    // if we can't resume the audio, let's recreate it.
                    justPlayIt();
                }
                break;
            case AudioManager.AUDIOFOCUS_LOSS:
            case AudioManager.AUDIOFOCUS_LOSS_TRANSIENT:
            case AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK:
                Log.w(TAG, "lossing the audio focus");
                pauseAudio();
                break;
            default:
                Log.w(TAG, "unhandled audio focus change : " + focusChange);
                break;
        }
    }

    public void saveTimes() {
        Log.i(TAG, "saving times to the preferences");
        SharedPreferences sharedPreferences = this.getSharedPreferences(PREFERENCE_FILE_NAME,
                MODE_PRIVATE);
        long lastRunningTime = sharedPreferences.getLong(TimeRunnable.TIME_RUNNING, 0);
        Log.i(TAG, "lastRunningTimes : " + lastRunningTime);
        Log.i(TAG, "time all : " + (lastRunningTime + playedTime));
        Log.i(TAG, "time running : " + playedTime);
        Log.i(TAG, "time started : " + startedTime);
        
        Editor editor = sharedPreferences.edit();
        editor.putLong(TimeRunnable.TIME_ALL, lastRunningTime + playedTime);
        editor.putLong(TimeRunnable.TIME_RUNNING, playedTime);
        editor.putLong(TimeRunnable.TIME_STARTED, startedTime);
        editor.commit();
    }
}
