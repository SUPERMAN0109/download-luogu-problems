#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import web_crawler


with open('path.txt', 'r') as path:
    SavePath = path.read()
if not os.path.exists(SavePath):
    os.makedirs(SavePath)
os.chdir(SavePath)


def main():
    print("即将开始爬取")
    print("准备爬取主题库")
    if not web_crawler.mainProblems():
        return
    print("主题库爬取完毕")
    print("准备爬取入门题库")
    if not web_crawler.BasicProblems():
        return
    print("入门题库爬取完毕")
    print("准备爬取CF题库")
    if not web_crawler.CFProblems():
        return
    print("CF题库爬取完毕")
    print("准备爬取SPOJ题库")
    if not web_crawler.SPOJProblems():
        return
    print("SPOJ题库爬取完毕")
    print("准备爬取AtCoder题库")
    if not web_crawler.ATProblems():
        return
    print("Atcoder题库爬取完毕")
    print("准备爬取UVA题库")
    if not web_crawler.UVAProblems():
        return
    print("UVA题库爬取完毕")


if __name__ == '__main__':
    if not os.path.exists(r'.\problems'):
        os.mkdir(r'.\problems')
    if not os.path.exists(r'.\.done'):
        os.mkdir(r'.\.done')
    if not os.path.exists(r'.\.done\P.txt'):
        a = open(r".\.done\P.txt", "a")
        a.close()
    if not os.path.exists(r'.\.done\B.txt'):
        a = open(r".\.done\B.txt", "a")
        a.close()
    if not os.path.exists(r'.\.done\CF.txt'):
        a = open(r".\.done\CF.txt", "a")
        a.close()
    if not os.path.exists(r'.\.done\SP.txt'):
        a = open(r".\.done\SP.txt", "a")
        a.close()
    if not os.path.exists(r'.\.done\AT.txt'):
        a = open(r".\.done\AT.txt", "a")
        a.close()
    if not os.path.exists(r'.\.done\UVA.txt'):
        a = open(r".\.done\UVA.txt", "a")
        a.close()
    main()
