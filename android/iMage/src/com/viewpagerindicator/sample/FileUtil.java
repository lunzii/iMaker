package com.viewpagerindicator.sample;

import android.content.Context;
import android.os.Build;
import android.os.Environment;

import java.io.*;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class FileUtil {

    private static final String rootPath = "image";
    private static final String bugPath = "bug";


    /**
     * 获取默认Bug存储路径
     *
     * @param context
     * @return
     */
    public static String getDefaultBugPath(Context context) {
        return getStorePath(context, bugPath);
    }

    /**
     * 获取Bug存储文件路径
     *
     * @param context
     * @param ext
     * @return
     */
    public static String getDefaultBugFile(Context context, String ext){
        String name = new SimpleDateFormat("yyyyMMddHHmmss", Locale.US).format(new Date())
                + ext;
        String file = FileUtil.getDefaultBugPath(context) + File.separator + name;
        return file;
    }

    /**
     * 获取Bugly存储根路径
     *
     * @param context
     * @return
     */
    public static String getRootStorePath(Context context) {
        String fullpath;
        if (Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState())) {
            if(Build.VERSION.SDK_INT >= Constant.ANDROID_VERSION_4_1){//Android 4.4以后版本路径问题
                fullpath = "/sdcard" + File.separator + rootPath;
            }else{
                File sdcardDir = Environment.getExternalStorageDirectory();
                fullpath = sdcardDir.getPath() + File.separator + rootPath;
            }
        } else {
            fullpath = context.getFilesDir().getPath() + File.separator + rootPath;
        }
        File check = new File(fullpath);
        if (!check.exists()) {
            check.mkdirs();
        }
        return fullpath;
    }

    /**
     * 获取指定文件夹存储路径
     *
     * @param context
     * @param path
     * @return
     */
    public static String getStorePath(Context context, String path) {
        File storePath = new File(getRootStorePath(context) + File.separator + path);
        if (!storePath.exists()) {
            storePath.mkdirs();
        }
        return storePath.getAbsolutePath();
    }

    public static String getStoreBugFile(Context context, String path, String ext){
        String name = new SimpleDateFormat("yyyyMMddHHmmss", Locale.US).format(new Date())
                + ext;
        String file = path + File.separator + name;
        return file;
    }

    /**
     * 拷贝资源文件
     *
     * @param source
     * @param des
     * @param overwrite
     * @return
     */
    public static boolean extractResource(InputStream source, String des, boolean overwrite) {
        if (source == null || des == null) {
            return false;
        }

        File f = new File(des);
        if (f.exists()) {
            if (!overwrite) {
                return true;
            }
        } else {
            try {
                f.createNewFile();
            } catch (IOException e) {
                return false;
            }
        }

        BufferedInputStream input = null;
        BufferedOutputStream output = null;
        try {
            input = new BufferedInputStream(source);
            output = new BufferedOutputStream(new FileOutputStream(des));

            byte[] buffer = new byte[5120];
            int count = 0;

            while ((count = input.read(buffer)) > 0)
                output.write(buffer, 0, count);
            return true;
        } catch (IOException e) {
            return false;
        } finally {
            try {
                if (input != null)
                    input.close();
                if (output != null)
                    output.close();
            } catch (IOException localIOException) {
                return false;
            }
        }
    }

    /**
     * 删除所有子文件
     *
     * @param dir
     */
    public static void deleteSubFiles(String dir) {
        File file = new File(dir);
        if (file != null && file.exists()) {
            if (file.isDirectory()) {
                File files[] = file.listFiles();
                for (int i = 0; i < files.length; i++) {
                    deleteFile(files[i]);
                }
            }
        }
    }

    /**
     * 删除指定文件
     *
     * @param file
     */
    public static void deleteFile(File file) {
        if (file != null && file.exists()) {
            if (file.isDirectory()) {
                File files[] = file.listFiles();
                for (int i = 0; i < files.length; i++) {
                    deleteFile(files[i]);
                }
            }
            file.delete();
        }
    }

    public static void writeTextFile(String fileName, String content) {
        if (fileName == null) {
            return;
        }

        if (content != null) {
            try {
                FileWriter output = new FileWriter(fileName);
                output.write(content);
                output.flush();
                output.close();
            } catch (IOException e) {
            }
        }
    }

    public static String readTextFile(String fileName) {
        StringBuilder sb = new StringBuilder();
        File file = new File(fileName);
        if (file.exists()) {
            BufferedReader reader = null;
            try {
                reader = new BufferedReader(new FileReader(file));
                String tempString = null;
                while ((tempString = reader.readLine()) != null) {
                    sb.append(tempString + "\n");
                }
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (reader != null) {
                    try {
                        reader.close();
                    } catch (IOException e1) {
                    }
                }
            }
        }

        return sb.toString();
    }

    public static String cutThePath(String path) {
        if (path != null && !path.equals("")) {
            return "/sdcard/" + path.substring(path.indexOf("bugly"));
        }
        return path;
    }

    /**
     * 返回最新的日志文件
     *
     * @param files
     * @return
     */
    public static String findTheNewestFile(File[] files) {
        List<Long> fileNmaes = new ArrayList<Long>();
        if (files != null) {
            for (File file : files) {
                if (file.getName().contains(".log")) {
                    String name = file.getName().replace(".log", "");
                    fileNmaes.add(Long.parseLong(name));
                }
            }
        }
        //获取最新的日志文件
        Long newestFile = new Long(0);
        for (int i = 0; i < fileNmaes.size(); i++) {
            if (newestFile < fileNmaes.get(i)) {
                newestFile = fileNmaes.get(i);
            }
        }

        return newestFile.toString() + ".log";
    }

    /**
     * 判断是否有指定类型的文件
     *
     * @param path
     * @param ext
     * @return
     */
    public static boolean hasExtFiles(String path, String ext){
        List<String> list = FileUtil.getFilePathByExt(path, ext);
        if(list != null && list.size() > 0){
            return true;
        }else{
            return false;
        }
    }

    /**
     * 根据后缀名获取文件列表
     *
     * @param filePath
     * @param ext
     * @return
     */
    public static List<String> getFilePathByExt(String filePath, String ext) {
        List<String> results = new ArrayList<String>();
        File[] files = new File(filePath).listFiles();
        if (files == null) {
            return results;
        }
        for (File file : files) {
            String fileName = file.getName();
            if (fileName.endsWith(ext)) {
                results.add(file.getAbsolutePath());
            }
        }
        return results;
    }

    public static List<String> getFileNameByExt(String filePath, String ext) {
        List<String> results = new ArrayList<String>();
        File[] files = new File(filePath).listFiles();
        if (files == null) {
            return results;
        }
        for (File file : files) {
            String fileName = file.getName();
            if (fileName.endsWith(ext)) {
                results.add(file.getName());
            }
        }
        return results;
    }

    /**
     * 删除指定后缀名的文件
     *
     * @param path
     * @param ext
     */
    public static void deleteFileByExt(String path, String ext){
        List<String> list = FileUtil.getFilePathByExt(path, ext);
        if(list != null && list.size() > 0){
            int size = list.size();
            for(int i=0; i<size; i++){
                deleteFile(new File(list.get(i)));
            }
        }
    }

    /**
     * 获取文件夹列表
     *
     * @param filePath
     * @return
     */
    public static List<String> getDirs(String filePath) {
        List<String> dirs = new ArrayList<String>();
        File[] files = new File(filePath).listFiles();
        if (files == null) {
            return dirs;
        }
        for (File file : files) {
            if(file.isDirectory()){
                dirs.add(file.getAbsolutePath());
            }
        }
        return dirs;
    }


}
