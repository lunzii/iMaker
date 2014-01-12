//
//  FirstViewController.m
//  iMage
//
//  Created by lunzii on 14-1-11.
//  Copyright (c) 2014年 olunx. All rights reserved.
//

#import "FirstViewController.h"

@interface FirstViewController ()

@end

@implementation FirstViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    UIWebView *webView = [[UIWebView alloc] initWithFrame:CGRectMake(0, 20, 320, 500)];
    NSURLRequest *request =[NSURLRequest requestWithURL:[NSURL URLWithString:@"http://192.168.1.108:7788/m/"]];
    [self.view addSubview: webView];
    [webView loadRequest:request];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
