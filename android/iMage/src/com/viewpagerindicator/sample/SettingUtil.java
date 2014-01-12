package com.viewpagerindicator.sample;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;

/**
 * Created by olunxchen on 2013.
 */
public class SettingUtil {
    private final static String settingName = "Settings";

    private final static String bugHomeAnimateRunning = "bug_home_animate_running";

    private final static String bugHomeAnimateHeight = "bug_home_animate_height";

    private final static String buglyFirstRun = "bugly_first_run_3";

    private final static String settingCurrentApp = "current_app";
    private final static String settingCurrentTapdId = "current_tapd_id";
    private final static String settingCurrentTapdName = "current_tapd_name";

    private final static String settingCurrentNotify = "current_notify";
    private final static String settingLastFeedback = "feedback";

    private final static String settingSubmitMethodFloat = "submit_method_float";
    private final static String settingSubmitMethodNotification = "submit_method_notification";

    private final static String settingCaptureStatus = "capture_status";
    private final static String settingCaptureQuality = "capture_quality";

    private final static String settingCaptureMethodShake = "capture_method_shake";
    private final static String settingCaptureMethodShakeOption = "capture_method_shake_option";

    private final static String settingLogcatStatus = "logcat_status";
    private final static String settingLogcatBufferMain = "logcat_buffer_main";
    private final static String settingLogcatBufferSystem = "logcat_bugger_system";
    private final static String settingLogcatBufferEvents = "logcat_buffer_events";
    private final static String settingLogcatBufferRadio = "logcat_buffer_radio";
    private final static String settingLogcatMode = "logcat_mode";

    private final static String settingPacketCaptureStatus = "packet_capture_status";
    private final static String settingTcpdumpStatus = "tcpdump_status";
    private final static String settingTcpdumpOption = "tcpdump_option";

    private final static String settingBugreportStatus = "bugreport_status";

    private final static String settingVoiceinputStatus = "voiceinput_status";

    private final static String settingScreenrecordStatus = "screen_record_status";
    private final static String settingScreencastStatus = "screencast_status";
    private final static String settingScreencastQualy = "screencast_quality";
    private final static String settingScreencastFps = "screencast_fps";
    private final static String settingScreencastSpeed = "screencast_speed";

    private final static String settingStartupStatus = "startup_status";

    private final static String settingUserIdentity = "user_identity";

    private final static String settingHomePageGuide = "home_page_guide";
    private final static String settingPostBoxGuide = "post_box_guide";
    private final static String settingDraftBoxGuide = "draft_box_guide";
    private final static String settingSettingPageGuide = "setting_page_guide";
    private final static String settingPaintingGuide = "setting_painting_guide";


    private static void setPreferences(Context context, String name, String value) {
        SharedPreferences share = context.getSharedPreferences(settingName, Activity.MODE_PRIVATE);
        SharedPreferences.Editor editor = share.edit();
        editor.putString(name, value);
        editor.commit();
    }

    private static String getPreferences(Context context, String name) {
        SharedPreferences share = context.getSharedPreferences(settingName,
                Activity.MODE_PRIVATE);
        return share.getString(name, null);
    }

    private static void setBooleanPreferences(Context context, String name, boolean value) {
        SharedPreferences share = context.getSharedPreferences(settingName, Activity.MODE_PRIVATE);
        SharedPreferences.Editor editor = share.edit();
        editor.putBoolean(name, value);
        editor.commit();
    }

    private static Boolean getBooleanPreferences(Context context, String name) {
        SharedPreferences share = context.getSharedPreferences(settingName,
                Activity.MODE_PRIVATE);
        return share.getBoolean(name, false);
    }

    private static void setIntPreferences(Context context, String name, int value) {
        SharedPreferences share = context.getSharedPreferences(settingName, Activity.MODE_PRIVATE);
        SharedPreferences.Editor editor = share.edit();
        editor.putInt(name, value);
        editor.commit();
    }

    private static int getIntPreferences(Context context, String name) {
        SharedPreferences share = context.getSharedPreferences(settingName,
                Activity.MODE_PRIVATE);
        return share.getInt(name, 0);
    }

    //首次运行
    public static void setBuglyFirstRun(Context context, boolean value) {
        setBooleanPreferences(context, buglyFirstRun, value);
    }

    public static boolean getBuglyFirstRun(Context context) {
        return getBooleanPreferences(context, buglyFirstRun);
    }

    //主页按钮点击运行
    public static void setBugHomeAnimateRunning(Context context, boolean value) {
        setBooleanPreferences(context, bugHomeAnimateRunning, value);
    }

    public static boolean getBugHomeAnimateRunning(Context context) {
        return getBooleanPreferences(context, bugHomeAnimateRunning);
    }

    //主页按钮点击运行
    public static void setBugHomeAnimateHeight(Context context, int value) {
        setIntPreferences(context, bugHomeAnimateHeight, value);
    }

    public static int getBugHomeAnimateHeight(Context context) {
        return getIntPreferences(context, bugHomeAnimateHeight);
    }


    //当前App
    public static void setSettingCurrentApp(Context context, String value) {
        setPreferences(context, settingCurrentApp, value);
    }

    public static String getSettingCurrentApp(Context context) {
        return getPreferences(context, settingCurrentApp);
    }

    //当前Tapd
    public static void setSettingCurrentTapdId(Context context, String value) {
        setPreferences(context, settingCurrentTapdId, value);
    }

    public static String getSettingCurrentTapdId(Context context) {
        String result = getPreferences(context, settingCurrentTapdId);
        if (result == null) {
            result = "-1";
            setSettingCurrentTapdId(context, result);
        }
        return result;
    }

    public static void setSettingCurrentTapdName(Context context, String value) {
        setPreferences(context, settingCurrentTapdName, value);
    }

    public static String getSettingCurrentTapdName(Context context) {
        String result = getPreferences(context, settingCurrentTapdName);
        if (result == null) {
            result = "不提交";
            setSettingCurrentTapdName(context, result);
        }
        return result;
    }

    //当前通知人员
    public static void setSettingCurrentNotify(Context context, String value) {
        setPreferences(context, settingCurrentNotify, value);
    }

    public static String getSettingCurrentNotify(Context context) {
        String result = getPreferences(context, settingCurrentNotify);
        if(result == null){
            result = "";
        }
        return result;
    }

    //反馈信息
    public static void setSettingLastFeedback(Context context, String value) {
        setPreferences(context, settingLastFeedback, value);
    }

    public static String getSettingLastFeedback(Context context) {
        return getPreferences(context, settingLastFeedback);
    }

    //提交方式
    public static void setSettingSubmitMethodFloat(Context context, Boolean value) {
        setBooleanPreferences(context, settingSubmitMethodFloat, value);
    }

    public static boolean getSettingSubmitMethodFloat(Context context) {
        return getBooleanPreferences(context, settingSubmitMethodFloat);
    }

    public static void setSettingSubmitMethodNotification(Context context, Boolean value) {
        setBooleanPreferences(context, settingSubmitMethodNotification, value);
    }

    public static boolean getSettingSubmitMethodNotification(Context context) {
        return getBooleanPreferences(context, settingSubmitMethodNotification);
    }

    public static void setSettingCaptureMethodShake(Context context, Boolean value) {
        setBooleanPreferences(context, settingCaptureMethodShake, value);
    }

    public static boolean getSettingCaptureMethodShake(Context context) {
        return getBooleanPreferences(context, settingCaptureMethodShake);
    }

    public static void setSettingCaptureMethodShakeOption(Context context, int value) {
        setIntPreferences(context, settingCaptureMethodShakeOption, value);
    }

    public static int getSettingCaptureMethodShakeOption(Context context) {
        int result = getIntPreferences(context, settingCaptureMethodShakeOption);
        if(result == 0){
            result = 700;
        }
        return result;
    }

    //capture
    public static void setSettingCaptureStatus(Context context, Boolean value) {
        setBooleanPreferences(context, settingCaptureStatus, value);
    }

    public static boolean getSettingCaptureStatus(Context context) {
        return getBooleanPreferences(context, settingCaptureStatus);
    }

    public static void setSettingCaptureQuality(Context context, String value) {
        setPreferences(context, settingCaptureQuality, value);
    }

    public static void setSettingLogcatBufferMain(Context context, Boolean value) {
        setBooleanPreferences(context, settingLogcatBufferMain, value);
    }

    public static boolean getSettingLogcatBufferMain(Context context) {
        return getBooleanPreferences(context, settingLogcatBufferMain);
    }

    public static void setSettingLogcatBufferSystem(Context context, Boolean value) {
        setBooleanPreferences(context, settingLogcatBufferSystem, value);
    }

    public static boolean getSettingLogcatBufferSystem(Context context) {
        return getBooleanPreferences(context, settingLogcatBufferSystem);
    }

    public static void setSettingLogcatBufferEvents(Context context, Boolean value) {
        setBooleanPreferences(context, settingLogcatBufferEvents, value);
    }

    public static boolean getSettingLogcatBufferEvents(Context context) {
        return getBooleanPreferences(context, settingLogcatBufferEvents);
    }

    public static void setSettingLogcatBufferRadio(Context context, Boolean value) {
        setBooleanPreferences(context, settingLogcatBufferRadio, value);
    }

    public static boolean getSettingLogcatBufferRadio(Context context) {
        return getBooleanPreferences(context, settingLogcatBufferRadio);
    }

    //tcpdump
    public static void setSettingTcpdumpStatus(Context context, boolean value){
        setBooleanPreferences(context, settingTcpdumpStatus, value);
    }

    public static boolean getSettingTcpdumpStatus(Context context) {
        return getBooleanPreferences(context, settingTcpdumpStatus);
    }

    public static void setSettingTcpdumpOption(Context context, String value){
        setPreferences(context, settingTcpdumpOption, value);
    }

    public static String getSettingsTcpdumpOption(Context context) {
        String result = getPreferences(context, settingTcpdumpOption);
        if (result == null) {
            result = "-i any -p -s 0";
            setSettingTcpdumpOption(context, result);
        }
        return result;
    }

    //packetcapture
    public static void setSettingPacketCaptureStatus(Context context, boolean value){
        setBooleanPreferences(context, settingPacketCaptureStatus, value);
    }

    public static boolean getSettingPacketCaptureStatus(Context context) {
        return getBooleanPreferences(context, settingPacketCaptureStatus);
    }

    //bugreport
    public static void setSettingBugreportStatus(Context context, boolean value){
        setBooleanPreferences(context, settingBugreportStatus, value);
    }
    public static boolean getSettingBugreportStatus(Context context) {
        return getBooleanPreferences(context, settingBugreportStatus);
    }

    //voiceinput
    public static void setSettingVoiceinputStatus(Context context, boolean value){
        setBooleanPreferences(context, settingVoiceinputStatus, value);
    }
    public static boolean getSettingVoiceinputStatus(Context context) {
        return getBooleanPreferences(context, settingVoiceinputStatus);
    }

    //screencast
    public static void setSettingScreencastStatus(Context context, boolean value){
        setBooleanPreferences(context, settingScreencastStatus, value);
    }
    public static boolean getSettingScreencastStatus(Context context) {
        return getBooleanPreferences(context, settingScreencastStatus);
    }

    public static void setSettingScreencastQualy(Context context, String value) {
        setPreferences(context, settingScreencastQualy, value);
    }

    //首页
    public static void setSettingHomePageGuide(Context context, boolean value){
        setBooleanPreferences(context, settingHomePageGuide, value);
    }
    public static boolean getSettingHomePageGuide(Context context) {
        return getBooleanPreferences(context, settingHomePageGuide);
    }

    //已提交
    public static void setSettingPostBoxGuide(Context context, boolean value){
        setBooleanPreferences(context, settingPostBoxGuide, value);
    }
    public static boolean getSettingPostBoxGuide(Context context) {
        return getBooleanPreferences(context, settingPostBoxGuide);
    }

    //草稿箱
    public static void setSettingDraftBoxGuide(Context context, boolean value){
        setBooleanPreferences(context, settingDraftBoxGuide, value);
    }
    public static boolean getSettingDraftBoxGuide(Context context) {
        return getBooleanPreferences(context, settingDraftBoxGuide);
    }

    //设置
    public static void setSettingSettingPageGuide(Context context, boolean value){
        setBooleanPreferences(context, settingSettingPageGuide, value);
    }
    public static boolean getSettingSettingPageGuide(Context context) {
        return getBooleanPreferences(context, settingSettingPageGuide);
    }

    //设置是否显示提示
    public static void setSettingPaintingGuide(Context context, boolean value){
        setBooleanPreferences(context, settingPaintingGuide, value);
    }
    public static boolean getSettingPaintingGuide(Context context) {
        return getBooleanPreferences(context, settingPaintingGuide);
    }
}
