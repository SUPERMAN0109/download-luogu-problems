import os
import re
import urllib.request
import urllib.error
import bs4

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
    print("准备爬取UVA题库")
    if not UVAProblems():
        return
    print("UVA题库爬取完毕")


def addno(s):
    problems = open("error.txt", "a")
    problems.writelines(str(s) + '\n')
    problems.close()


def UVAProblems() -> bool:
    minn = 100
    maxn = 13292
    for i in range(minn, maxn + 1):
        if os.path.exists(SavePath + r"\problems\UVA" + str(i) + ".md"):
            continue
        if findn("UVA" + str(i)):
            continue
        print("正在爬取UVA{}...".format(i), end="")
        html = getHTML(baseUrl + 'UVA' + str(i))
        if html == "internet":
            return False
        if html == "error":
            addno("UVA" + str(i))
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...", end="")
            saveData(problemMD, "UVA" + str(i) + ".md")
            print("保存成功！")
    return False


def SPOJProblems() -> bool:
    minn = 1
    maxn = 34127
    for i in range(minn, maxn + 1):
        if os.path.exists(SavePath + r"\problems\SP" + str(i) + ".md"):
            continue
        if findn("SP" + str(i)):
            continue
        print("正在爬取SP{}...".format(i), end="")
        html = getHTML(baseUrl + 'SP' + str(i))
        if html == "internet":
            return False
        if html == "error":
            addno("SP" + str(i))
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...", end="")
            saveData(problemMD, "SP" + str(i) + ".md")
            print("保存成功！")
    return True


def CFProblems() -> bool:
    minn = 1
    maxn = 1754
    for i in range(minn, maxn + 1):
        for j in "ABCDEFGHIJKL":
            if os.path.exists(SavePath + r"\problems\CF" + str(i) + j + ".md"):
                continue
            if findn('CF' + str(i) + j):
                continue
            print("正在爬取CF{}{}...".format(i, j), end="")
            html = getHTML(baseUrl + 'CF' + str(i) + j)
            if html == "internet":
                return False
            if html == "error":
                addno('CF' + str(i) + j)
                print("爬取失败，可能是不存在该题或无权查看")
            else:
                problemMD = getMD(html)
                print("爬取成功！正在保存...", end="")
                saveData(problemMD, "CF" + str(i) + j + ".md")
                print("保存成功！")
    return True


def BasicProblems() -> bool:
    minn = 2001
    maxn = 2148
    for i in range(minn, maxn + 1):
        if os.path.exists(SavePath + r"\problems\B" + str(i) + ".md"):
            continue
        if findn("B" + str(i)):
            continue
        print("正在爬取B{}...".format(i), end="")
        html = getHTML(baseUrl + 'B' + str(i))
        if html == "internet":
            return False
        if html == "error":
            addno("B" + str(i))
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...", end="")
            saveData(problemMD, "B" + str(i) + ".md")
            print("保存成功！")

    minn = 3600
    maxn = 3675
    for i in range(minn, maxn + 1):
        if os.path.exists(SavePath + r"\problems\B" + str(i) + ".md"):
            continue
        if findn("B" + str(i)):
            continue
        print("正在爬取B{}...".format(i), end="")
        html = getHTML(baseUrl + 'B' + str(i))
        if html == "internet":
            return False
        if html == "error":
            addno("B" + str(i))
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...", end="")
            saveData(problemMD, "B" + str(i) + ".md")
            print("保存成功！")
    return True


def findn(s) -> bool:
    with open("error.txt", "r") as e:
        for i in e:
            if str(i) == str(s + "\n"):
                return True
        return False


def mainProblems() -> bool:
    minn = 1000
    maxn = 8596
    for i in range(minn, maxn + 1):
        if os.path.exists(SavePath + r"\problems\P" + str(i) + ".md"):
            continue
        if findn("P" + str(i)):
            continue
        print("正在爬取P{}...".format(i), end="")
        html = getHTML(baseUrl + "P" + str(i))
        if html == "internet":
            return False
        if html == "error":
            addno("P" + str(i))
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...", end="")
            saveData(problemMD, "P" + str(i) + ".md")
            print("保存成功！")
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
    a = open("error.txt", "a")
    a.close()
    main()
