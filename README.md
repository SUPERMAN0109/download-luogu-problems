# 洛谷题目下载

在这里，可以批量下载洛谷的题目

## 使用前的准备

由于其中用到了bs4, openpyxl,urllib,selenium，如果没有需要进行安装，在cmd输入以下命令

```commandline
pip install bs4
pip install openpyxl
pip install urllib
pip install selenium
```

此外，如果没有安装谷歌浏览器的驱动，请前往<https://chromedriver.storage.googleapis.com/index.html>寻找自己的谷歌浏览器版本号下载相应的驱动下载，并吧其添加到系统环境变量

### 确定谷歌浏览器版本

在浏览器输入<chrome://settings/help>，如下图，即可知道版本号
![Google Chrome版本](image.png)

## 使用方法

先在main.py所在的目录中创建path.txt文件，里面写入保存题目到电脑的位置，然后运行main.py即可

## 版本说明

v1.0 仅可下载主题库的  
v1.1 可以下载除了AtCoder的题目  
v1.2 可以继续上次的下载  
v1.3 继续下载时可以跳过之前下载不成功（没有这题）的题目  
v1.3.2 修改了v1.3的一个bug  
v1.4 可以更改保存目录  
v1.5 网络错误会有提醒，而不是直接退出  
v1.6 优化了一下格式  
v2.1 可以根据网页下载题目（不会出现下载不存在的题）  
v2.2 修改了一下，变成了多文件  
v2.3 修改了一个bug，更新了一下显示格式（显示当前在爬取哪一页）  
v2.4 可以爬取题目信息并分别保存为xlsx工作表的形式  
v2.5 简化了一下程序  
v2.6 改进了一下程序，加快运行速度  
v2.7 添加了一个下载完之后更新的程序（用于检查是否有新的题目）  

## 参考资料

在以上的版本中，有些参考了下面两篇博客的程序  
[用python+selenium库爬洛谷题库（人生第一个爬虫）](https://blog.csdn.net/CrazyGuo2000/article/details/105598844)  
[【python爬虫】爬取洛谷习题并转为md格式](https://blog.csdn.net/qq_38243831/article/details/108909442)  
