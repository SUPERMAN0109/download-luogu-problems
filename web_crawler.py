#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import transform
import os
import urllib.request
import urllib.error
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def getHTML(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.URLError:
        print('当前网络不稳定，请稍后再试')
        return "internet"
    html = response.read().decode('utf-8')
    if str(html).find("HttpException") == -1:
        return html
    else:
        return "error"


def problem(s) -> bool:
    baseUrl = "https://www.luogu.com.cn/problem/"
    if os.path.exists(".\\problems\\" + s + '.md'):
        return True
    print("正在爬取{}...".format(s), end="")
    html = getHTML(baseUrl + s)
    if html == "internet":
        return False
    if html == "error":
        print("爬取失败，可能是无权查看")
        return True
    problemMD = transform.getMD(html)
    print("爬取成功！正在保存...", end="")
    transform.saveData(problemMD, s + ".md")
    print("保存成功！")
    return True


def Problems(problem_type) -> bool:
    browser = webdriver.Chrome()
    url = r"https://www.luogu.com.cn/problem/list?type=" + problem_type + '&page='
    try:
        browser.get(url+"1")
    except selenium.common.exceptions.WebDriverException:
        print("网络不稳定，请稍后再试")
        browser.quit()
        return False
    WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located((By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
    )
    pages = int(browser.find_element(By.XPATH, r'/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong').text)
    print("一共要爬取{}页".format(pages))
    for i in range(1, pages+1):
        data_list = []
        if transform.findn(problem_type, i):
            continue
        print("正在爬取第{}页".format(i))
        try:
            browser.get(url+str(i))
        except selenium.common.exceptions.WebDriverException:
            print("网络不稳定，请稍后再试")
            browser.quit()
            return False
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
        )
        divs = browser.find_elements(By.XPATH, '/html/body/div/div[2]/main/div/div/div/div[1]/div[2]/div')
        numb_list = []
        title_list = []
        sour_list = []
        algo_list = []
        difficulty_list = []
        for div in divs:
            numb = div.find_element(By.XPATH, 'span[2]').text
            title = div.find_element(By.XPATH, 'div[1]/a').text
            temp = div.find_elements(By.XPATH, 'div[2]/div/a')
            sour = []
            for tem in temp:
                sour.append(tem.text)
            sour_str = '，'.join(sour)
            difficulty = div.find_element(By.XPATH, 'div[3]/a/span').text
            numb_list.append(numb)
            title_list.append(title)
            sour_list.append(sour_str)
            difficulty_list.append(difficulty)
            if not problem(str(numb)):
                browser.quit()
                return False
        browser.find_element(By.XPATH,'/html/body/div/div[2]/main/div/div/div/div[1]/div[1]/div/div[4]/span/a').click()
        for div in divs:
            temp = div.find_elements(By.XPATH, 'div[2]/div/a')
            algo = []
            for tem in temp:
                algo.append(tem.text)
            algo_str = '，'.join(algo)
            algo_list.append(algo_str)
        for numb, title, sour, algo, difficulty in zip(numb_list, title_list, sour_list, algo_list, difficulty_list):
            data = [numb, title, sour, algo, difficulty]
            data_list.append(data)
        transform.write_excel(data_list)
        with open(".\\.done\\"+problem_type+'.txt', "a") as e:
            e.write(str(i)+'\n')
        print("第{}页爬取完毕".format(i))
    browser.quit()
    return True
