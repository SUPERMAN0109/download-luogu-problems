#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import web_crawler


with open('path.txt', 'r') as path:
    SavePath = path.read()
if not os.path.exists(SavePath):
    os.makedirs(SavePath)
os.chdir(SavePath)
problem_list = ['P', 'B', 'CF', 'SP', 'AT', 'uVA']
problem_list_name = ['主题库', '入门题库', 'CF题库', 'SPOJ题库', 'AtCoder题库', 'UVA题库']


def main():
    print("即将开始爬取")
    for i, j in zip(problem_list, problem_list_name):
        print("准备爬取"+j)
        if not web_crawler.Problems(i):
            return
        print(j+"爬取完毕")


if __name__ == '__main__':
    if not os.path.exists(r'.\problems'):
        os.mkdir(r'.\problems')
    if not os.path.exists(r'.\.done'):
        os.mkdir(r'.\.done')
    for i in problem_list:
        if not os.path.exists('.\\.done\\'+i+'.txt'):
            a = open('.\\.done\\'+i+'.txt', "a")
            a.close()
    main()
