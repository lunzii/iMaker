package com.tencent.image;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Toast;
import com.viewpagerindicator.sample.FileUtil;
import com.viewpagerindicator.sample.SampleTabsDefault;
import com.viewpagerindicator.sample.SettingUtil;

import java.io.File;
import java.io.InputStream;


/**
 * Create by: olunxchen on 2013
 */
public class StartActivity extends Activity {

    private Handler handler;


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.splash);

        handler = new Handler(){
            @Override
            public void handleMessage(Message msg) {
                process();
            }
        };
        new Thread(){
            @Override
            public void run() {
                try{
                    Thread.sleep(3000);
                }catch (InterruptedException e){
                }
                handler.sendEmptyMessage(0);
            }
        }.start();
    }

    private void process(){
        if(!SettingUtil.getBuglyFirstRun(this)){//第一次启动
            AlertDialog.Builder dialog = new AlertDialog.Builder(this);
            dialog.setTitle("提示");
            dialog.setMessage("你要进行数据备份吗？");
            dialog.setCancelable(false);
            dialog.setNegativeButton("取消", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialogInterface, int i) {
                    dialogInterface.dismiss();
                    finish();
                }
            });
            dialog.setPositiveButton("是的", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialogInterface, int i) {
                    dialogInterface.dismiss();

                    //写配置文件
                    try {
                        InputStream source = StartActivity.this.getResources().openRawResource(R.raw.config);
                        String file = FileUtil.getRootStorePath(StartActivity.this) + File.separator + "config.ini";
                        FileUtil.extractResource(source, file, true);
                    } catch (Exception e) {
                        Log.e("image", Log.getStackTraceString(e));
                    }

                    SettingUtil.setBuglyFirstRun(StartActivity.this, true);

                    Toast.makeText(StartActivity.this, "正在开始努力备份你的靓照！", Toast.LENGTH_LONG).show();
                    new Thread(){
                        @Override
                        public void run() {
                            try{
                                Thread.sleep(3000);
                            }catch (InterruptedException e){
                            }
                            finish();
                        }
                    }.start();
                }
            });
            dialog.show();
        }else{
            goMain();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
    }

    private void goMain() {
        startActivity(new Intent(StartActivity.this, SampleTabsDefault.class));
        finish();
    }

}
