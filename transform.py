import bs4
import re


def findn(n, s) -> bool:
    with open(".\\.done\\" + n + '.txt', "r") as e:
        for i in e:
            if str(i) == str(s)+'\n':
                return True
        return False


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
    cfilename = ".\\problems\\" + filename
    file = open(cfilename, "w", encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()
