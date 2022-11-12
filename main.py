import os
import re
import urllib.request
import urllib.error
import bs4
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

baseUrl = "https://www.luogu.com.cn/problem/"
with open('path.txt', 'r') as path:
    SavePath = path.read()
if not os.path.exists(SavePath):
    os.makedirs(SavePath)


def main():
    print("即将开始爬取")
    print("准备爬取主题库")
    if not mainProblems():
        return
    print("主题库爬取完毕")
    print("准备爬取入门题库")
    if not BasicProblems():
        return
    print("入门题库爬取完毕")
    print("准备爬取CF题库")
    if not CFProblems():
        return
    print("CF题库爬取完毕")
    print("准备爬取SPOJ题库")
    if not SPOJProblems():
        return
    print("SPOJ题库爬取完毕")
    print("准备爬取AtCoder题库")
    if not ATProblems():
        return
    print("Atcoder题库爬取完毕")
    print("准备爬取UVA题库")
    if not UVAProblems():
        return
    print("UVA题库爬取完毕")


def addno(s):
    problems = open("error.txt", "a")
    problems.writelines(str(s) + '\n')
    problems.close()


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
        if findn('AT', i):
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
        with open(SavePath + r"\.done\AT.txt", "a") as e:
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
        if findn('UVA', i):
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
        with open(SavePath + r"\.done\UVA.txt", "a") as e:
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
        if findn('SP', i):
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
        with open(SavePath + r"\.done\SP.txt", "a") as e:
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
        if findn('CF', i):
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
        with open(SavePath + r"\.done\CF.txt", "a") as e:
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
        if findn('B', i):
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
        with open(SavePath + r"\.done\B.txt", "a") as e:
            e.write(str(i) + '\n')
    browser.quit()
    return True


def findn(n, s) -> bool:
    with open(SavePath + "\\.done\\" + n + '.txt', "r") as e:
        for i in e:
            if str(i) == str(s)+'\n':
                return True
        return False


def problem(s) -> bool:
    if os.path.exists(SavePath + "\\problems\\" + s + '.md'):
        return True
    print("正在爬取{}...".format(s), end="")
    html = getHTML(baseUrl + s)
    if html == "internet":
        return False
    if html == "error":
        print("爬取失败，可能是无权查看")
        return True
    problemMD = getMD(html)
    print("爬取成功！正在保存...", end="")
    saveData(problemMD, s + ".md")
    print("保存成功！")
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
        if findn('P', i):
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
        with open(SavePath + r"\.done\P.txt", "a") as e:
            e.write(str(i)+'\n')
    browser.quit()
    return True


def getHTML(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
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


def getMD(html):
    bs = bs4.BeautifulSoup(html, "html.parser")
    core = bs.select("article")[0]
    md = str(core)
    md = re.sub("<h1>", "# ", md)
    md = re.sub("<h2>", "## ", md)
    md = re.sub("<h3>", "### ", md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>", "", md)
    return md


def saveData(data, filename):
    cfilename = SavePath + "\\problems\\" + filename
    file = open(cfilename, "w", encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()


if __name__ == '__main__':
    if not os.path.exists(SavePath + r'\problems'):
        os.mkdir(SavePath + r'\problems')
    if not os.path.exists(SavePath + r'\.done'):
        os.mkdir(SavePath + r'\.done')
    if not os.path.exists(SavePath + r'\.done\P.txt'):
        a = open(SavePath + r"\.done\P.txt", "a")
        a.close()
    if not os.path.exists(SavePath + r'\.done\B.txt'):
        a = open(SavePath + r"\.done\B.txt", "a")
        a.close()
    if not os.path.exists(SavePath + r'\.done\CF.txt'):
        a = open(SavePath + r"\.done\CF.txt", "a")
        a.close()
    if not os.path.exists(SavePath + r'\.done\SP.txt'):
        a = open(SavePath + r"\.done\SP.txt", "a")
        a.close()
    if not os.path.exists(SavePath + r'\.done\AT.txt'):
        a = open(SavePath + r"\.done\AT.txt", "a")
        a.close()
    if not os.path.exists(SavePath + r'\.done\UVA.txt'):
        a = open(SavePath + r"\.done\UVA.txt", "a")
        a.close()
    main()
