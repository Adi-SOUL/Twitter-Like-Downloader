# Twitter-Like-Downloader

帮你自动下载你喜欢的推文中包含的图片

Help you to download the pics contained in the tweets which you liked

## 如何使用/How to use

### 安装/Install

1.使用Python(3.10)/With Python (3.10):

[Python 官网/ Official site of Python](https://www.python.org/downloads/)

[Python 安装/ Install Python](https://www.tutorialspoint.com/how-to-install-python-in-windows)

```shell

pip3 install -r requirements.txt

python main.py

```

2.或者从[此处](https://github.com/Adi-SOUL/Twitter-Like-Downloader/releases/tag/v0.1)下载/Or get the releases [here](https://github.com/Adi-SOUL/Twitter-Like-Downloader/releases/tag/v0.1)

### 参数设置/Settings

1.```Twitter API Token```处输入你的**Bearer Token**，具体情况可见：https://developer.twitter.com/en

Enter your **Bearer Token** at ```Twitter API Token```, see the details: https://developer.twitter.com/en

2.```Twitter ID```处输入与Like关联的账号id，例如[Elon Musk](https://twitter.com/elonmusk)的id是elonmusk，[小島秀夫](https://twitter.com/Kojima_Hideo)的id是Kojima_Hideo；

Enter the account id associated with Like in ```Twitter ID```, for example, the id of [Elon Musk](https://twitter.com/elonmusk) is elonmusk, and the id of [小島秀夫](https://twitter.com/Kojima_Hideo) is Kojima_Hideo;

3.```Save Path```是保存图片所在的根目录；```View Path```用于选择目录；

```Save Path``` is the directory where the picture is saved; ```View Path``` is used to select the directory;

4.```Number of cycles```：希望程序运行几轮；

```Number of cycles```: The number of cycles you want the program to run;

5.```Interval time```：每两轮之间间隔多少分钟。

```Interval time```: The minutes between each two cycles.

**记得点击OK，当然不点也没啥大事。**

**Remember to click OK, it’s ok if you don’t click ok.**

## 特别感谢/Special Thanks

[@TwitterDev](https://github.com/twitterdev)
