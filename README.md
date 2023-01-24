# 洛谷题目下载

![stars](https://img.shields.io/github/stars/SUPERMAN0109/download-luogu-problems.svg)

在这里，可以批量下载洛谷的题目

## 项目目录

```
├──.done #存放每一类题目中已经下载完的题目的页码
│   ├── AT.txt
│   ├── B.txt
│   ├── CF.txt
│   ├── P.txt
│   ├── SP.txt
│   ├── UVA.txt
├── sql # 存放相关数据库sql语句
│   ├── table_create.sql
│   └── insert_tags.sql
├── img # 存放用于此markdown中的图片
│   ├── google.png
│   ├── list.png
│   ├── problem.png
│   ├── problems.png
│   └── tags_problems_link.png
├── problems # 存放每道题目的markdown文件
│   ├── P1000.md
│   ├── P1001.md
│   ├── ...
├── check.py # 检查程序，用于在下载完后运行检查时候有题目更新
├── config.toml # 配置文件，配置有关MySQL的数据库信息
├── download.py # 下载程序，用于进行第一次下载（下载途中如有中断，可以继续运行此程序进行下载）
├── list.xlsx # 工作表，用于存放下载完后的题目信息
```

其中`problems`文件夹，`.done`文件夹，`config.toml`，`list.xlsx`是运行`download.py`后才会产生的

## 项目环境

* python 3.10
* mysql 8.0

### 使用的程序

* python文件及运行 -> Pycharm
* sql文件及数据库处理 -> DataGrip

## 使用

* 克隆项目
* 安装相关库

```commandline
pip install bs4
pip install openpyxl
pip install toml
pip install selenium
pip install pymysql
pip install sqlalchemy
pip install pandas
```

* 安装谷歌浏览器驱动
  此外，如果没有安装谷歌浏览器的驱动，请前往<https://chromedriver.storage.googleapis.com/index.html>寻找自己的谷歌浏览器版本号下载相应的驱动下载，并吧其添加到系统环境变量
  * 确定谷歌浏览器版本
   在浏览器输入<chrome://settings/help>，如下图，即可知道版本号
   ![Google Chrome版本](./img/google.png)

* 配置数据库
  * 来到sql目录下，在命令行进入mysql  
   `mysql -u 'username' -p`
  * 插入数据

  ```mysql
  source table_create.sql;
  source insert_tags.sql;
  ```

* 输入数据库信息
  在主目录创建config.toml文件，按照以下格式输入数据库信息。

```toml
USE_MYSQL = true           #是否使用数据库，是填true，否填false，如果填false，后面可不填
HOST = "localhost"
PORT = 3306
USERNAME = "root"
PASSWORD = "admin123456"
```

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
v3.1 可以将题目数据加载到MySQL数据库中  
v3.2 修改了一下格式，并将配置文件从python文件转为toml文件，更简单  
v3.2.2 修改了一下本文件，更改了一些错误，并对内容进行了添加

## 数据库说明

在新建的数据库luogu_problems中，一共有3个表，分别为tags,problems,tags_problems_link。

* tags表用来存储每个标签对应的id号，方便搜索
  * id列储存每个id的编号
  * name列储存每个标签的名称
* problems表用来存储每一道题对应的题号、题目名称和难度
  * numb列存储每道题的题目编号
  * name列存储每道题的题目名称
  * difficulty列存储每道题的题目难度
* tags_problems_link表 相当于中间关系表，将标签和题目连起来
  * id指的是编号，在此无实际意义
  * tags_id指标签的id号，即标签在tags表中的id
  * problems_title指的是题目的编号，即在problems表中的numb列

## 爬取成果展示

* 下载的题目 ![problem](./img/problem.png)
* 题目信息的Excel表 ![list](./img/list.png)
* MySQL数据库
  * problems表 ![problems](./img/problems.png)
  * tags_problems_link表 ![tags_problems_link](./img/tags_problems_link.png)

## 参考资料

在以上的版本中，有些参考了下面两篇博客的程序  
[用python+selenium库爬洛谷题库（人生第一个爬虫）](https://blog.csdn.net/CrazyGuo2000/article/details/105598844)  
[【python爬虫】爬取洛谷习题并转为md格式](https://blog.csdn.net/qq_38243831/article/details/108909442)  
