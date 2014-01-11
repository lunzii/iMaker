package com.viewpagerindicator.sample;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.view.ViewPager;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import com.viewpagerindicator.TabPageIndicator;

import java.util.ArrayList;
import java.util.List;

public class SampleTabsDefault extends FragmentActivity {
    private static final String[] CONTENT = new String[] { "照片", "相簿", "分享", "我"};

    private static final String[] URL = new String[] {
            "http://192.168.1.177:8080/m/",
            "http://192.168.1.177:8080/m_family/",
            "http://192.168.1.177:8080/m_share/",
            "http://192.168.1.177:8080/m_me/"
    };

    ArrayList<Fragment> views = new ArrayList<Fragment>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.simple_tabs);

        views.add(0,TestFragment.newInstance(URL[0]));
        views.add(1,TestFragment.newInstance(URL[1]));
        views.add(2,TestFragment.newInstance(URL[2]));
        views.add(3,TestFragment.newInstance(URL[3]));

        FragmentPagerAdapter adapter = new GoogleMusicAdapter(getSupportFragmentManager());

        ViewPager pager = (ViewPager)findViewById(R.id.pager);
        pager.setAdapter(adapter);

        TabPageIndicator indicator = (TabPageIndicator)findViewById(R.id.indicator);
        indicator.setViewPager(pager);

    }

    class GoogleMusicAdapter extends FragmentPagerAdapter {
        public GoogleMusicAdapter(FragmentManager fm) {
            super(fm);

        }

        @Override
        public Fragment getItem(int position) {
            return views.get(position);
        }

        @Override
        public CharSequence getPageTitle(int position) {
            return CONTENT[position % CONTENT.length].toUpperCase();
        }

        @Override
        public int getCount() {
          return CONTENT.length;
        }
    }

//    @Override
//    public boolean onCreateOptionsMenu(Menu menu) {
//        getMenuInflater().inflate(R.menu.menu, menu);
//        return true;
//    }
//
//    @Override
//    public boolean onOptionsItemSelected(MenuItem item) {
//        switch (item.getItemId()) {
//            case R.id.random:
//                return true;
//        }
//        return super.onOptionsItemSelected(item);
//    }
}
