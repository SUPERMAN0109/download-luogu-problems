import os
import re
import urllib.request,urllib.error
import bs4

baseUrl = "https://www.luogu.com.cn/problem/"
savePath = "D:\\programming documents\\python\\programs\\DownloadLuoguProblems\\problems\\"

def main():
    #print("即将开始爬取")
    #print("准备爬取主题库")
    #mainProblems()
    #print("主题库爬取完毕")
    #print("准备爬取入门题库")
    #BasicProblems()
    #print("入门题库爬取完毕")
    #print("准备爬取CF题库")
    #CFProblems()
    #print("CF题库爬取完毕")
    #print("准备爬取SPOJ题库")
    #SPOJProblems()
    #print("SPOJ题库爬取完毕")
    print("准备爬取UVA题库")
    UVAProblems()
    print("UVA题库爬取完毕")

def UVAProblems():
    minn = 100
    maxn = 13292
    for i in range(minn,maxn+1):
        print("正在爬取UVA{}...".format(i),end="")
        html = getHTML(baseUrl +'UVA'+str(i))
        if html == "error":
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...",end="")
            saveData(problemMD,"UVA"+str(i)+".md")
            print("保存成功！")

def SPOJProblems():
    minn = 1
    maxn = 34127
    for i in range(minn,maxn+1):
        print("正在爬取SP{}...".format(i),end="")
        html = getHTML(baseUrl +'SP'+str(i))
        if html == "error":
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...",end="")
            saveData(problemMD,"SP"+str(i)+".md")
            print("保存成功！")

def CFProblems():
    minn = 1
    maxn = 1754
    for i in range(minn,maxn+1):
        for j in "ABCDEFGHIJKL":
            print("正在爬取CF{}{}...".format(i,j),end="")
            html = getHTML(baseUrl +'CF'+str(i)+j)
            if html == "error":
               print("爬取失败，可能是不存在该题或无权查看")
            else:
                problemMD = getMD(html)
                print("爬取成功！正在保存...",end="")
                saveData(problemMD,"CF"+str(i)+j+".md")
                print("保存成功！")

def BasicProblems():
    minn = 2001
    maxn = 2148
    for i in range(minn,maxn+1):
        print("正在爬取B{}...".format(i),end="")
        html = getHTML(baseUrl +'B'+str(i))
        if html == "error":
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...",end="")
            saveData(problemMD,"B"+str(i)+".md")
            print("保存成功！")
    
    minn = 3600
    maxn = 3675
    for i in range(minn,maxn+1):
        print("正在爬取B{}...".format(i),end="")
        html = getHTML(baseUrl +'B'+str(i))
        if html == "error":
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...",end="")
            saveData(problemMD,"B"+str(i)+".md")
            print("保存成功！")


def mainProblems():
    minn = 1000
    maxn = 8596
    for i in range(minn,maxn+1):
        print("正在爬取P{}...".format(i),end="")
        html = getHTML(baseUrl +"P"+str(i))
        if html == "error":
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...",end="")
            saveData(problemMD,"P"+str(i)+".md")
            print("保存成功！")

def getHTML(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    if str(html).find("Exception") == -1:
        return html
    else:
        return "error"

def getMD(html):
    bs = bs4.BeautifulSoup(html,"html.parser")
    core = bs.select("article")[0]
    md = str(core)
    md = re.sub("<h1>","# ",md)
    md = re.sub("<h2>","## ",md)
    md = re.sub("<h3>","### ",md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md

def saveData(data,filename):
    cfilename = savePath + filename
    file = open(cfilename,"w",encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()

if __name__ == '__main__':
    if not os.path.exists(r'D:\programming documents\python\programs\DownloadLuoguProblems\problems'):
        os.mkdir(r'D:\programming documents\python\programs\DownloadLuoguProblems\problems')
    main()