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
    if str(html).find("Exception") == -1:
        return html
    else:
        return "error"


def problem(s) -> bool:
    baseUrl = "https://www.luogu.com.cn/problem/"
    if os.path.exists("\\problems\\" + s + '.md'):
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

def ATProblems() -> bool:
    browser = webdriver.Chrome()
    url = r"https://www.luogu.com.cn/problem/list?type=AT&page="
    try:
        browser.get(url + "1")
    except selenium.common.exceptions.WebDriverException:
        print("网络不稳定，请稍后再试")
        browser.quit()
        return False
    WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
    )
    pages = int(
        browser.find_element(By.XPATH, r'/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong').text)
    for i in range(1, pages + 1):
        if transform.findn('AT', i):
            continue
        try:
            browser.get(url + str(i))
        except selenium.common.exceptions.WebDriverException:
            print("网络不稳定，请稍后再试")
            browser.quit()
            return False
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
        )
        divs = browser.find_elements(By.XPATH, '/html/body/div/div[2]/main/div/div/div/div[1]/div[2]/div')
        for div in divs:
            numb = div.find_element(By.XPATH, 'span[2]').text
            if not problem(str(numb)):
                browser.quit()
                return False
        with open(r"\.done\AT.txt", "a") as e:
            e.write(str(i) + '\n')
    browser.quit()
    return True

def UVAProblems() -> bool:
    browser = webdriver.Chrome()
    url = r"https://www.luogu.com.cn/problem/list?type=UVA&page="
    try:
        browser.get(url + "1")
    except selenium.common.exceptions.WebDriverException:
        print("网络不稳定，请稍后再试")
        browser.quit()
        return False
    WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
    )
    pages = int(
        browser.find_element(By.XPATH, r'/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong').text)
    for i in range(1, pages + 1):
        if transform.findn('UVA', i):
            continue
        try:
            browser.get(url + str(i))
        except selenium.common.exceptions.WebDriverException:
            print("网络不稳定，请稍后再试")
            browser.quit()
            return False
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
        )
        divs = browser.find_elements(By.XPATH, '/html/body/div/div[2]/main/div/div/div/div[1]/div[2]/div')
        for div in divs:
            numb = div.find_element(By.XPATH, 'span[2]').text
            if not problem(str(numb)):
                browser.quit()
                return False
        with open(r"\.done\UVA.txt", "a") as e:
            e.write(str(i) + '\n')
    browser.quit()
    return True


def SPOJProblems() -> bool:
    browser = webdriver.Chrome()
    url = r"https://www.luogu.com.cn/problem/list?type=SP&page="
    try:
        browser.get(url + "1")
    except selenium.common.exceptions.WebDriverException:
        print("网络不稳定，请稍后再试")
        browser.quit()
        return False
    WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
    )
    pages = int(
        browser.find_element(By.XPATH, r'/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong').text)
    for i in range(1, pages + 1):
        if transform.findn('SP', i):
            continue
        try:
            browser.get(url + str(i))
        except selenium.common.exceptions.WebDriverException:
            print("网络不稳定，请稍后再试")
            browser.quit()
            return False
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
        )
        divs = browser.find_elements(By.XPATH, '/html/body/div/div[2]/main/div/div/div/div[1]/div[2]/div')
        for div in divs:
            numb = div.find_element(By.XPATH, 'span[2]').text
            if not problem(str(numb)):
                browser.quit()
                return False
        with open(r"\.done\SP.txt", "a") as e:
            e.write(str(i) + '\n')
    browser.quit()
    return True


def CFProblems() -> bool:
    browser = webdriver.Chrome()
    url = r"https://www.luogu.com.cn/problem/list?type=CF&page="
    try:
        browser.get(url + "1")
    except selenium.common.exceptions.WebDriverException:
        print("网络不稳定，请稍后再试")
        browser.quit()
        return False
    WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
    )
    pages = int(
        browser.find_element(By.XPATH, r'/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong').text)
    for i in range(1, pages + 1):
        if transform.findn('CF', i):
            continue
        try:
            browser.get(url + str(i))
        except selenium.common.exceptions.WebDriverException:
            print("网络不稳定，请稍后再试")
            browser.quit()
            return False
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
        )
        divs = browser.find_elements(By.XPATH, '/html/body/div/div[2]/main/div/div/div/div[1]/div[2]/div')
        for div in divs:
            numb = div.find_element(By.XPATH, 'span[2]').text
            if not problem(str(numb)):
                browser.quit()
                return False
        with open(r"\.done\CF.txt", "a") as e:
            e.write(str(i) + '\n')
    browser.quit()
    return True


def BasicProblems() -> bool:
    browser = webdriver.Chrome()
    url = r"https://www.luogu.com.cn/problem/list?type=B&page="
    try:
        browser.get(url + "1")
    except selenium.common.exceptions.WebDriverException:
        print("网络不稳定，请稍后再试")
        browser.quit()
        return False
    WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
    )
    pages = int(
        browser.find_element(By.XPATH, r'/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong').text)
    for i in range(1, pages + 1):
        if transform.findn('B', i):
            continue
        try:
            browser.get(url + str(i))
        except selenium.common.exceptions.WebDriverException:
            print("网络不稳定，请稍后再试")
            browser.quit()
            return False
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, r"/html/body/div/div[2]/main/div/div/div/div[2]/div/div/span/strong"))
        )
        divs = browser.find_elements(By.XPATH, '/html/body/div/div[2]/main/div/div/div/div[1]/div[2]/div')
        for div in divs:
            numb = div.find_element(By.XPATH, 'span[2]').text
            if not problem(str(numb)):
                browser.quit()
                return False
        with open(r"\.done\B.txt", "a") as e:
            e.write(str(i) + '\n')
    browser.quit()
    return True


def mainProblems() -> bool:
    browser = webdriver.Chrome()
    url = r"https://www.luogu.com.cn/problem/list?type=P&page="
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
    for i in range(1, pages+1):
        if transform.findn('P', i):
            continue
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
        for div in divs:
            numb = div.find_element(By.XPATH, 'span[2]').text
            if not problem(str(numb)):
                browser.quit()
                return False
        with open(r"\.done\P.txt", "a") as e:
            e.write(str(i)+'\n')
    browser.quit()
    return True
